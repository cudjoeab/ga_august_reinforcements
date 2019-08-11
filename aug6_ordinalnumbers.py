# Write a function that accepts a number as an argument and returns a string containing 
# that number along with its "ordinal indicator". 
# E.g. passing in 1 would return "1st", 2 would return "2nd", 3 would return "3rd", 4 would return "4th", etc.

# Make sure your function works for every number between 1 and 20. 
# If you're feeling ambitious, see if you can get it working for numbers beyond that

def ordinal_number(num):
    num_string = str(num)
    if num > 9:
        if int(num_string[-2:]) >= 10 and int(num_string[-2:]) <= 20:
            return(num_string + 'th')
        else:
            if num_string[-1] == '1':
                return(num_string + 'st')
            elif num_string[-1] == '2':
                return(num_string + 'nd')
            elif num_string[-1] == '3':
                return(num_string + 'rd')
            else:
                return(num_string + 'th')

print(ordinal_number(21))
print(ordinal_number(199))
print(ordinal_number(3))
print(ordinal_number(2))
print(ordinal_number(1))

        

