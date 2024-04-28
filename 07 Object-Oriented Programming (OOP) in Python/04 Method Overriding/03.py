class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __eq__(self, other):
    if isinstance(other, Point):
      return self.x == other.x and self.y == other.y
    else:
      return False

  def __lt__(self, other):
    if isinstance(other, Point):
      return self.y < other.y or (self.y == other.y and self.x < other.x)
    else:
      raise TypeError("Can only compare Point objects")

# Create points
p1 = Point(3, 5)
p2 = Point(3, 5)
p3 = Point(2, 1)

# Comparison examples
print(p1 == p2)  # True (same coordinates)
print(p1 < p3)  # False (p1 has higher y-coordinate)
print(p3 < p1)  # True (p3 has lower y-coordinate)
