def add_upto(numlist):
   newlist = []
   for _ in range(len(numlist)):
      popped = numlist.pop(0)
      #print(numlist)

      mult = 1

      for num in numlist:
         mult *= num
      newlist.append(mult)

      numlist.append(popped)
      #print(numlist,end="\n\n")

   return newlist

nums = []

print("Enter integers (Enter to finish):")

while 1:
   inp = input()

   if inp == "":
      break
   
   else:
      nums.append(int(inp)) 

result = add_upto(nums)

print(result)

input()
