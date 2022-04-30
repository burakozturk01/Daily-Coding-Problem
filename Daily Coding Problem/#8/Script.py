import random as r

class Node:
   layers = []
   def __init__(self, value, left=None, right=None, layer=1):
      self.left = left
      self.value = value
      self.right = right
      self.layer = layer
      self.repr = None

   def print(self):
      import pprint as pp

      if len(Node.layers) < self.layer:
         Node.layers.append([])
      Node.layers[self.layer-1].append(self.value)
      
      if self.left == None and self.right == None:
         if len(Node.layers) < self.layer+1:
            Node.layers.append([])
         Node.layers[self.layer].append(None)
         Node.layers[self.layer].append(None)
         return

      if self.left == None:
         if len(Node.layers) < self.layer+1:
            Node.layers.append([])
         Node.layers[self.layer].append(None)
         self.right.print()
         return

      if self.right == None:
         if len(Node.layers) < self.layer+1:
            Node.layers.append([])
         Node.layers[self.layer].append(None)
         self.left.print()
         return

      self.left.print()
      self.right.print()

      
      if self.layer == 1:
         self.repr = Node.layers

         [print(layer) for layer in Node.layers]

         # Birgün belki

         print(self.isValid())

   def isValid(self):
      repr = root.repr

      valid = True
      for i in range(len(repr) - 1):
         if not (len(repr[i]) - repr[i].count(None)) * 2 == len(repr[i + 1]):
            valid = not valid
            break
      return valid

def countUnival(node):
   if node.left == None or node.right == None:
      return 1
   if node.left.value == node.right.value:
      return 1 + countUnival(node.left) + countUnival(node.right)
   return countUnival(node.left) + countUnival(node.right)

def randNode(layer=1):
   sw = r.randrange(0, 4)
   if sw == 0:
      return Node(r.randrange(0,2), randNode(layer+1), randNode(layer+1), layer)
   elif sw == 1:
      return Node(r.randrange(0,2), randNode(layer+1), None, layer)
   elif sw == 2:
      return Node(r.randrange(0, 2), None, randNode(layer + 1), layer)
   elif sw == 3:
      return Node(r.randrange(0, 2), None, None, layer)

root = randNode()

root.print()

