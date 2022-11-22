class Solution:
    def calculate(self, s : str) -> int:
        stack, n, sign = [0], 0, +1 # stack, number, sign
        for c in filter(lambda char : char != " ", s):
            # for all charecter in given string, ignore
            # the white space, or even can use the `"".join(ss.split())`
            if c.isdigit():
                # accumulate number from digits
                n = (10 * n) + int(c)
                
            # there are only +ve and -ve signs, which are
            # controlled using two of the signed elements
            if c == "+":
                stack[-1] += n * sign
                sign, n = 1, 0
            elif c == "-":
                stack[-1] += n * sign
                sign, n = -1, 0
            else:
                # else, we control the opening and closing
                # parenthesis, this is done in the stack, in
                # addition, the last element is updated
                if c == "(":
                    stack.extend([sign, 0])
                    sign, n = 1, 0
                elif c == ")":
                    l_num = (stack.pop() + n * sign) * stack.pop()
                    stack[-1] += l_num
                    sign, n = 1, 0
                    
        return stack[-1] + n * sign