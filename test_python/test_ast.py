from _ast import AST, Assign, Attribute, Call, Name
from collections import ChainMap
import sys
from typing import Any

def test_difflib():
    import difflib
    s1 = ['eggy\n', 'bacon\n', 'eggs\n', 'ham\n', 'guido\n']
    s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
    sys.stdout.writelines(difflib.context_diff(s1, s2, fromfile='before.py', tofile='after.py'))


def test_hashlib():
    import hashlib
    m = hashlib.md5('aaa'.encode('utf8'))
    print(m.hexdigest())
    m = hashlib.md5()
    m.update('aaa'.encode('utf8'))
    print(m.hexdigest())


def test_ast():
    import ast
    src = '''from review_queue.common.bbc import BBCHelper
bbc_key = "/moderation/tiktok_user_gif"
bbc_tenant = "moderation_conf"
bbc_config = BBCHelper.get(bbc_tenant, bbc_key)
def f(t, k):
    inner_conf = BBCHelper.get(t, k)
    return inner_conf
outer_conf = f(bbc_tenant, bbc_key)
bbc_lt, bbc_lk = bbc_tenant, bbc_key
ff = lambda : BBCHelper.get(bbc_lt, bbc_lk)
bbc_conf = ff()
    '''
    # print(ast.dump(ast.parse(src), indent=4))
    node = ast.parse(src)
    class MyV(ast.NodeVisitor):
        def __init__(self) -> None:
            self.in_call = self.is_bbc = self.is_bbc_get = self.is_assign = False
            self.bbc_get_args = []
            self.assign_list = []
            self.ctx = ChainMap({})
            super().__init__()

        # def generic_visit(self, node: AST) -> Any:
        #     return super().generic_visit(node)

        def visit_Assign(self, node: Assign):
            self.is_assign = True
            self.generic_visit(node)
            self.is_assign = False
        
        def visit_Call(self, node: Call):
            self.in_call = True
            self.generic_visit(node)
            self.in_call = False
            if self.is_bbc_get:
                print(self.bbc_get_args)
                self.bbc_get_args = []
                self.is_bbc = self.is_bbc_get = False

        def visit_Attribute(self, node: Attribute):
            self.generic_visit(node)
            if self.in_call and self.is_bbc:
                self.is_bbc_get = node.attr == 'get'

        def visit_Name(self, node: Name):
            if self.in_call and node.id == 'BBCHelper':
                self.is_bbc = True
            elif self.is_bbc_get:
                self.bbc_get_args.append(node.id)
            elif self.is_assign:
                self.assign_list.append(node.id)
            self.generic_visit(node)

    MyV().visit(node)


def md_ast():
    import mistletoe
    from mistletoe.ast_renderer import ASTRenderer
    with open('output.json', 'w') as output:
        with open('/Users/bytedance/notes/game/sgs/notes.md') as fin:
            with ASTRenderer() as renderer:
                doc = mistletoe.Document(fin)
                output.write(renderer.render(doc))


if __name__ == '__main__':
    test_difflib()
    # test_ast()
    # md_ast()

