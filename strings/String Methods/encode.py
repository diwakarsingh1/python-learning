# Parameter
# string.encode(encoding=encoding, errors=errors)

txt = "My name is Stale"

x = txt.encode()

print(x)


txt = "My name is Stale"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))