from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def __str__(self):
        return f"{self.stack}"

    def push(self,value):
        return self.stack.append(value)
    
    def pop(self,):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        if len(self.stack) ==0:
            return True
        return False
    
    def lenght(self):
        return len(self.stack)

    def reverse_value(self,value):
        return value[::-1]
        
def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr


def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0

    

st = Stack()
st.push(34)
st.push(74)
st.push(20)
st.push(80)
st.push(100)
print(st.pop())
print(st)
print(st.reverse_value("We will conquer COVI-19"))






