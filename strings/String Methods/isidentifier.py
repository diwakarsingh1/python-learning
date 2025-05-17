'''
 A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_).
 A valid identifier cannot start with a number, or contain any spaces.
'''

txt = "Dem_1o"

x = txt.isidentifier()

print(x)




a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())