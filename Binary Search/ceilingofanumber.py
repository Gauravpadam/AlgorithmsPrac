arr = [2,3,5,9,14,16,18]
target = 15

#  ceiling = smallest number in arr >= target
# Answer supposed to be 14

s = 0
e = len(arr) - 1
foundflag = 0 # Necessary when using print

while (s<=e):
    mid = s + (e-s)//2
    if target == arr[mid]:
        print (arr[mid]) # return arr[mid]
        foundflag = 1
        break # Necessary for this case, as return is missing
    elif target<arr[mid]:
        e=mid-1
    else:
        s=mid+1

if foundflag==0: # Only necesary when using print
    print (arr[s]) #return arr[s]

#Logic of this:
#Kunal's Binary Search questions video timestamp 25:00~40:00
    