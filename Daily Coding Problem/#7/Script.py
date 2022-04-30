# Returns a list of every substring of the string (unused)
def splitter_(string):
   sparts = {string}
   length = len(string)

   if len(string) == 0:
      return None
   if len(string) == 1:
      return sparts

   for i in range(1, length):
      tpart = string[0:i]
      sparts.add(tpart)
         
      tparts = splitter(string[i:])
      for part in tparts:
         sparts.add(part)
      
   parts = list(sparts)
   parts.sort()
   return parts

# Generates every possible splitted form of the string as lists
def splitgenerator(string):
    for i in range(1, len(string)):
        start = string[0:i]
        end = string[i:]
        yield (start, end)
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield result

# To make a list from splitgenerator (unused)
def splitter(string):
   tmp = list(splitgenerator(string))

   return tmp

# Checks every splitted form and generates valid decoded strings
def decode(encoded):
   alph = ".abcdefghijklmnopqrstuvwxyz"

   decodes = []
   
   if len(encoded) == 0:
      return decodes

   for splitted in splitgenerator(encoded):
      decode = ""
      for part in splitted:
         if 0 < int(part) < 27 and part[0] != "0":
            decode += alph[int(part)]
         else:
            decode = None
            break

      if decode == None:
         continue
      else:
         yield decode

def encode(string):
   length = len(string)

   if length == 0:
      return ""
   
   alph = "abcdefghijklmnopqrstuvwxyz"
   string = string.lower()
   encoded = ""

   for char in string:
      if not char in alph:
         return "Only alphabet"
      encoded += str(ord(char) - ord("a") + 1)

   return encoded

while 1:       
   if input("1: Encode / Anything: Decode\n") == "1":
      inp = input("Message to encode: ")
      print("Encoded message:")
      print(encode(inp))
      
   else: 
      inp = input("Message to decode: ")
      print("Possible decodes:")
      for i in decode(inp): print(i)
