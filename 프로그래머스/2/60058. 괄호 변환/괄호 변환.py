def divide(p):

    left, right = 0, 0
    for i, char in enumerate(p):
    
        left += (char == '(')
        right += (char == ')')
        
        if left == right:
            return p[:i+1], p[i+1:]

def good(p):

    stack = []
    for char in p:
    
        if char == '(':
            stack.append(char)
            
        elif stack:
            stack.pop()
            
        else:
            return False
            
    return True

def solution(p):

    if not p:
        return ""
    
    u, v = divide(p)
    
    if good(u):
        return u + solution(v)
    
    return "(" + solution(v) + ")" + "".join(')' if char == '(' else '(' for char in u[1:-1])