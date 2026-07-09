from itertools import combinations
list = [-2,5,-4,-7,8,1]
print("Positive combination")
for r in range(1,len(list)+1):
    for combo in combinations(list,r):
        if all(x>0 for x in combo):
            print(combo)