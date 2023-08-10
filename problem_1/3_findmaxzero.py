def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*factorial(num-1)
def getzeroFFac(num):
    facnum = factorial(num) # edit with recursive
    max_count = []
    temp_ct = 0
    resetFlag = False
    print(facnum)
    while(facnum!=0):
        if(facnum % 10 ==0):
            resetFlag = False
            temp_ct += 1
        else :
            resetFlag = True
        facnum = round(facnum / 10)
        if(resetFlag==True):
            max_count.append(temp_ct)
            temp_ct = 0
    return max(max_count)
s1 = 10
s2 = 5
print(getzeroFFac(s1))