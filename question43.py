# Link: https://leetcode.com/problems/multiply-strings/description/
# Multiply Strings

def multiply(num1: str, num2: str) -> str:
        max_len = max(len(num1), len(num2))
        if max_len % 2 != 0:
            max_len += 1
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)
        
        
        mid = max_len // 2
        x1, x0 = int(num1[:mid]), int(num1[mid:])
        y1, y0 = int(num2[:mid]), int(num2[mid:])
        
        A = x1 * y1
        C = x0 * y0
        B = (x1+x0)*(y1+y0) - A - C
        
        
        karatusba = (10 ** (2 * mid)) * A + (10 ** mid) * B  + C
        print(karatusba) 

multiply("100", "11")