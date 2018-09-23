import itertools


class Vector:
    def __init__(self, coords):
        self.x, self.y = coords

    def __add__(self, other):
        x = self.x + other.x
        y = self.y - other.y
        return Vector((x, y))

    def __str__(self):
        return 'vector=(%s, %s)' % (self.x, self.y)


v1 = Vector((10, 20))
v2 = Vector((5, 7))

v3 = v1 + v2

print(v3)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

for element in itertools.chain(list1, list2):
    print(element)
