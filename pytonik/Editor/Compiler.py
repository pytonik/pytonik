from pytonik.Editor._Fragment import _Fragment
from pytonik.util.Exception import TemplateSyntaxError, TemplateError, TemplateSyntaxError, TemplateContextError
from pytonik.Editor.Node import _Node, _Call,  _Root, _ScopableNode, _Text, _Variable, _If, _Each, _Else, _Block
from pytonik.Editor.Resolver import *

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
