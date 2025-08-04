class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        l = 0
        maxlen = 0

        for r in range(len(fruits)):
            fruit = fruits[r]
            
            if fruit in basket:
                basket[fruit] += 1
            else:
                basket[fruit] = 1

            while len(basket) > 2:
                leftfruit = fruits[l]
                basket[leftfruit] -= 1
                if basket[leftfruit] == 0:
                    del basket[leftfruit]
                l += 1

            lenth = r - l + 1
            if lenth > maxlen:
                maxlen = lenth

        return maxlen
