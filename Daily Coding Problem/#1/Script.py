def add_upto(numlist, num):
	tried = []
	for totry in numlist:
		if num - totry in numlist:
			return True
	return False

nums = []
inp = 1

print("Enter non-zero integers (0 to finish):")

while inp != 0:
   inp = int(input())
   
   if inp != 0:
      nums.append(inp) 

key = int(input("Enter number to search: "))

result = add_upto(nums, key)

if result:
   print(f"Yes, there are at least two numbers that add up to {key}")
else:
   print(f"No, there are not any two numbers that add up to {key}")

input()
