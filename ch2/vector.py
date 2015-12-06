class Vector:
  "Represents a vector in a multidimensional space"

  def __init__(self, d):
    """creates a d-dimensional vector of zeros."""
    self._coords = [0] * d

  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)

  def __getitem__(self, j):
    """Return jth coordinate of vector."""
    return self._coords[j]

  def __setitem__(self, j, val):
    """Set jth coordinate of vector to given value."""
    self._coords[j] = val

  def __add__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other): # relies on len method
      raise ValueError("dimensions must agree")
    result = Vector(len(self)) # start with vector of zeros
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result

  def __radd__(self, other):
    """Add a sequence to the vector."""
    self.__add__(self, other)

  def __sub__(self, other):
    """Return the difference of two vectors."""
    if len(self) != len(other):
      raise ValueError("dimensions must agree")
    result = Vector(len(self))
    for j in range(len(self)):
      result[j] = self[j] - other[j]
    return result

  def __neg__(self):
    """Return a negated vector instance."""
    result = Vector(len(self))
    for i in range(len(self)):
      result[i] = -1 * self[i]
    return result

  def __mul__(self, factor):
    """Return the product of a vector and a scalar."""
    result = Vector(len(self))
    for i in range(len(self)):
      result[i] = factor * self[i]
    return result    

  def __eq__(self, other):
    """Return True if vector has same coordinates as other."""
    return self._coords == other._coords

  def __ne__(self, other):
    """Return True if vector differs from other."""
    return not self == other # rely on existing eq definition

  def __str__(self):
    """Produce string representation of vector."""
    return '<' + str(self._coords)[1:-1] + '>' # adapt list representation
