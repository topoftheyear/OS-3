class CSCAN:
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
            self.queue = sorted(self.queue)
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
            if len(self.queue) > 0:

                # If current head is in the queue, remove it from the queue
                if self.head in self.queue:
                    self.queue.remove(self.head)
                    self.disk[self.head] += 1
                # Else spin positive to the closest
                else:
                    # Find closest element to current head
                    closest = 0
                    for thing in self.queue:
                        if thing > closest:
                            closest = thing
                            break
                    else:
                        closest = self.queue[0]

                    # Deal with overlap from max size to 0
                    distance = closest - self.head
                    if distance < 0:
                        distance += self.size()

                    self.head += min(self.speed, distance)

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
