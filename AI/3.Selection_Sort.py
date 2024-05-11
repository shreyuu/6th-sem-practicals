def selectionSort(arr):
    for i in range(len(arr)):
        min = float('-inf')
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j], arr[i]
    return arr
    
print(selectionSort([89,56,45,34,65,76]))

'''
# for user input array:

def main():
    

    arr=[]
    n=int(input("enter total number of values:"))
    for i in range(n):
        ele=int(input("enter the elements"))
        arr.append(ele)
    
    print(selectionSort(arr))
'''


'''
[34, 45, 56, 65, 76, 89]
'''