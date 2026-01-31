class Robot:
    def _init_(self):
        self.robotName = ""
        self.rowNumber = 0
        self.columnNumber = 0
        self.direction = ""

    def getRobotName(self):
        return self.robotName

    def setRobotName(self, n):
        self.robotName = n

    def getRowNumber(self):
        return self.rowNumber

    def setRowNumber(self, v):
        self.rowNumber = v

    def getColumnNumber(self):
        return self.columnNumber

    def setColumnNumber(self, v):
        self.columnNumber = v

    def getDirection(self):
        return self.direction

    def setDirection(self, d):
        self.direction = d

    def setRobot(self, nm, cx, cy, dr):
        self.robotName = nm
        self.rowNumber = cx
        self.columnNumber = cy
        self.direction = dr

    def canStep(self, front):
        if front == "up":
            return self.rowNumber > 0
        elif front == "down":
            return self.rowNumber < 9  # Assuming maximum row number is 9
        elif front == "left":
            return self.columnNumber > 0
        elif front == "right":
            return self.columnNumber < 9  # Assuming maximum column number is 9

    def takeStep(self):
        if self.direction == "up":
            self.rowNumber -= 1
        elif self.direction == "down":
            self.rowNumber += 1
        elif self.direction == "left":
            self.columnNumber -= 1
        elif self.direction == "right":
            self.columnNumber += 1

    def turnLeft(self):
        if self.direction == "up":
            self.direction = "left"
        elif self.direction == "down":
            self.direction = "right"
        elif self.direction == "left":
            self.direction = "down"
        elif self.direction == "right":
            self.direction = "up"

    def turnRight(self):
        if self.direction == "up":
            self.direction = "right"
        elif self.direction == "down":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "up"
        elif self.direction == "right":
            self.direction = "down"

    def turnBackward(self):
        if self.direction == "up":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "up"
        elif self.direction == "left":
            self.direction = "right"
        elif self.direction == "right":
            self.direction = "left"

    def show(self):
        return f"Robot Name: {self.robotName}, Row: {self.rowNumber}, Column: {self.columnNumber}, Direction: {self.direction}"

# Example usage:
robot1 = Robot()
robot1.setRobot("Robot1", 0, 0, "right")
print(robot1.show())
robot1.turnLeft()
robot1.takeStep()
print(robot1.show())