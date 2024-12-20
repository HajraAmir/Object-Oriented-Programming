import random

class Teenda:
    def __init__(self, data, size):
        self.data = data
        self.size = size

    def is_teenda(self):
        if self.size not in (3, 5):
            return False

        if self.size == 3:
            return self.data[0] > self.data[1] and self.data[1] > self.data[2]
        else:
            return (self.data[0] > self.data[1] and
                    self.data[1] > self.data[2] and
                    self.data[2] > self.data[3] and
                    self.data[3] > self.data[4])

    def get_avg(self, a, b):
        return (a + b) // 2

    def mutate(self):
        # Simulate random event (grow or split)
        if random.random() < 0.5:  # Use random.random() for 0 to 1 probability
            if self.size == 3:
                # Grow (increase to size 5)
                avg1 = self.get_avg(self.data[0], self.data[1])
                avg2 = self.get_avg(self.data[1], self.data[2])

                # Check if new sequence is valid teenda
                if self.data[0] > avg1 and avg1 > avg2 and avg2 > self.data[2]:
                    self.data.insert(2, avg1)
                    self.data.insert(4, avg2)
                    self.size = 5
                    print("Teenda grew to: ", end="")
                else:
                    print("Growth failed. Teenda remains: ", end="")
            else:
                # Split (decrease to size 3)
                split_val = self.data[2] // 2

                # Check if new sequences are valid teendas
                if self.data[0] > split_val and split_val > self.data[1]:
                    teenda1 = Teenda(self.data[:3], 3)
                    teenda1.data[2] = split_val

                    teenda2 = Teenda(self.data[3:], 2)
                    teenda2.data[0] = split_val

                    # Valid split, display mutated teendas
                    print("Teenda split into: ")
                    teenda1.display()
                    teenda2.display()
                else:
                    print("Split failed. Teenda remains: ", end="")

        self.display()  # Display teenda after mutation attempt

    def display(self):
        print(self.data)

# Create some teenda objects
teenda1 = Teenda([4, 5, 2], 3)
teenda2 = Teenda([30, 200, 29], 3)
teenda3 = Teenda([23, 35, 40, 30, 20], 5)  # Invalid (not a teenda) - for testing

# Loop for mutations (example for 2 iterations)
for _ in range(2):
    teenda1.mutate()
    teenda2.mutate()
    teenda3.mutate()