class Stack:
  def __init__(self):
    self.items = []
  def push(self, item):
    self.items.append(item)
  def pop(self):
    return self.items.pop()
  def peek(self):
    return self.items[-1]
  def size(self):
    return len(self.items)
  def __iter__(self):
    return self
  def __next__(self):
    if self.items:
      return self.items.pop()
    else:
      raise StopIteration
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())
for item in stack:
  print(item)
