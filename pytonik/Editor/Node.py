from pytonik import App
from pytonik.util.Exception import TemplateSyntaxError, TemplateError, TemplateSyntaxError
from pytonik.Editor.Resolver import *
from pytonik.Log import Log
from pytonik.Version import *

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



class _Call(_Node):

    def process_fragment(self, fragment):
        
        try:
            #bits = WHITESPACE.
            self.bits = WHITESPACE.split(fragment)
            self.callable = self.bits[1]
            self.fragment = fragment
            self.args, self.kwargs = parse_params(self.bits[2:])

        except Exception as err:
            raise TemplateSyntaxError(fragment)

    
    def render(self, context):
        
        self.contxt = context

        ob_dir = [str(os.path.dirname(__file__).replace('Editor', '')) + str("Functions"), str(host) + str("/") + "model"]

        resolved_args, resolved_kwargs = [], {}

        for kind, value in self.args:
            if kind == 'name':
                value = value

            
            value = self._call_each(str(value))
            
            resolved_args.append(value)
            
        if PYVERSION_MA >= 2:
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
                item = ""
                for k, itc in enumerate(contsplit):

                    if 'it.' in itc:

                        ite = resolve(itc, self.contxt)
                        item = str(self.it).replace(itc, str(ite))
            
                    elif '..' in itc:
                        ite = resolve(itc, self.contxt)
                        item = str(self.it).replace(itc, str(ite))
                        
                    else:
                        try:
                            ite = resolve(itc, self.contxt)
                            item = str(self.it).replace(itc, str(ite))
                        except Exception as err:
                            err = ""
                return item

            elif len(contsplit) > 1:
                
                dic_ls = {}
                dict_r = ""
                
                for s in contsplit:

                    if 'it.'.lower() in s.lower():
                        dic_ls.update({s: resolve(s, self.contxt)})
                        dict_r = dict_local(self.it, dic_ls)

                    elif '..'.lower() in s.lower():
                        dic_ls.update({s: resolve(s, self.contxt)})
                        dict_r = dict_local(self.it, dic_ls)
                    else:
                        
                        try:
                            dic_ls.update({s: resolve(s, self.contxt)})
                            dict_r = dict_local(self.it, dic_ls)
                        except Exception as err:
                            err = ""
                        
                return  dict_r

            else:
                item = ""
                if 'it.' in self.it:
                    ite = resolve(self.it, self.contxt)
                    item = str(self.it).replace(self.it, ite)
                elif '..' in self.it:

                    ite = resolve(self.it, self.contxt)
                    item = str(self.it).replace(self.it, ite)
                else:
                    try:
                        ite = resolve(self.it, self.contxt)
                        item = str(self.it).replace(self.it, ite)
                    except Exception as err:
                        err = ""
                        
                return item

        elif '..' in context:
            item = ""
            for it in context.split('/'):
                if '..' in it:
                    ite = resolve(it, self.contxt)
                    item = str(context).replace(it, ite)
                else:
                    try:
                        ite = resolve(it, self.contxt)
                        item = str(context).replace(it, ite)
                    except Exception as err:
                        err = ""
            return item
        else:
            return context



class _Text(_Node):
    def process_fragment(self, fragment):
        self.text = fragment
    def render(self, context):
        
        return self.text
