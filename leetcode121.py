price=[7,1,5,3,6,4]
buy_price=price[0]
profit=0
n=len(price)

for i in range(1,n):
    if buy_price>price[i]:
        buy_price=price[i]
    else:
        current_profit=price[i]-buy_price
        profit=max(profit,current_profit)
print(profit)




