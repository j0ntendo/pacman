# Import our own constants:
from globals import FOODMAX, STEPMAX, WIDTH, HEIGHT, X_MAX, Y_MAX, MS_TO_QUIT
from globals import FOOD as food, GHOSTS as ghosts

# Import our own doboggi_man class:
from characters import doboggi_man

import turtle


class auto_doboggi_man(doboggi_man):

    """
    Class auto_doboggi_man, the autonomous doboggi-collector.

    The auto_doboggi_man class is a subclass of the doboggi_man class. It
    inherits all data attributes and methods from the doboggi_man class. It
    overrides the move() method of the doboggi_man class to automatically
    navigate doboggi_man across the screen.

    Attributes:
        stage (int): Represents the current stage of movement
    """

    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.stage = 0
        
    def move(self):
        """
        Move the character to the next position.
        """
        # set _x and _y for convenience
        _x = self.ttl.xcor()
        _y = self.ttl.ycor()
        walkDistance = 10

        # three stages:
        # 1. go to the nearest doboggi at the lower half of the screen (y > 0)
        # 2. go to towards the center so that x = 0, then move up
        #     a. if there is a ghost, do not move. Set walkDistance to 0
        #     b. if there is no ghost, move up
        # 3. go to the nearest doboggi at the upper half of the screen (y < 0)

        # stage 1
        if self.stage == 0:
            foodUnderZero = []  # Initialize an empty list 
            for i in range(len(food)):  # Iterate over the food list
                if food[i].getPosition()[1] < 0:  # Chck if the ycord is lt 0
                    foodUnderZero.append(food[i])  # Add the item to the list
            if len(foodUnderZero) == 0:  # Chck if no items below the y-axis
                self.stage = 1  # Change the stage to Stage 2
            else:
                nearestFood = foodUnderZero[0]  # first item as nearest food
                # Chck if the xcord diff is gt 10
                if abs(nearestFood.getPosition()[0] - _x) > 10:  
                    # Chck if the nearest food is to the right
                    if nearestFood.getPosition()[0] > _x:  
                        self.turnEast()  # Turn the character to the east
                    else:
                        self.turnWest()  # Turn the character to the west
                # Chck if the ycord difference is gt 10
                elif abs(nearestFood.getPosition()[1] - _y) > 10:  
                    # Chck if the nearest food is above the crent 
                    if nearestFood.getPosition()[1] > _y:  
                        self.turnNorth()  # Turn the character to the north
                    else:
                        self.turnSouth()  # Turn the character to the south 

        # stage 2
        elif self.stage == 1:
            if abs(_x) < 20 and _y < -60:  # Near center and below -60
                self.turnNorth()  # Turn character up
            elif _x > 0:  # Character is right of center
                self.turnWest()  # Turn character left
            elif _x < 0:  # Character is left of center
                self.turnEast()  # Turn character right
            if abs(_x) < 10 and _y >= -60:  # chck to move stage
                self.stage = 2  # Change to Stage 2a

        # stage 2a
        elif self.stage == 2:
            self.turnNorth()  # Turn the character to the north (up)
            ghostIndex = -1  # Initialize ghostIndex variable
            # Compare ycords
            if ghosts[0].getPosition()[1] < ghosts[1].getPosition()[1]:  
                ghostIndex = 1  # Set index to 1 if the second is lower
            else:
                ghostIndex = 0  # Set index to 0 if the first is lower
            walkDistance = 0  # (stop character from moving)
            # Chck if the ghost is on left
            if ghosts[ghostIndex].getPosition()[0] < 0: 
                if ghosts[ghostIndex].getPosition()[0] - X_MAX < 20: 
                    self.stage = 3  # Change to Stage 3

        # stage 3
        elif self.stage == 3:
            self.turnNorth()  # Turn the character to the north (up)
            # Compare y-coordinates of ghosts
            if ghosts[0].getPosition()[1] < ghosts[1].getPosition()[1]: 
                # Set ghostIndex to 1 if the second ghost is lower 
                ghostIndex = 1  
            else:
                # Set ghostIndex to 0 if the first ghost is lower
                ghostIndex = 0  
            # Check if ghost is more than 20 units above the character
            if ghosts[ghostIndex].getPosition()[1] + 20 < _y:  
                self.stage = 4  # Change to Stage4

        # stage 4
        elif self.stage == 4:
            foodOverZero = []  # Food items above y-axis
            for i in range(len(food)):  # Iterate over food list
                if food[i].getPosition()[1] > 0:  # Food item above y-axis
                    # Add food item to foodOverZero list
                    foodOverZero.append(food[i])  
            if len(foodOverZero) == 0:  # No food items above y-axis
                self.stage = 5  # Change to Stage 5
            else:
                nearestFood = foodOverZero[0]  # Nearst item above y
                # Check xcord diff
                if abs(nearestFood.getPosition()[0] - _x) > 10:  
                    # Nearest food is right of current 
                    if nearestFood.getPosition()[0] > _x:  
                        self.turnEast()  # Turn right
                    else:
                        self.turnWest()  # Turn left
                # Check cord diff
                elif abs(nearestFood.getPosition()[1] - _y) > 10:  
                    # Nearest food is above current
                    if nearestFood.getPosition()[1] > _y:  
                        self.turnNorth()  # Turn up
                    else:
                        self.turnSouth()  # Turn down
        self.ttl.forward(walkDistance)