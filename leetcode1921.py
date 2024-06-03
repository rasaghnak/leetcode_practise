dist=[1,3,4]
speed=[1,1,1]

if len(dist)<len(speed):
    print("this is a inappropriate testcase")

time=[]

for i in range(len(dist)):
    time.append(int(dist[i]/speed[i]))

time.sort()

for j in range(len(time)):
    if time[j]==1:
        time[j]="X"
        
    else:
        time[j]-=1

print(time)