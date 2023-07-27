# Initialize a random list of unique values 

arr = [3, 4, 1, 6, 2] 
output = []

start = 0
end = len(arr)-1
for i, value in enumerate(arr):
    # Move in one direction, then the other 
    # Check for 
    #   start of list, and 
    #   end of list 
    #   value < starting_value arr[i] 

    # Check direction 1 
    c = i
    left_subarray = []
    while c >= start and arr[c] <= arr[i]:
        left_subarray.append( arr[c] ) 
        c-=1

    # Check direction 2 
    c = i
    right_subarray = []
    while c <= end and arr[c] <= arr[i]:
        right_subarray.append( arr[c] )  
        c+=1

    print('left sub: ',left_subarray)
    print('right sub: ',right_subarray)
    print(' ')
    output.append( len(left_subarray) + len(right_subarray) -1 )
    
print("output: ",output)