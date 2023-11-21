class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num = 0
        all_min_index = prices.index(min(prices))
        r_max_index = len(prices[:all_min_index]) + prices[all_min_index:].index(max(prices[all_min_index:]))
        if all_min_index != r_max_index:
            if num < prices[r_max_index] - prices[all_min_index]:
                num = prices[r_max_index] - prices[all_min_index]
        while True:
            all_min_index = prices.index(min(prices))
            if prices[:all_min_index] != []:
                l_min_index = prices.index(min(prices[:all_min_index]))
            else:
                return num
            l_max_index = len(prices[:l_min_index]) + prices[l_min_index:all_min_index].index(max(prices[l_min_index:all_min_index]))
            if l_min_index == l_max_index:
                for _ in range(l_max_index - l_min_index +1):
                    prices.pop(l_min_index)
            else:
                if num < prices[l_max_index] - prices[l_min_index]:
                    num = prices[l_max_index] - prices[l_min_index]
                for _ in range(l_max_index - l_min_index +1):
                    prices.pop(l_min_index)