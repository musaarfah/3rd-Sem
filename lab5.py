class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class MyStack:
    def __init__(self):
        self.head=None
        self.count=0

    def display(self):
        if not self.head:
            print('stack is empty')
            return
        curr=self.head
        while curr:
            print(curr.data,end=' ')
            curr=curr.next

        print()

    
    def push(self,data):
        newNode = Node(data)
        newNode.next=self.head
        self.head=newNode
        self.count+=1

    def pop(self):
        if not self.isempty():
            data=self.head.data

            self.head=self.head.next
            self.count-=1
            return data
        else:
            return('Empty stack')
    
    def peek(self):
        return self.head.data
        
    
    def isempty(self):
        if self.head is None:
            return True
        return False
    
    def size(self):
        return self.count


def reverse_string(string):
    reversed_expression = string[::-1] 
    reversed_with_swapped_brackets = ''
    for char in reversed_expression:
        if char == '(':
            reversed_with_swapped_brackets += ')'
        elif char == ')':
            reversed_with_swapped_brackets += '('
        else:
            reversed_with_swapped_brackets += char
    
    def reverse_substring(string):
        return string[::-1]
    
    final_reversed_string = ''
    temp = ''
    for char in reversed_with_swapped_brackets:
        if char == '(':
            final_reversed_string += reverse_substring(temp)
            temp = ''
            final_reversed_string += char
        elif char == ')':
            final_reversed_string += reverse_substring(temp)
            temp = ''
            final_reversed_string += char
        else:
            temp += char
    final_reversed_string += reverse_substring(temp)
    
    return final_reversed_string





def convertTooPost(string):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = ''
    
    for charac in string:
        if charac.isalnum():
            postfix += charac
        elif charac == '(':
            stack.append(charac)
        elif charac == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  
        else:  
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(charac, 0):
                postfix += stack.pop()
            stack.append(charac)
    
    while stack:
        postfix += stack.pop()
    
    return postfix


def convertToPost(string):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = ''

    for charac in string:
        if charac.isalnum():
            postfix += charac
        elif charac == '(':
            stack.append(charac)
        elif charac == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            if stack:  
                stack.pop()  
            else:
                raise ValueError("Unbalanced parentheses")
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(charac, 0):
                postfix += stack.pop()
            stack.append(charac)

    while stack:
        if stack[-1] == '(':
            raise ValueError("Unbalanced parentheses")
        postfix += stack.pop()

    return postfix


def convertTooPre(string):
    new_string=reverse_string(string)
    convertToPost(new_string)

    
# def convertTopostfix(string):
#     para='()'
#     operators='/*+-'

#     postfix=''
#     operator_stack=MyStack()

#     for i in range(len(string)):
#         if string[i] not in operators and para:
#             postfix+=f'{string[i]}'

#         elif string[i] in operators:
#             j=0
#             while string[i] != operators[j]:
#                 if (not operator_stack.isempty()) and \
                
                
#                 postfix+=operators[j]
#                 operator_stack.pop()
#                 j+=1

#             operator_stack.push(string[i])

#         elif string[i] =='(':
#             operator_stack.push(string[i])

#         elif string[i]==')':


def main():
    # s1=MyStack()
    # s1.push(2)
    # s1.push(3)
    # s1.push(4)
    # s1.display()
    # s1.pop()
    # s1.display()

    # infix_string = input("Enter an infix expression: ")
    # postfix_expression = convertTooPost(infix_expression)
    # print("After Conversion:", postfix_expression)()

    infix_expression = input("Enter an infix expression: ")
    prefix_expression = convertTooPre(infix_expression)
    print("After Conversion:", prefix_expression)

    # convertTooPre(input("Enter a Postfix Expression : "))

    # print(reverse_string('(A+B)*C-D'))




main()