def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0 

def remove_brackets(string):
    prefix_exp = ''
    for char in string:
        if char != '(' and char != ')':
            prefix_exp += char
    return prefix_exp

def convertToPostfix(infix_expr):
    postfix_expr = ''
    stack = []
    for char in infix_expr:
        # if char.isalnum():  
        if ord(char) >= 48 and ord(char) <= 57:
            postfix_expr += char
        elif char == '(':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                postfix_expr += stack.pop()
            stack.pop() 
        else:  
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix_expr += stack.pop()
            stack.append(char)
    while stack:
        postfix_expr += stack.pop()
    return postfix_expr

def convertToPrefix(infix_expr):
    reverse = infix_expr[::-1]
    new = remove_brackets(reverse)
    new = ''
    for i in range(len(reverse)):
        if reverse[i] == '(':
            new += ')'
        elif reverse[i] == ')':
            new += '('
        else:
            new += reverse[i]
    prefix = convertToPostfix(new)[::-1]
    prefix_exp = remove_brackets(prefix)
    return prefix_exp

    
infix_expression = input("Enter an infix expression: ")
prefix_expression = convertToPrefix(infix_expression)
print("Prefix expression:", prefix_expression)


# print(name[::-1])