x = "awesome" #global variable

def myfunc():
  print("Python is " + x)

myfunc()


x = "awesome"
def myfunc():
  x = "fantastic" # local variable
  print("Python is " + x)
myfunc()
print("Python is " + x)


def func():
  global x
  x = "global inside local"
func()
print(x)




x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)