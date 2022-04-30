#Gather the array
array = []

i = 0
inp = input(f"Enter array element {i} (Any string to exit): ")

while inp.isnumeric():
   array.append(int(inp))
   i += 1
   inp = input(f"Enter array element {i} (Any string to exit): ")

#Ask index
ind = "-1"
while not ind.isnumeric() or not 0 < int(ind) < len(array):
   ind = input("Enter a valid index number: ")

#Find result
left = ind-1
right = ind+1
if ind == 0:
   while array[right] <= array[ind] and right < len(array):
      right += 1
   if right == len(array):
      print(None)
   else:
      print(array[right])
elif ind == len(array - 1):
   while array[left] <= array[ind] and left >= 0:
      left -= 1
   if left == 0:
      print(None)
   else:
      print(array[right])
      
