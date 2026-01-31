import random

class Batsman:
    def _init_(self, matches=None):
        if matches is None:
            self.matches = random.randint(1, 95)
        else:
            self.matches = matches
        self.scores = self.randomScores(self.matches)
    
    def randomScores(self, num_matches):
        scores = []
        for _ in range(num_matches):
            # Generating random scores between 0 and 180,
            # but some values may be up to 350 or seldomly up to 500
            score = random.randint(0, 180)
            if random.random() < 0.1:  # 10% chance for higher scores
                score = random.randint(181, 350)
            elif random.random() < 0.01:  # 1% chance for very high scores
                score = random.randint(351, 500)
            scores.append(score)
        return scores
    
    def calcTotal(self):
        return sum(self.scores)
    
    def calcAverage(self):
        return sum(self.scores) / len(self.scores)
    
    def findMaxScore(self):
        return max(self.scores)
    
    def count50s(self):
        return sum(1 for score in self.scores if score >= 50 and score < 100)
    
    def count100s(self):
        return sum(1 for score in self.scores if score >= 100)
    
    def show(self):
        print("No of Matches:", self.matches)
        print("Scores:", " ".join(map(str, self.scores)))
        print("Total Score:", self.calcTotal())
        print("Average Score:", self.calcAverage())
        print("Highest Score:", self.findMaxScore())
        print("Number of 50s:", self.count50s())
        print("Number of 100s:", self.count100s())

# Example usage:
batsman1 = Batsman()
batsman1.show()