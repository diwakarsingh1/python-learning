# parameter
# string.find("substring", start, end)

txt = "What is your name?"
x = txt.find("is", 7, 16)
print(x)

x = txt.find("is")
print(x)

# Print -1 if sub: str not found