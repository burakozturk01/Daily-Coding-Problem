def inCircle(r, center, coords):
   return (coords[0] - center[0])**2 + (coords[1] - center[1])**2 <= r**2

def find_pi(err_pow): # Error < 10^(-err_pow)
   import math as m
   import random as rnd

   sq_len = 100
   r = sq_len / 2

   points = 0
   countCirc = 0
   
   pi = 0

   while abs(pi - m.pi) > 10**(-err_pow):
      points += err_pow * 20
      
      for _ in range(err_pow * 20):
         if inCircle(r, (r,r), (rnd.random()*sq_len, rnd.random()*sq_len)):
            countCirc += 1

      pi = (countCirc/points) * 4

   return pi, points

print(find_pi(6))
