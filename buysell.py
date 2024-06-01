lst=[7,1,5,3,6,4]
stock_sell=lst[1]-lst[0]
max_val=stock_sell


print(stock_sell)

n=len(lst)
k=1


for i in range(k,n):
    stock_sell-=lst[i]-lst[i-k]
    max_val=max(max_val,stock_sell)
print(max_val)


