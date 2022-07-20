
def sort(a):
    count =0
    for i in range(len(a)-1):
        swap = False
        count+=1
        for j in range(len(a)-1-i):
            if a[j]> a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap = True
        print(a)
        if not swap:
            break
    print(count)

sort([21,4,1,3,9,20,25,6,21,14])
sort([1,2,3,4,5,6])