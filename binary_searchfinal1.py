def b(arr,begin,last,ele):
    mid=int((begin+last)/2)
    if ele==arr[mid]:
        print("Element found at :"+str(mid))
        return
    elif ele<arr[mid]:
        b(arr,0,mid-1,ele)
    else:
        b(arr,mid,len(arr),ele)
arr=[20,55,35,64,78,96,34,25,76,45,94,12]
arr.sort()


ele=int(input("Enter the element :"))
b(arr,0,len(arr),ele)

















    
