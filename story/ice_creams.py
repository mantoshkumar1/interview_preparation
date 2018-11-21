"""
A person has X amount of money and wants to buy ice-creams. The cost of each ice-cream is Y.
For every purchase of ice-creams he gets 1 unit of money which could be used to buy ice-creams.

Find the number of ice-creams he can buy.
"""
class Solution:
    def approach2(self, money, cost_per_ice):
        coupon_money = 0
        ans = 0
        while money > 0:
            if coupon_money == cost_per_ice:
                coupon_money = 1
                ans += 1
                continue
            
            if money >= cost_per_ice:
                ans += 1
                money -= cost_per_ice
                coupon_money += 1
            else:
                break
    
        ans = ans + (money+coupon_money)//cost_per_ice
        return ans
        
    def get_max_num_ice_creams(self, money, cost_per_ice, ans=0):
        if money < cost_per_ice:
            return ans
        
        num_bought_ice = money // cost_per_ice
        ans += num_bought_ice
        
        money = money % cost_per_ice
        coupon_money = num_bought_ice
        money = money + coupon_money
        
        return self.get_max_num_ice_creams(money, cost_per_ice, ans)
        
    def get_num_ice_creams(self, money, cost_per_ice):
        return self.get_max_num_ice_creams(money, cost_per_ice)
    
a = Solution()
assert 4 == a.get_num_ice_creams(5, 2)
assert 5 == a.get_num_ice_creams(6, 2)

assert 4 == a.approach2(5, 2)
assert 5 == a.approach2(6, 2)
