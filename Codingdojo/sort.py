

inp =  [4,5,6,7,2,3,11,13]
sorted_l = sorted(inp)
print("Rev sorted",sorted_l)
even_l = []
odd_l = []
for i in range(len(sorted_l)):
    if sorted_l[i] %2 == 0:
        even_l.append(sorted_l[i])

    else:
        odd_l.append(sorted_l[i])
final_l = even_l + odd_l
print(final_l)

w1 = 'geeks'
w2 = 'practice'





