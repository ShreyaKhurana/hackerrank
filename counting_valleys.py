'''

Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, , or a downhill,  step. Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

'''


# Complete the countingValleys function below.
def countingValleys(n, s):

    # We'll use a stack to keep track of how far we are from the sea level
    start = s[0]

    # Every time we come back to the sea level we'll have an empty stack
    stack = [s[0]]

    # Initialize counter
    numValleys = 0

    for letter in s[1:]:

        # If stack is empty, simply push
        if len(stack) == 0:
            start = letter
            stack.append(letter)

        # If stack has 'D' on top and we have 'U', then pop, else push
        elif letter == 'U':
            if stack[-1] == 'D':
                del stack[-1]
            else:
                stack.append(letter)

        # Similarly for 'U'
        else:
            if stack[-1] == 'U':
                del stack[-1]
            else:
                stack.append(letter)

        # If we started by going down and then came back to the sea level, it's
        # a valley
        if start == 'D' and len(stack) == 0:
            numValleys += 1

    return numValleys
