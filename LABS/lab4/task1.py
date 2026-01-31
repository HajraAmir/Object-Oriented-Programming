import random

class Batsman:
    def _init_(self, matches=None):
        if matches is None:
            self.matches = random.randint(1, 95)
        else:
            self.matches = matches
        self.scores = [random.randint(0, 180) for _ in range(self.matches)]
    
    def calcTotal(self):
        return sum(self.scores)
    
    def calcAverage(self):
        return sum(self.scores) / len(self.scores)
    
    def findMaxScore(self):
        return max(self.scores)
    
    def show(self):
        print("No of Matches:", self.matches)
        print("Scores:", " ".join(map(str, self.scores)))
        print("Total Score:", self.calcTotal())

# Example usage:
batsman1 = Batsman()
batsman1.show()