class LogNode:
   def __init__(self, order_id):
      self.order_id = order_id
      prev = None
      print(f"{self.order_id} created")

   def __del__(self):
      print(f"{self.order_id} deleted")

class Log:
   maxNodes = 20
   
   def __init__(self):
      self.root = None
      self.nodeCount = 0

   def record(self, order_id):
      tmp = LogNode(order_id)

      tmp.prev = self.root
      self.root = tmp

      self.nodeCount += 1

      if self.nodeCount > Log.maxNodes:
         tail = self.root
         
         for _ in range(Log.maxNodes-1):
            tail = tail.prev
            
         tail.prev = None
         
         self.nodeCount -= 1

   def get_last(self, i):
      if self.nodeCount == 0 or i <= 0 or i > self.nodeCount:
         return None

      tmp = self.root

      for _ in range(i-1):
         tmp = tmp.prev

      return tmp.order_id

L = Log()

x = -1
while not x == 0:
   print("1: Record")
   print("2: Get last")
   print("0: Exit\n")
   x = input("Do what: ")
   if x == "":
      print("\n\n")
      continue
   x = int(x)
   
   if x == 1:
      L.record(int(input(" ID: ")))
   elif x == 2:
      print(L.get_last(int(input(" i: "))))
   print()









