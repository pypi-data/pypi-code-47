#!/usr/bin/python3

import ast
import operator as op
import sys

operators={ast.Add: op.add, ast.Sub: op.sub}
values={'a': 123, 'foo': 456}

def eval_ast(node):
    print(node)
    if (isinstance(node, ast.Num)):
        return node.n
    elif (isinstance(node, ast.UnaryOp)):
        return operators[type(node.op)](eval_ast(node))
    elif (isinstance(node, ast.BinOp)):
        return operators[type(node.op)](eval_ast(node.left), eval_ast(node.right))
    elif (isinstance(node, ast.Name)):
        return values[node.id]
    else:
        raise TypeError(node)

def parse_expression(e):
    parsed = ast.parse(e, mode='eval')
    return parsed

def eval_expression(parsed, result, values):
    return eval_ast(parsed.body)

def main():
    e = " ".join(sys.argv[1:])
    print(e)
    parsed = ast.parse(e, mode='eval')
    print(eval_ast(parsed.body))

if __name__ == "__main__":
    main()

        
