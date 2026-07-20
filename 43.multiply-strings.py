#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# 311/311 cases passed (43 ms)
# Your runtime beats 28.79 % of python3 submissions
# Your memory usage beats 66.22 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is "0", the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize result array with zeros
        # The max possible length of the product is len(num1) + len(num2)
        res = [0] * (len(num1) + len(num2))
        
        # Reverse iterate through both strings to multiply digit by digit
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Calculate product of individual digits
                # ord(char) - ord('0') converts string digit to integer
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                # Indices in the 'res' array where this product contributes
                p1, p2 = i + j, i + j + 1
                
                # Add product to the current value at the lower position
                total = mul + res[p2]
                
                # Update the result array with the new digit and carry
                res[p2] = total % 10    # Single digit
                res[p1] += total // 10  # Carry to the next position
        
        # Convert the integer array back to a string
        result_str = "".join(map(str, res))
        
        # Remove leading zeros (e.g., "056088" -> "56088")
        return result_str.lstrip('0')  
# @lc code=end

