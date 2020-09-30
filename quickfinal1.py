def q(arr,low,high):
    if low < high:
        pi=partition(arr,low,high)
        q(arr,low,pi-1)
        q(arr,pi,high)

def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range (low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        print("Passes"+str(j))
        print(arr)
        print("\n")
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1



arr=[12,234,56,76]
q(arr,0,len(arr)-1)
print(arr)
        
