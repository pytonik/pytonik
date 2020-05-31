###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###



import re, operator, ast
from pytonik import Version, App
import os, importlib, sys
from pytonik.Log import Log

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


class TemplateError(Exception):
    pass


class TemplateContextError(TemplateError):

    def __init__(self, context_var):
        self.context_var = context_var


    def __str__(self):
        Log('').error("cannot resolve '%s'" % self.context_var)
        return "cannot resolve '%s'" % self.context_var


class TemplateSyntaxError(TemplateError):

    def __init__(self, error_syntax):
        self.error_syntax = error_syntax

    def __str__(self):
        Log('').error("'%s' seems like invalid syntax" % self.error_syntax)
        return "'%s' seems like invalid syntax" % self.error_syntax


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


class _Fragment(object):
    def __init__(self, raw_text):

        self.raw = raw_text

        self.clean = self.clean_fragment()

    def clean_fragment(self):
        if self.raw[:2] in (VAR_TOKEN_START, BLOCK_TOKEN_START):

            return self.raw.strip()[2:-2].strip()

        return self.raw

    @property
    def type(self):
        raw_start = self.raw[:2]
        if raw_start == VAR_TOKEN_START:
            return VAR_FRAGMENT
        elif raw_start == BLOCK_TOKEN_START:

            block = str('end{}'.format(self.clean[3:9]))

            return CLOSE_BLOCK_FRAGMENT if self.clean[:9] == block else OPEN_BLOCK_FRAGMENT

        elif raw_start == COMMENT_TOKEN_START:
            if self.clean.find(TRANSLATOR_COMMENT_MARK):
                self.clean[2:-2].strip()
            return CLOSE_COMMENT_FRAGMENT
        else:

            return TEXT_FRAGMENT



class _Node(object):
    creates_scope = False

    def __init__(self, fragment=None):
        self.children = []

        self.process_fragment(fragment)

    def process_fragment(self, fragment):

        pass

    def enter_scope(self):
        pass

    def render(self, context):

        pass

    def exit_scope(self):
        pass

    def render_children(self, context, children=None):


        if children is None:
            children = self.children

        def render_child(child):

            child_html = child.render(context)

            return '' if not child_html else str(child_html)

        return ''.join(map(render_child, children))


class _ScopableNode(_Node):
    creates_scope = True


class _Root(_Node):
    def render(self, context):

        return self.render_children(context)


class _Variable(_Node):
    def process_fragment(self, fragment):
        self.name = fragment

    def render(self, context):

        return resolve(self.name, context)


class _Each(_ScopableNode):

    def process_fragment(self, fragment):

        try:

            _, it = WHITESPACE.split(fragment, 1)
            self.it = eval_expression(it)

        except Exception as err:

            raise TemplateSyntaxError(fragment)

    def render(self, context):

        items = self.it[1] if self.it[0] == 'literal' else resolve(self.it[1], context)

        def render_item(item):
            Ap = App.App()
            load = Ap.loadmodule()

            load_m = {'..': context, 'it': item}

            load.update(load_m)

            return self.render_children(load)

        return ''.join(map(render_item, items))

class _Block(_Node):

    def process_fragment(self, fragment):

        try:
            it = WHITESPACE.split(fragment)

            self.block = eval_expression(it)

        except Exception as err:
            raise TemplateSyntaxError(fragment)

    def render(self, context):

        it = self.block[1]

        d, s = [], []
        try:

            for iv in it:
                if iv not in operator_lookup_table:
                    items = resolve(iv, context)
                    d.append(items)
                else:
                    s.append(iv)
            operator_lookup = s[0]
            try:
                return eval(operator_lookup.join(d))

            except Exception as err:
                return operator_lookup.join(d)

        except Exception as err:

            for iv in it:

                if iv not in operator_lookup_table:
                    d.append(iv)
                else:
                    s.append(iv)

            operator_lookup = s[0]
            try:
                return eval(operator_lookup.join(d))
            except Exception as err:
                return operator_lookup.join(d)





