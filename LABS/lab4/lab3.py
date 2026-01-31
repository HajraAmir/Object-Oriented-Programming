class Timespan:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def __repr__(self):
        return f"Timespan({self.hours}, {self.minutes})"

    def __str__(self):
        return f"{self.hours} hours and {self.minutes} minutes"

    def show(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

    def add_hours(self, hrs):
        self.hours += hrs

    def add_minutes(self, mins):
        self.hours += mins // 60
        self.minutes += mins % 60
        if self.minutes >= 60:
            self.hours += 1
            self.minutes -= 60

    def isequal(self, other):
        return self.hours == other.hours and self.minutes == other.minutes

    def change(self, ts):
        return abs(self.minutes - ts.minutes) + abs((self.hours - ts.hours) * 60)

    def minutes(self):
        return self.hours * 60 + self.minutes

    def hours(self):
        return self.hours + self.minutes / 60


def main():
    t1 = Timespan(2, 30)
    t2 = Timespan(7, 45)

    print(t1)  
    print(t2)  

    t1.add_hours(2)
    print(t1)  

     
    print('Difference in minuites:',(t1.change(t2))) 

    print('Minutes',t1.minutes)  
    print('Hours',t1.hours)
main()    