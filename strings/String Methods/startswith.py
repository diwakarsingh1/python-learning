# parameter
# string.startswith(value, start, end)

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

txt = "Hello, welcome to my world."

x = txt.startswith("wel", 7, 20)

print(x)


txt = "Hi, welcome to my world."

x = txt.startswith(("Hello", "Hi"))

print(x)