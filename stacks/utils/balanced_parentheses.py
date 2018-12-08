# Problem Statement
# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/


from stacks.build_stack import BuildLinkedStack


def are_parentheses_balanced(expression_str: str):

    closing_opening_parenthesis_pairs = {
        '}': '{',
        ']': '[',
        ')': '(',
        '>': '<',
    }
    opening_parentheses = set(closing_opening_parenthesis_pairs.values())

    stack = BuildLinkedStack().build()
    for char in expression_str:
        if char in opening_parentheses:
            stack.push(char)
        elif closing_opening_parenthesis_pairs.get(char, None):
            if stack.is_empty() or stack.pop() != closing_opening_parenthesis_pairs[char]:
                return False

    if not stack.is_empty():
        return False
    return True


# driver code
def run():
    str_expression = "{()}[]"
    print(f'Given str_expression: {str_expression}')

    if are_parentheses_balanced(str_expression):
        print('YES parentheses are balanced in given string.')
    else:
        print('NO parentheses are not balanced in given string.')


if __name__ == '__main__':
    run()
