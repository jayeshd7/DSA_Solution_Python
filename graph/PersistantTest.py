

l1 = [1,2,4,5,6,7]

count = 0


ans = []
result = []

for i in range(1, len(l1)):

    if l1[i] == (l1[i-1] +1):
        if l1[i-1] not in ans:
            ans.append(l1[i-1])
        ans.append(l1[i])


    if len(ans)> len(result) :
        result.extend(ans)


    else:
        ans.clear()
        result.clear()




    print(ans)






