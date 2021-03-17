x = int(float(input("Enter a number: ")))  # input為string, 一定要先轉float再轉int.

y=np.zeros((x+1,x+1))

#print (y)
y[0,0]=1

if x>=1:  # 都要冒號
    for r in range(1,x+1):  # 不會執行到range 序列終止值
        for c in range(0,x+1):  # 都要縮排
            if c==0:
                y[r,c]=1
            else:
                y[r,c]=y[r-1,c-1]+y[r-1,c]
           
print (y[x,:])  # 不要忘了array 提取是用[中括號]
