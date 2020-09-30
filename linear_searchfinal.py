def linsearch(arr,ele):
    if ele in arr:
        return arr.index(ele)
    else:
        return -1
arr=[10,20,30,40,50,60,70,80,90]

result=linsearch(arr,80)
if result == -1:
	print("Element not found!")
else:
	print("Element at position:"+str(result))
