import re, operator, ast, os, importlib, sys
from pytonik.util.Exception import TemplateSyntaxError, TemplateError, TemplateSyntaxError, TemplateContextError
from pytonik import App, Version

VAR_FRAGMENT = 0
OPEN_BLOCK_FRAGMENT = 1
CLOSE_BLOCK_FRAGMENT = 2
TEXT_FRAGMENT = 3
CLOSE_COMMENT_FRAGMENT = 4

VAR_TOKEN_START = '{{'
VAR_TOKEN_END = '}}'
BLOCK_TOKEN_START = '{%'
BLOCK_TOKEN_END = '%}'
COMMENT_TOKEN_START = '{#'
COMMENT_TOKEN_END = '#}'


#(%s.*?%s|%s.*?%s|%s.*?%s)
TOK_REGEX = (re.compile('(%s.*?%s|%s.*?%s|%s.*?%s)' % (
    re.escape(VAR_TOKEN_START),
    re.escape(VAR_TOKEN_END),
    re.escape(BLOCK_TOKEN_START),
    re.escape(BLOCK_TOKEN_END),
    re.escape(COMMENT_TOKEN_START),
    re.escape(COMMENT_TOKEN_END)
)))

TRANSLATOR_COMMENT_MARK = 'Comment'

WHITESPACE = re.compile("[\s]")
UPPARA = re.compile('\,+')

operator_lookup_table = {
    '<': operator.lt,
    '>': operator.gt,
    '==': operator.eq,
    '!=': operator.ne,
    '<=': operator.le,
    '>=': operator.ge,
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '//': operator.floordiv,
    '/': operator.truediv,
    '%': operator.mod,
    '**': operator.pow,
    '<<': operator.lshift,
    '>>': operator.rshift,
    '^': operator.xor,
}

if os.path.isdir(os.getcwd() + '/public'):
    host = os.getcwd()  # os.path.dirname(os.getcwd())

else:
    host = os.path.dirname(os.getcwd())


def eval_expression(expr):

    try:
        return 'literal', ast.literal_eval(expr)
    except Exception as err:
        return 'name', expr


def resolve(name, context):
    
    if name.startswith('..'):
        context = context.get('..', {})
        name = name[2:]
        

    try:
        for tok in name.split('.'):
            context = context[tok]
        return context
    except Exception as err:
        try:
            Ap = App.App()
            load = Ap.loadmodule()
            load.update({name: name})
            md = importlib.import_module(name, name)
            ob = getattr(md, name)
            return ob()
        except Exception as err:
            # name
            raise TemplateContextError(err)

    

def parse_params(params):
        new_args, args, kwargs = [], [], {}

        for param in params:

            if len(params) > 3:

                p = str(params).translate({ord(i): None for i in '"'})

                if '=' in p:

                    new_name = str(p).translate({ord(i): None for i in '"\',\[]'})
                    sln = new_name.split(" ")

                    for n in sln:

                        if '=' in n:

                            k, v = str(n).split("=")

                            kwargs[k] = eval_expression(str(v))
                        else:

                            new_n = str(n).translate({ord(i): None for i in '[]'})
                            new_args.append(new_n)


                    args.append(eval_expression(" ".join(new_args)))

                else:

                    args.append(eval_expression(p))
                break

            else:
                if '=' in param:
                    name, value = param.split('=')

                    kwargs[name] = eval_expression(str(value))
                else:
                    args.append(eval_expression(param))


        return args, kwargs


def dict_local(it, resolves={}):
    l = "" 
    for i, k in enumerate(resolves):
        if k in resolves:
            l = str(it).replace(k, str(resolves[k]))
        if len(resolves) > 1:
            return dict_local_next(l, resolves)
        else:
            return l


def dict_local_next(it, resolves):
    for i, k in enumerate(resolves):
        if k in it:
            it = it.replace(k, resolves[k])
    return it
