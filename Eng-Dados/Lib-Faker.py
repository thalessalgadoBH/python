from faker import Faker
fake = Faker('pt_BR')

for _ in range(10):
  print(fake.name())
  
numbers = set(fake.unique.random_int() for i in range(1000))
assert len(numbers) == 1000
print(numbers)