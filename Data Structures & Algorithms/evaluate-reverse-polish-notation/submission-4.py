class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        total = 0
        stack= []
        for char in tokens:
            if char == "+":
                str(stack.append(int(stack.pop()) + int(stack.pop())))
            elif char =="-":
                val = int(stack.pop())
                str(stack.append((int(stack.pop()) - val)))
            elif char == "*":
                str(stack.append(int(stack.pop()) * int(stack.pop())))
            elif char == "/":
                right = int(stack.pop())
                left = int(stack.pop())
                str(stack.append(int(left / right)))
            else:
                stack.append(char)
        total = int(stack.pop())
        return total


                
        

        