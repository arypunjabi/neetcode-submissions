class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        denomArr = [0] * (amount + 1)
        denomArr[0] = 1

        for n in coins:
            for i in range(n, amount + 1):
                denomArr[i] = denomArr[i] + denomArr[i-n]

        return denomArr[amount]
