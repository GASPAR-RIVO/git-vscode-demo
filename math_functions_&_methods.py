# num1 = input("Enter a number ")
# float_num1 =float(num1)
# float_rund_num1 = round(float_num1, 2)

# print(F"{num1} rounded to 2 decimal places is {float_rund_num1}")






# num1 = input("Enter a number ")
# float_num1 =float(num1)
# abs_rund_num1 = abs(float_num1)

# print(F"The abolute value of {num1} is {abs_rund_num1}")



num1 = input("Enter a number ")
float_num1 =float(num1)
num2 = input("Enter antoher number ")
float_num2 =float(num2)

difference = float_num1 - float_num2
true_difference = difference.is_integer()

print(F"The differnce between{num1} and {num2} ia an integer ? {true_difference}")