#Ndabezinhle Ndebele
#Finds Deletion Distance of two strings

def checkString(i,str):
    v = 0
    for j in str:
        if( i == j):
            v += 1
    return v

def deletion_distance(str1,str2):
    v = 0
    for i in str1:
        v += checkString(i,str2)
    return len(str1) - v

def disParse(str1,str2):
    v = 0
    v = deletion_distance(str1,str2) + deletion_distance(str2,str1)
    print "The Deletion Sequence is " + str(v)
    
arr = raw_input("input two strings seperated by ',': ")
arr = arr.split(",")
disParse(arr[0],arr[1])
