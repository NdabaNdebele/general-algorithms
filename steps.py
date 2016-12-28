#Ndabezinhle Ndebele
#Solving step algorithm problem 

#recursively solves step algorithm
def printSteps(res,n,i):
    if(n < 0):
        return
    if(n == 0):
        ansStr = ""
        for h in range(0,i):
            ansStr += str(res[h])
        print ansStr
        return
    
    res[i] = '1'
    printSteps(res,n -1,i+1)
    res[i] = '2'
    printSteps(res,n - 2,i+1)

n = 4
res = [0 for x in range(n)]
printSteps(res,n,0)


    
