ideal_output = 'nopqrstuvwxyzABCDEFGHIJKLM9012345678' 


def rotateCipher(inputString, rotationFactor):
    alphabet = 'abcdefghijklmnopqrstuvwxyz' 
    integers = '0123456789' 

    output = ''

    # Divide the size of the lookup table by the shift number, and get the remainder 
    alphabet_shift = rotationFactor % len(alphabet) 
    integer_shift = rotationFactor % len(integers)    

    for char in inputString:
        if char.isdecimal():
            # Digits are a bit easier
            # Get the number, add the rotation factor, and divide by the length of the lookup. T
            # Then use [-1] to verify we are getting the last number in the case of an overrun  
            c = str(int(char) + rotationFactor % len(integers) )[-1]
            output = output + c
            
        elif char.isalpha():
            # Current character index + shifted amount, then modulo to make sure we don't overrun 
            code_index = (alphabet.index(char.lower()) + alphabet_shift) % len(alphabet)
            c = alphabet[ code_index  ]

            if char.isupper():
                output = output + c.upper() 
            else:
                output = output + c

        # Pass if not one of the categories 
        else:
            output+=char

        return output 

inputString = 'abcdefghijklmNOPQRSTUVWXYZ0123456789' 
rotationFactor = 39

output = rotateCipher(inputString, rotationFactor)

print(output)
assert output == ideal_output