class _If(_ScopableNode):
    def process_fragment(self, fragment):
        bits = fragment.split()[1:]
        if len(bits) not in (1, 3):
            raise TemplateSyntaxError(fragment)
        self.lhs = eval_expression(bits[0])
        if len(bits) == 3:
            self.op = bits[1]
            self.rhs = eval_expression(bits[2])

    def render(self, context):

        lhs = self.resolve_side(self.lhs, context)

        if hasattr(self, 'op'):
            op = operator_lookup_table.get(self.op)
            if op is None:
                raise TemplateSyntaxError(self.op)
            rhs = self.resolve_side(self.rhs, context)
            exec_if_branch = op(lhs, rhs)
        else:
            exec_if_branch = operator.truth(lhs)


        self.if_branch, self.else_branch = self.split_children()
        return self.render_children(context, self.if_branch if exec_if_branch else self.else_branch)

    def resolve_side(self, side, context):

        return side[1] if side[0] == 'literal' else resolve(side[1], context)

    def exit_scope(self):
        self.if_branch, self.else_branch = self.split_children()

    def split_children(self):
        if_branch, else_branch = [], []
        curr = if_branch
        for child in self.children:
            if isinstance(child, _Else):
                curr = else_branch
                continue
            curr.append(child)
        return if_branch, else_branch


class _Else(_Node):
    def render(self, context):
        pass


def dict_local(it, resolves):

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
           l = str(it).replace(k, str(resolves[k]))
           return l

class _Call(_Node):

    def process_fragment(self, fragment):

        try:
            #bits = WHITESPACE.
            self.bits = WHITESPACE.split(fragment)
            self.callable = self.bits[1]
            self.fragment = fragment

            self.args, self.kwargs = self._parse_params(self.bits[2:])



        except Exception as err:
            raise TemplateSyntaxError(fragment)

    def _parse_params(self, params):
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

    def render(self, context):
        self.contxt = context

        ob_dir = [str(os.path.dirname(__file__).replace('Editor', '')) + str("Functions"), str(host) + str("/") + "model"]



        resolved_args, resolved_kwargs = [], {}


        for kind, value in self.args:

            if kind == 'name':
                value = value
            value = self._call_each(str(value))
            resolved_args.append(value)


        if Version.PYVERSION_MA >= 2:
            items  = self.kwargs.items()
        else:
            items = self.kwargs.iteritems()

        for key, (kind, value) in items:

            if kind == 'name':

                value = value

            value = self._call_each(str(value))
            try:
                valux = eval(value)
            except Exception as err:
                valux = value
            resolved_kwargs[key] = valux



        path = [str(ob_dir[0]) + "/" + str(self.callable) + ".py",  str(ob_dir[1]) + "/" + str(self.callable) + ".py"]


        sys.path.append(str(ob_dir[0]))
        sys.path.append(str(ob_dir[1]))


        importlib._RELOADING

        if os.path.isfile(path[0]) == True:


            md = importlib.import_module(self.callable, self.callable)


            ob = getattr(md, self.callable)



            if hasattr(ob(), '__call__') == True:

                calls = ""
                try:
                    newob = getattr(ob, ''.join(resolved_args).replace(" ", ""))
                    calls = newob(**resolved_kwargs)
                    
                except Exception as err:
                    try:
                        newob = getattr(ob(), ''.join(resolved_args).replace(" ", ""))
                        calls = newob(**resolved_kwargs)
                    except Exception as err:
                        try:
                            _cal = ob()
                            _new_cal = getattr(_cal, *resolved_args)
                            calls =  _new_cal(**resolved_kwargs)

                        except Exception as err:
                            try:
                                calls = ob(*resolved_args, **resolved_kwargs)
                            except Exception as err:
                                Log('').error(err)

                return calls
            else:
                raise TemplateError("'%s' is not a callable" % self.callable)

        elif os.path.isfile(path[1]) == True:


            md = importlib.import_module(self.callable, self.callable)
            ob = getattr(md, self.callable)


            if hasattr(ob(), '__call__'):

                calls = ""
                try:
                    newob = getattr(ob, ''.join(resolved_args).replace(" ", ""))
                    calls = newob(**resolved_kwargs)
                except Exception as err:

                    try:
                        newob = getattr(ob(), ''.join(resolved_args).replace(" ", ""))
                        calls = newob(**resolved_kwargs)
                    except Exception as err:
                        try:
                            _cal = ob()
                            _new_cal = getattr(_cal, *resolved_args)
                            calls = _new_cal(**resolved_kwargs)

                        except Exception as err:

                            try:
                                calls = ob(*resolved_args, **resolved_kwargs)

                            except Exception as err:
                                Log('').error(err)
                return calls
            else:
                raise TemplateError("'%s' is not a callable" % self.callable)

        else:
            raise TemplateError("'%s' module not found " % self.callable)

    def _call_each(self, context):

        if  VAR_TOKEN_START in context:
            self.it = str(context).translate({ord(i): None for i in '{VAR_TOKEN_START}{VAR_TOKEN_END}'.format(VAR_TOKEN_START = '{{', VAR_TOKEN_END = '}}')})
            oparatork = "/"
            for oparator_k,  oparator_v in operator_lookup_table.items():
                if oparator_k in self.it:
                    oparatork = oparator_k


            contsplit = self.it.split(oparatork)


            if len(contsplit) < 2:

                for k, itc in enumerate(contsplit):

                    if 'it.' in itc:

                        ite = resolve(itc, self.contxt)
                        item = str(self.it).replace(itc, str(ite))
                        return item
                    elif '..' in itc:

                        ite = resolve(itc, self.contxt)
                        item = str(self.it).replace(itc, str(ite))
                        return item
                    else:
                        ite = resolve(itc, self.contxt)
                        item = str(self.it).replace(itc, str(ite))
                        return item


            elif len(contsplit) > 1:

                dic_ls = {}
                for s in contsplit:

                    if 'it.'.lower() in s.lower():
                        dic_ls.update({s:resolve(s, self.contxt)})

                    elif '..'.lower() in s.lower():

                        dic_ls.update({s: resolve(s, self.contxt)})



                return dict_local(self.it,dic_ls)


            else:

                if 'it.' in self.it:
                    ite = resolve(self.it, self.contxt)
                    item = str(self.it).replace(self.it, ite)
                elif '..' in self.it:

                    ite = resolve(self.it, self.contxt)
                    item = str(self.it).replace(self.it, ite)

                return item



        elif '..' in context:

            for it in context.split('/'):
                if '..' in it:
                    ite = resolve(it, self.contxt)

                else:
                    ite = resolve(it, self.contxt)

                item = str(context).replace(it, ite)
                return item

        else:

            return context



