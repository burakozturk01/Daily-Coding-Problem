class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
   if root == None:
      return ""
   elif isinstance(root, Node):
      if Node.left == None or Node.right == None:
         return f"[{serialize(root.val)}]"
      else:
         return f"[{serialize(root.val)},{serialize(root.left)},{serialize(root.right)}]"
   else:
      return str(root)

n = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(n))

def deserialize(serial):
   if "[" in serial:
      serial = serial[1:-1]

      items = serial.split(",")
      return Node(deserialize(items[0]),deserialize(items[1]),deserialize(items[2]))
   elif isinstance(serial, str):
      if serial == "":
         return None
      else:
         return serial

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(deserialize(serialize(node)).left.left.val == 'left.left')
