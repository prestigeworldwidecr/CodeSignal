'''

Great! The next problem is very similar to the second one from the lesson, but now you are a linguist analyst who works with texts, not integer values. Your goal is to design a MovingAverage class that accepts new words and keeps tracking the average length of the last size words.

Don't forget to round your answer to two decimal places so your output looks awesome!

'''

from collections import deque

class MovingAverage :
# {
    def __init__(self, size) :
    # {
        self.queue = deque(maxlen=size)
        self.size = size
        self.total = 0
    # }

    def calculate_moving_average(self, word) :
    # {
        # implement this
        if (len(self.queue) == self.size) :
        # {
            # self.total -= self.queue.popleft()
            self.total = self.total - self.queue.popleft()
        # }

        else :
        # {
            None
        # }

        self.queue.append(len(word))
        # self.total += val
        self.total = self.total + len(word)

        return round(self.total / len(self.queue), 2)
    # }

# }

# Test samples
ma = MovingAverage(3)
print(ma.calculate_moving_average('one'))  # Expected: 3.0
print(ma.calculate_moving_average('two'))  # Expected: 3.0
print(ma.calculate_moving_average('three'))  # Expected: 3.67
print(ma.calculate_moving_average('four'))  # Expected: 4.0
print(ma.calculate_moving_average('five'))  # Expected: 4.33
print(ma.calculate_moving_average('six'))  # Expected: 3.67


'''

***** BONEYARD *****

if (len(self.queue) == self.size) :
        # {
            # self.total -= self.queue.popleft()
            self.total = self.total - self.queue.popleft()
        # }

        else :
        # {
            None
        # }

        self.queue.append(val)
        # self.total += val
        self.total = self.total + val

        return round(self.total / len(self.queue), 2)

# print(self, word)

'''