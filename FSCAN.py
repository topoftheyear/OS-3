import random


class FSCAN:
    def __init__(self, size=200, queue_one=list(), queue_two=list(), speed=1, head=100):
        self.disk = [0] * size
        self.queue_one = queue_one
        self.queue_two = queue_two
        self.override = False
        self.speed = speed
        self.head = head
        self.first_queue_done = False
        self.sum_travel = 0

        if self.speed == 0:
            raise ValueError("Speed should be greater than 0, idiot")

    # Add an item to the queue so it'll be taken care of when the disk is on
    def append(self, item):
        if 0 <= item < len(self.disk):
            self.queue_one.append(item)
            self.queue_one = sorted(self.queue_one)
        else:
            print(f'Could not append {item} to disk: Out of range')

    def append_during_runtime(self, item):
        if 0 <= item < len(self.disk):
            self.queue_two.append(item)
            self.queue_two = sorted(self.queue_two)
        else:
            print(f'Could not append {item} to disk: Out of range')

    # Returns size of disk
    def size(self):
        return len(self.disk)

    # Boots the disk so it actively deals with items in the queue
    def start(self):
        # If not stopped
        while not self.override:

            # If there are items in the queue, spin the head
            if len(self.queue_one) > 0:
                # Append items to the second queue
                if len(self.queue_two) < 1000:
                    item = random.randint(0, len(self.disk)-1)
                    self.append_during_runtime(item)

                # If current head is in the queue, remove it from the queue
                if self.head in self.queue_one:
                    self.queue_one.remove(self.head)
                    self.disk[self.head] += 1
                # Else spin positive to the closest
                else:
                    # Find closest element to current head
                    closest = 0
                    for thing in self.queue_one:
                        if thing > closest:
                            closest = thing
                            break
                    else:
                        closest = self.queue_one[0]

                    # Deal with overlap from max size to 0
                    distance = closest - self.head
                    if distance < 0:
                        distance += self.size()

                    self.head += min(self.speed, distance)
                    self.sum_travel += min(self.speed, distance)

                # Deal with the looping around
                if self.head > len(self.disk):
                    self.head = 0
                if self.head < 0:
                    self.head = len(self.disk)

        return

    def start_second_queue(self):
        # If not stopped
        while not self.override:

            # If there are items in the queue, spin the head
            if len(self.queue_two) > 0:

                # If current head is in the queue, remove it from the queue
                if self.head in self.queue_two:
                    self.queue_two.remove(self.head)
                    self.disk[self.head] += 1
                # Else spin positive to the closest
                else:
                    # Find closest element to current head
                    closest = 0
                    for thing in self.queue_two:
                        if thing > closest:
                            closest = thing
                            break
                    else:
                        closest = self.queue_two[0]

                    # Deal with overlap from max size to 0
                    distance = closest - self.head
                    if distance < 0:
                        distance += self.size()

                    self.head += min(self.speed, distance)
                    self.sum_travel += min(self.speed, distance)

                # Deal with the looping around
                if self.head > len(self.disk):
                    self.head = 0
                if self.head < 0:
                    self.head = len(self.disk)
            else:
                break
        return

    # Stops the disk from running when the queue empties
    def stop(self):
        while True:
            if len(self.queue_one) <= 0 and not self.first_queue_done:
                self.first_queue_done = True
                self.start_second_queue()
            elif len(self.queue_two) <= 0 and self.first_queue_done:
                self.override = True
                print("total travel FSCAN: ", self.sum_travel)
                return
