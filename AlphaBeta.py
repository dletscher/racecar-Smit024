import random

class Agent:
    def __init__(self):
        #epsilon greedy value
        self.epsilon = 0.05

    def chooseAction(self, observations, possibleActions):
        lidar = observations['lidar']
        velocity = observations['velocity']

        farLeft, left, center, right, farRight = lidar

        #for driving car in center 
        leftSide = farLeft + left
        rightSide = farRight + right

        def select_action():
            #for sharp turns
            if min(lidar) < 0.1:
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

            if (move, 'coast') in possibleActions:
                return (move, 'coast')

            return random.choice(possibleActions)

        #epsilon greedy methd
        if random.random() < self.epsilon:
            return random.choice(possibleActions)
        else:
            return select_action()

    def load(self, data=None):
        pass

