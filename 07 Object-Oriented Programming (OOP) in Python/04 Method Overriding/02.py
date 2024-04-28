class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # Overload the + operator for vector addition
  def __add__(self, other):
    if isinstance(other, Vector):
      return Vector(self.x + other.x, self.y + other.y)
    else:
      raise TypeError("Can only add Vector objects")

# Create two vector objects
v1 = Vector(3, 5)
v2 = Vector(2, 1)

# Add the vectors using the + operator
v3 = v1 + v2

print(f"Resultant vector: ({v3.x}, {v3.y})")
