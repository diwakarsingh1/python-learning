# parameter
# string.format(value 1, value 2)

txt = "My salary is {salary:.2f} per month"
x = txt.format(salary = 1000)
print(x)


txt1 = "My name is {name} and I am {age} years old.".format(name = "Diwakar Singh" , age = 24)
txt2 = "My name is {0} and I am {1} years old.".format("Diwakar Singh" , 24)
txt3 = "My name is {} and I am {} years old.".format("Diwakar Singh" , 24)

print(txt1)
print(txt2)
print(txt3)