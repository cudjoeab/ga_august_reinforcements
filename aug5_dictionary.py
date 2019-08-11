# Write code to generate a dictionary where the keys are the numbers from 1 to 50 and the values follow these rules:

# if the number is divisible by 2 the value should be one more than the key
# if the number is divisible by 7 the value should be one less than the key
# if the number is divisible by 2 and 7 the value should be the key multiplied by 2
# otherwise the value should be the same number as the key

def print_dict():
    dict_entry = {} 
    for num in range(1, 51):
        if num % 2 == 0 and num % 7 == 0:
            dict_entry[num] = num*2
        elif num % 2 == 0:
            dict_entry[num] = num + 1
        elif num % 7 == 0:
            dict_entry[num] = num - 1
        else:
            dict_entry[num] = num
    return dict_entry

print(print_dict())


