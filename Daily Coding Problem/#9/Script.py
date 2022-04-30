import random as r

def find_max_sum(arr):
   exc = 0
   inc = arr[0]

   for i in arr[1:]:
      tmp = inc
      inc = exc + i
      exc = max(tmp,exc)

   return max(exc,inc)

while 1:
   a = [r.randrange(-5,10) for _ in range(5)]
   print(a)
   print(find_max_sum(a))
   input()

# Çözemedim çildiricam
