import matplotlib.pyplot as plt  


a = [7,1,5,3,6,4] 
a = [7,6,4,3,1]
b = []
for i in range(1,len(a)):
    b.append(a[i] - a[i-1]) 

print(a)
print(b)


"""
Brute force method: 
Start at the beginning, and evalate every after 
Start at the next day, and evaluate every after 
Keep going to n-1 days 
"""
def optimalPriceBruteForce(prices):
    max_profit = 0
    dates = []
    for buy_date_index in range(len(prices)-1): 
        for sell_date_index in range(buy_date_index, len(prices)):
            print(sell_date_index)
            if prices[sell_date_index] - prices[buy_date_index] > max_profit: 
                print("sold: ",sell_date_index, "  bought: ", buy_date_index) 
                max_profit = prices[sell_date_index] - prices[buy_date_index] 
                dates = [buy_date_index+1, sell_date_index+1] 
    return max_profit, dates

profit, dates = optimalPriceBruteForce(a)

print("optimal profit: ", profit, "dates(buy, sell): ",dates) 


fig, ax = plt.subplots(figsize=(6,6)) 
ax.plot([a for a in range(len(a))], a)   

plt.show() 