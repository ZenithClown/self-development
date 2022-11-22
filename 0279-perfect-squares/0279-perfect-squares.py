class Solution:
    def check_two(self, num : int) -> bool:
        # CASE k = 2 : Fermat's Two Square Theorem
        # divide the numbers as long as possible with
        # the given bases `2, 5, 9`
        bases = [2, 5, 9]
        for base in bases:
            while (num % base) == 0: num //= base
        
        if (num % 3) == 0:
            return False
        elif (num in (0, 1, 13, 17)):
            return True
        
        i, j = 0, int(num ** 0.5)
        while i <= j:
            if (i * i) + (j * j) == num:
                return True
            elif (i * i) + (j * j) < num:
                i += 1
            elif (i * i) + (j * j) > num:
                j -= 1
            else:
                continue
                
        return False
        
    def numSquares(self, n: int) -> int:
        # https://leetcode.com/problems/perfect-squares/discuss/2837639
        # https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
        i = 1
        
        while (i * i) <= n:
            # CASE k = 1 : Rudd's One Square Theorem
            if (i * i) == n:
                return 1
            
            i += 1
            
        # implement second case
        if self.check_two(n):
            return 2
        
        # CASE k = 3 : Legendre's Three Square Theorem
        while not (n % 4):
            n //= 4
            
        if (n % 8) != 7:
            return 3
        
        # CASE k = 4 : Legrange's Four Square Theorem
        return 4