import random

class Teenda:
  def __init__(self, numbers, size):
    self.numbers = numbers
    self.size = size

  def is_teenda(self):
    if self.size != 3 and self.size != 5:
      return False

    # Check order for size 3 and size 5 teendas (larger in the middle)
    return (self.numbers[0] > self.numbers[1] and 
            (self.size == 3 or self.numbers[1] > self.numbers[2] and self.numbers[2] > self.numbers[3] and self.numbers[3] > self.numbers[4]))

  def get_average(self, a, b):
    return (a + b) // 2

  def mutate(self):
    # Simulate random event (grow or split)
    if random.random() < 0.5:  # 50% chance of mutation
      if self.size == 3:
        # Grow (increase to size 5)
        avg1 = self.get_average(self.numbers[0], self.numbers[1])
        avg2 = self.get_average(self.numbers[1], self.numbers[2])

        # Check if new sequence is a valid teenda
        if self.numbers[0] > avg1 and avg1 > avg2 and avg2 > self.numbers[2]:
          self.numbers.insert(2, avg1)
          self.numbers.insert(4, avg2)
          self.size = 5
          print("Teenda grew to: ", end="")
        else:
          print("Growth failed. Teenda remains: ", end="")
      else:
        # Split (decrease to size 3)
          split_value = self.numbers[2] // 2

          # Check if new sequences are valid teendas
          if self.numbers[0] > split_value and split_value > self.numbers[1]:
            new_teenda1 = Teenda(self.numbers[:3], 3)
            new_teenda1.numbers[2] = split_value

            new_teenda2 = Teenda(self.numbers[3:], 2)
            new_teenda2.numbers[0] = split_value

            # Valid split, display mutated teendas
            print("Teenda split into: ")
            new_teenda1.display()
            new_teenda2.display()
          else:
            print("Split failed. Teenda remains: ", end="")

    # Display teenda after mutation attempt
    self.display()

  def display(self):
    print(self.numbers)

# Create some teenda objects
teenda1 = Teenda([4, 5, 2], 3)
teenda2 = Teenda([30, 200, 29], 3)
teenda3 = Teenda([23, 35, 40, 30, 20], 5)  # Invalid (not a teenda) - for testing

# Loop for mutations (example for 2 iterations)
for _ in range(2):
  teenda1.mutate()
  teenda2.mutate()
  teenda3.mutate()