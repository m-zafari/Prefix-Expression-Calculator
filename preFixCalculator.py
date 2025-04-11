#mohammad zafari
# mhdzafari80@gmail.com

def is_operand(k): 
    return k.isdigit() 
def calculated(expression): 
    stack = [] 
    for c in expression[::-1]: 
        if is_operand(c): 
            stack.append(int(c)) 
        else: 
            o1 = stack.pop() 
            o2 = stack.pop() 
  
            if c == '+': 
                stack.append(o1+ o2 ) 
  
            elif c == '-': 
                stack.append(o1- o2 ) 
  
            elif c == '*': 
                stack.append(o1* o2 ) 
  
            elif c == '/': 
                stack.append(o1 / o2 ) 
    return stack.pop() 
"""    
if __name__ == "__main__": 
    test1 = "-+8/632"
    print(test1)
    print(calculated(test1)) 
"""
