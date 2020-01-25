# Problem Statement
# https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/


# logic ref: https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
from base import closing_opening_parenthesis_pairs
from stacks import BuildLinkedStack


class ExpressionConversion:
    POSTFIX = 'postfix'
    PREFIX = 'prefix'
    INFIX = 'infix'

    operators_precedence = {
        '-': 1,
        '+': 1,
        '*': 2,
        '/': 2,
        '^': 3,
    }

    opening_parenthesis = set(closing_opening_parenthesis_pairs.values())

    def __init__(self, expr_str, expr_type=INFIX):
        self.expr_str = expr_str
        self.expr_type = expr_type

    def validate_infix_expr(self):
        assert self.expr_type == self.INFIX, 'given expression is not infix expression'
        pass

    def validate_postfix_expr(self):
        pass

    def validate_prefix_expr(self):
        pass

    def infix_to_postfix(self, debug_mode=True):
        self.validate_infix_expr()

        postfix_expr_str = ''
        operator_stack = BuildLinkedStack().build()

        if debug_mode:
            print('Present char', '{: ^30}'.format('Postfix-str'), '{: ^30}'.format('Operator stack'), sep='\t\t')

        for char in self.expr_str:
            if debug_mode:
                print(char, '{: ^30}'.format(postfix_expr_str), '{: ^30}'.format(repr(operator_stack)), sep='\t\t\t|')

            if char in self.operators_precedence:
                while (not operator_stack.is_empty()) and (operator_stack.top not in self.opening_parenthesis) and self.operators_precedence[char] <= self.operators_precedence[operator_stack.top]:
                    postfix_expr_str = postfix_expr_str + operator_stack.pop()

                operator_stack.push(char)

            elif char in self.opening_parenthesis:
                operator_stack.push(char)

            elif char in closing_opening_parenthesis_pairs:
                corresponding_opening_parenthesis = closing_opening_parenthesis_pairs[char]
                while operator_stack.top and operator_stack.top != corresponding_opening_parenthesis:
                    postfix_expr_str += operator_stack.pop()

                operator_stack.pop()  # pop opening bracket

            else:
                postfix_expr_str = postfix_expr_str + char

        while not operator_stack.is_empty():
            postfix_expr_str += operator_stack.pop()

            if debug_mode:
                print(char, '{: ^30}'.format(postfix_expr_str), '{: ^30}'.format(repr(operator_stack)), sep='\t\t\t|')

        return postfix_expr_str


# driver code
def run():
    infix_expr = 'a+b*(c^d-e)^(f+g*h)-i'
    postfix_expr = ExpressionConversion(infix_expr).infix_to_postfix()

    print(f'\n\nInfix-expression: {infix_expr} \nPostfix-expression: {postfix_expr}')


if __name__ == '__main__':
    run()
