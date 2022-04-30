def flatten(it):
        from collections.abc import Iterable
        
        new_list = []
        for a in it:
                if isinstance(a, Iterable):
                        new_list += flatten(a)
                else:
                        new_list.append(a)
        return new_list

def range_handler(*args):
   from itertools import product
   if len(args) == 2:
      flat = flatten(product(*args))
   else:
      last = args[0]
      for i in range(len(args)-1):
         last = product(last, args[i+1])
      flat = flatten(last)

   for i in range(0, len(flat), len(args)):
      yield tuple(flat[i: i+len(args)])

def stairs(N, steps):
   if isinstance(steps, int):
      return N % steps == 0

   elif isinstance(steps, list):
      factors = []
      i = []
      for x in steps:
         factors.append(N//x)
         i.append(0)
      
      from itertools import product

      count = [steps]
      for i in range_handler(*[range(0,N+1,js) for js in steps]):
         if sum(i) == N:
            count.append([a//s for a, s in zip(i, steps)])
            
      return count

def perm(count):
   states = 0

   from math import factorial
   from functools import reduce
   for c in count[1:]:
      states += (factorial(sum(c))/reduce(lambda x, y: x*y, [factorial(i) for i in c]))

   return int(states)

print(perm(stairs(int(input("Stair step-count: ")),[int(input(f"Step size {i+1}: ")) for i in range(int(input("How many step sizes:")))])))
