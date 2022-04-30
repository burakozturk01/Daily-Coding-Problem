def dist_chars(substr):
   chars = []
   count = 0
   for c in substr:
      if not c in chars:
         chars.append(c)
   return chars

def long_sub(substrs):
   if len(substrs) == 0:
      return -1

   longest = substrs[0]
   longests = []

   if len(substrs) == 1:
      return longest

   for sub in substrs[1:]:
      if len(sub) > len(longest):
         longest = sub

   longlen = len(longest)

   for sub in substrs:
      if len(sub) == longlen:
         longests.append(sub)

   if len(longests) == 1:
      return longest

   return longests

def maxsub(string, maxchars):

   if maxchars < 1 or string == "":
      return ""

   ind0 = 0
   ind1 = 1
   indmax = len(string) - 1

   maxlen = 1
   
   chars = dist_chars(string[ind0:ind1])
   print("Org chars: ", chars)

   substrs = []
   tobreak = 0

   while not tobreak:
      print("indexes: ", ind0, ind1)

      ind1 += 1
      if ind1 == indmax +1:
         tobreak = 1
      
      chars = dist_chars(string[ind0:ind1])
      print("Chars: ", chars)

      if len(chars) > maxchars:
         print("chars > max")
         ind0 += 1
         print("Popped: ", chars.pop(chars.index(string[ind0-1])))
      elif len(chars) < maxchars:
         print("chars < max")
         maxlen += 1
      else:
         print("chars = max")
         maxlen += 1
         substr = string[ind0:ind1]
         print("Substring: ", substr)
         if len(substrs) == 0 or len(substr) >= len(substrs[-1]):
            print(4)
            substrs.append(substr)
            
   print("Substrings: ", substrs)
   return long_sub(substrs)

print(maxsub("abcba", 2))
