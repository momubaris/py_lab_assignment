X=[[0,1,2],
  [3,4,5],
  [6,7,8]]
Y=[[9,10,11],
  [12,13,14],
  [15,16,17]]
result=[[0,0,0],
       [0,0,0],
       [0,0,0,]]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j]=result[i][j]+(X[i][k]*Y[k][j])
for x in result:
    print(x)