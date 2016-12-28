#Ndabezinhle Ndebele
#how many brackets are out of place

def Stringify(str):
    arr = []
    v = 0
    for i in str:
        if(i == "("):
            arr.append(i)
        elif(i == ")"):
            if(len(arr) == 0):
                v += 1
            else:
                arr.pop()
    print v + len(arr)

Stringify(")((()))")

