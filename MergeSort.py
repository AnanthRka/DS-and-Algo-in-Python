
def sort(a):
    if len(a)>1:
        mid = len(a)//2
        left_array = a[:mid]
        right_array = a[mid:]

        sort(left_array)
        sort(right_array)

        i,j,k =0,0,0

        while i < len(left_array) and j <len(right_array):
            if left_array[i] <= right_array[j]:
                a[k] = left_array[i]
                i+=1
            else:
                a[k] = right_array[j]
                j+=1
            k+=1
        
        while i<len(left_array):
            a[k] = left_array[i]
            i+=1
            k+=1
        while j < len(right_array):
            a[k] = right_array[j]
            j+=1
            k+=1
    print(a)


sort([8,7,6,1,0,9,2])
print()
sort([21,4,1,3,9,20,25,6,21,14])
print()
sort([1,2,3,4,5,6])
print()
sort([21,4,1,3,9,20,25])
