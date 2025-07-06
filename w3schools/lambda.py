def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc1(m):
  def func3(k):
    return m*k
  return func3(2)

print(myfunc1(11))