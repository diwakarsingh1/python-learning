print("Hello")
print('Hello')

#Quotes inside the quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assgin value to a variable as a string
a = "Hello"
print(a)

#Multiline string
a = """Lorem ipsum dolor sit amet,consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[12])

for x in "banana":
  print(x)

#length of a string

x = "Diwakar"
print(len(x))


txt = "The best things in life are free!"
print("diwakar" not in txt)
if "free" not in txt:
    print("Yes, 'free' is present.")
else:
    print("No, its present")