class _Text(_Node):
    
    def process_fragment(self, fragment):
        self.text = fragment

    def render(self, context):
        return self.text


class Compiler(object):
    def __init__(self, template_string):
        self.template_string = template_string

    def each_fragment(self):


        for fragment in TOK_REGEX.split(self.template_string):

            if fragment:
                yield _Fragment(fragment)

    def compile(self):

        root = _Root()
        scope_stack = [root]

        for fragment in self.each_fragment():

            if not scope_stack:
                raise TemplateError('nesting issues')

            parent_scope = scope_stack[-1]


            if fragment.type == CLOSE_BLOCK_FRAGMENT:
                parent_scope.exit_scope()
                scope_stack.pop()
                continue

            new_node = self.create_node(fragment)

            if new_node:

                parent_scope.children.append(new_node)
                if new_node.creates_scope:
                    scope_stack.append(new_node)
                    new_node.enter_scope()

        return root

    def create_node(self, fragment):
        node_class = None
        if fragment.type == TEXT_FRAGMENT:
            node_class = _Text
        elif fragment.type == VAR_FRAGMENT:
            node_class = _Variable
        elif fragment.type == OPEN_BLOCK_FRAGMENT:
            cmd = fragment.clean.split()[0]

            if cmd == 'each':
                node_class = _Each
            elif cmd == 'if':
                node_class = _If
            elif cmd == 'else':
                node_class = _Else
            elif cmd == 'call':
                node_class = _Call
            else:
                node_class = _Block

        if node_class is None:
            raise TemplateSyntaxError(fragment)

        return node_class(fragment.clean)


class Template(object):
    def __init__(self, contents):
        self.contents = contents
        self.root = Compiler(contents).compile()



    def render(self, **kwargs):
        
        return str(self.root.render(kwargs)).replace('\ufeff', ' ')
