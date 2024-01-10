from antlr4 import *
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser
from Python3Visitor import Python3Visitor

class PythonToJavaScriptVisitor(Python3Visitor):
    def __init__(self):
        self.indent_count = 0
        self.indent = "    "
    
    def visitFile_input(self, ctx):
        # Generate code for the entire file
        code = ""
        for child in ctx.getChildren():
            result = self.visit(child)
            if result:
                code += result
        return code
    
    def visitFuncdef(self, ctx):
        # Generate code for a function definition
        self.indent_count += 1
        name = ctx.NAME().getText()
        params = self.visit(ctx.parameters())
        if not params:
            params = ""
        body = self.visit(ctx.suite())
        return f"function {name}({params}) {{\n{body}}}\n"
    
    def visitParameters(self, ctx):
        # Generate code for a function's parameters
        params = []
        for child in ctx.getChildren():
            if child.getText() != ",":
                params.append(child.getText())
        if params != ['(', ')']:
            return ", ".join(params)
    
    def visitStmt(self, ctx):
    # Visit each statement in the suite
        if ctx.simple_stmt():
            return self.visit(ctx.simple_stmt())
        elif ctx.compound_stmt().if_stmt():
            return self.visitIf_stmt(ctx.compound_stmt().if_stmt())
        elif ctx.compound_stmt().for_stmt():
            return self.visitFor_stmt(ctx.compound_stmt().for_stmt())
        elif ctx.compound_stmt().while_stmt():
            return self.visitWhile_stmt(ctx.compound_stmt().while_stmt())
        elif ctx.compound_stmt().funcdef():
            return self.visitFuncdef(ctx.compound_stmt().funcdef())
        else:
            raise NotImplementedError("Statement type not yet implemented")
    
    def visitSimple_stmt(self, ctx):
        # Generate code for a simple statement
        code = ""
        for child in ctx.getChildren():
            tmp_code = child.getText()
            tmp_code = tmp_code.replace("print", "console.log")
            code += tmp_code
        return self.indent_count * self.indent + code + ";\n"

    def visitExpr_stmt(self, ctx):
        # Generate code for an expression statement
        lhs = self.visit(ctx.testlist_star_expr(0))
        rhs = self.visit(ctx.testlist_star_expr(1))
        return f"{lhs} = {rhs}"
    
    def visitAtom(self, ctx):
        # Generate code for an atom
        if ctx.STRING():
            return f'"{ctx.STRING().getText()[1:-1]}"'
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.NAME():
            return ctx.NAME().getText()
    
    def visitSuite(self, ctx):
        # Generate code for a suite of statements
        code = ""
        for child in ctx.getChildren():
            result = self.visit(child)
            if result is not None:
                code += result
        return code
    
    def visitIf_stmt(self, ctx):
        # Generate code for an if statement
        code = self.indent * self.indent_count + "if ("
        self.indent_count += 1
        tests = ctx.test()
        for i, test in enumerate(tests):
            code += self.visit(test)
            if i < len(tests) - 1:
                code += " && "
        code += ") {\n"
        code += self.visit(ctx.suite(0))
        self.indent_count -= 1
        code += self.indent * self.indent_count + "}\n"
        if ctx.ELSE():
            code += self.indent * self.indent_count + "else {\n"
            self.indent_count += 1
            code += self.visit(ctx.suite(1))
            self.indent_count -= 1
            code += self.indent * self.indent_count + "}\n"
        return code
    
    def visitWhile_stmt(self, ctx):
    # Generate code for a while loop
        condition = self.visit(ctx.test())
        code = self.indent * self.indent_count + f"while ({condition}) {{\n"
        self.indent_count += 1
        for stmt in ctx.suite():
            code += self.visit(stmt)
        self.indent_count -= 1
        code += self.indent * self.indent_count + "}\n"
        return code
    
    def visitTestlist(self, ctx:Python3Parser.TestlistContext):
        # Handle the case where testlist contains only a single item
        if len(ctx.test()) == 1:
            return self.visit(ctx.test(0))
        else:
            return "[" + ", ".join(self.visit(test) for test in ctx.test()) + "]"
        
    def visitFor_stmt(self, ctx):
    # Generate code for a for loop
        target = ctx.exprlist().getText()
        iterable = ctx.testlist().getText().replace("range(", "").replace(")", "")
        iterable = [int(x) for x in iterable.split(",")]

        if len(iterable) == 1:
            code = self.indent * self.indent_count + f"for (let {target} of {iterable[0]}) {{\n"
        else:
            code = self.indent * self.indent_count + "for (let i = {0}; i < {1}; i + {2}){{\n".format(*iterable)
        self.indent_count += 1
        for stmt in ctx.suite():
            code += self.visit(stmt)
        self.indent_count -= 1
        code += self.indent * self.indent_count + "}\n"
        return code
    
    def visitComp_op(self, ctx:Python3Parser.Comp_opContext):
        if ctx.LESS_THAN():
            return "<"
        elif ctx.GREATER_THAN():
            return ">"
        elif ctx.LT_EQ():
            return "<="
        elif ctx.GT_EQ():
            return ">="
        elif ctx.EQUALS():
            return "=="
        elif ctx.NOT_EQ_1() or ctx.NOT_EQ_2():
            return "!="
        else:
            return self.visitChildren(ctx)
    
    def visitComparison(self, ctx:Python3Parser.ComparisonContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1)) if ctx.expr(1) is not None else ""
        ops = [self.visit(op) for op in ctx.comp_op()]
        if ops:
            return " && ".join([f"{left} {op} {right}" for op in ops])
        return left
    
    def visitReturn_stmt(self, ctx):
    # Generate code for a return statement
        if ctx.test() is not None:
            return f"return {self.visit(ctx.test())};\n"
        else:
            return "return;\n"
        
if __name__ == '__main__':
    with open("code/code.py", "r+") as f:
        code = f.read()
    lexer = Python3Lexer(InputStream(code))
    parser = Python3Parser(CommonTokenStream(lexer))
    tree = parser.file_input()
    visitor = PythonToJavaScriptVisitor()
    js_code = visitor.visit(tree)
    js_code = js_code.replace("\n;", ";")
    with open("code/code.js", "w+") as f:
        f.write(js_code)
