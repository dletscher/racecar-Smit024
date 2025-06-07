
import random

class Agent:
    def chooseAction(self, observations, possibleActions):
        #for lidar and speed info
        lidar = observations['lidar']  
        velocity = observations['velocity']

        #inf is for bigger number 
        lidar = [d if d != float('inf') else 100 for d in lidar]
        farLeft, left, center, right, farRight = lidar

        #for driving car in center 
        leftSide = farLeft + left
        rightSide = farRight + right

        #for sharp turn 
        if min(lidar) < 0.05:
            if ('straight', 'brake') in possibleActions:
                return ('straight', 'brake')
            return random.choice(possibleActions)

        #decide left and right turn
        if rightSide + 0.2 < leftSide:
            move = 'left'
        elif leftSide + 0.2 < rightSide:
            move = 'right'
        else:
            move = 'straight'

        #narrow path
        if center < 0.6 or left < 0.5 or right < 0.5:
            if (move, 'brake') in possibleActions:
                return (move, 'brake')

        if velocity > 0.19:
            if (move, 'brake') in possibleActions:
                return (move, 'brake')
            elif (move, 'coast') in possibleActions:
                return (move, 'coast')

        #speedign on straight road
        if velocity <= 0.3 and center > 0.8 and left > 0.8 and right > 0.8:
            if (move, 'accelerate') in possibleActions:
                return (move, 'accelerate')

        #just coast (means no accelerate or brake)
        if (move, 'coast') in possibleActions:
            return (move, 'coast')

        #last backup
        return random.choice(possibleActions)

    def load(self, data=None):
        pass
