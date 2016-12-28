#Ndabezinhle Ndebele
#Solving step algorithm problem 

#recursively solves step algorithm
def printSteps(ans,i,n):
    if(n < 0):
        return
    if(n == 0):
        ansStr = ""
        for h in range(0,i):
            ansStr += ans[h]
        print ansStr
        return
    
    ans[i] = '1'
    printSteps(ans,n -1,i++)
    ans[i] = '2'
    printSteps(ans,n - 2,i++)

n = 4
res = [0 for x in range(n)]
pathPrintUtil(res,0,n)


    
