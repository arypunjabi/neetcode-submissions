class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        fewestCoins = {}
        for coin in coins:
            fewestCoins[coin] = 1

        for i in range(1, amount + 1):
            for coin in coins:
                if not ((i-coin) < 0) and i-coin in fewestCoins:
                    if i in fewestCoins:
                        fewestCoins[i] = min(fewestCoins[i], fewestCoins[i-coin] + 1)
                    else:
                        fewestCoins[i] = fewestCoins[i-coin] + 1
        if amount in fewestCoins:
            return fewestCoins[amount]
        return -1
