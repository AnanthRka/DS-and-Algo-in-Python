def sort(a):
    l = len(a)
    min = 0
    for i in range(l):
        min = i
        for j in range(i,l):
            if a[min] > a[j]:
                min = j
        a[i],a[min] = a[min],a[i]
        print(a)

sort([29, 10, 14, 37, 13])
# sort([34,28,8,37,18,43,43,22,44,1,47,20,9,2])
# sort([21,4,1,3,9,20,25,6,21,14])
# print()
# sort([1,2,3,4,5,6])
# print()
# sort([21,4,1,3,9,20,25])