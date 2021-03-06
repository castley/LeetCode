#Given a string of numbers and operators, return all possible results from computing all the different possible ways to 
# group numbers and operators. The valid operators are +, - and *.
# Example 1
# Input: "2-1-1".
#
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Output: [0, 2]
#
# Example 2
# Input: "2*3-4*5"
#
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10]

#
# 分治法（Divide and conquer），递归地将表达式按照运算符拆分为左右两半
#


class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        nums, ops = [], []
        input = re.split(r'(\D)', input)
        for x in input:
            if x.isdigit():
                nums.append(int(x))
            else:
                ops.append(x)
        return self.dfs(nums, ops)
        
    def calc(self, a, b, o):
        return {'+':lambda x,y:x+y, '-':lambda x,y:x-y, '*':lambda x,y:x*y}[o](a, b)
        
    def dfs(self, nums, ops):
        if not ops:
            return [nums[0]]
        ans = []
        for x in range(len(ops)):
            left = self.dfs(nums[:x+1], ops[:x])
            right = self.dfs(nums[x+1:], ops[x+1:])
            for l in left:
                for r in right:
                    ans.append(self.calc(l, r, ops[x]))
        return ans
