num1 = "456"
num2 = "77"

# Check to see which is longer 

power = 0 
remainder = 0 
for n, digit_char in enumerate(num2): # The shorter string 
    d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}  
    i = n 

    # Add the two digits 
    num2 = str(d[digit_char] + d[num1[n]])[0] 
    if len(num2) > 1:
        remainder = num2[1] 

# Add the last remainder to the next 
num1[n]