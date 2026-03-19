class Solution(object):
    def maximumWealth(self, accounts):
        wealth = []
        
        for i in accounts:
            total = 0
            for j in range(len(i)):
                total = total + i[j]
            wealth.append(total)
        
        return max(wealth)


#  Test the function
accounts = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]

s = Solution()
print(s.maximumWealth(accounts))   # Output: 15 