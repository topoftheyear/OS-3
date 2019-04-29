class FIFO:
    def __init__(self, size=200, queue=list(), speed=1, head=100):
        self.disk = [0] * size
        self.queue = queue
        self.override = False
        self.speed = speed
        self.head = head

        if self.speed == 0:
            raise ValueError("Speed should be greater than 0, idiot")

    # Add an item to the queue so it'll be taken care of when the disk is on
    def append(self, item):
        if 0 <= item < len(self.disk):
            self.queue.append(item)
        else:
            print(f'Could not append {item} to disk: Out of range')

    # Returns size of disk
    def size(self):
        return len(self.disk)

    # Boots the disk so it actively deals with items in the queue
    def start(self):

        # If not stopped
        while not self.override:

            # If there are items in the queue, spin the head to add it
            if len(self.queue) > 0:
                current = self.queue[0]

                # If the head is currently at the correct destination, modify the disk
                if self.head == current:
                    self.queue.pop(0)
                    self.disk[self.head] += 1
                # Else spin the head in the closest direction to get there
                else:
                    if self.head < current:
                        distance = current - self.head
                        if distance > int(len(self.disk) / 2):
                            self.head -= min(distance, self.speed)
                        else:
                            self.head += min(distance, self.speed)
                    else:
                        distance = self.head - current
                        if distance > int(len(self.disk) / 2):
                            self.head += min(distance, self.speed)
                        else:
                            self.head -= min(distance, self.speed)

                    # Deal with the looping around
                    if self.head > len(self.disk):
                        self.head = 0
                    if self.head < 0:
                        self.head = len(self.disk)

        return

    # Stops the disk from running when the queue empties
    def stop(self):
        while True:
            if len(self.queue) <= 0:
                self.override = True
                return
