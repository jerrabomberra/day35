class Person:
  def __init__(self, name, age, weight)-> None:
    self.name = name
    self.age = age
    self.weight = weight


p1 = Person("John", 36, 72)

print(p1.name)
print(p1.age)
print(p1.weight)