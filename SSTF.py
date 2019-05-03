class SSTF:
    def __init__(self, size=200, queue=list(), speed=1, head=100):
        self.disk = [0] * size
        self.queue = queue
        self.override = False
        self.speed = speed
        self.head = head
        self.sum_travel = 0

        if self.speed == 0:
            raise ValueError("Speed should be greater than 0, idiot")

        self.current = None

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
                # If current head is in the queue, remove it from the queue
                if self.head in self.queue:
                    self.queue.remove(self.head)
                    self.current = None
                if self.current is None:
                    distance = 201
                    destination = -1
                    self.queue = sorted(self.queue)
                    for item in self.queue:
                        if self.head < item:
                            if item - self.head < distance:
                                distance = item - self.head
                                destination = item
                        elif self.head > item:
                            if self.head - item < distance:
                                distance = self.head - item
                                destination = item
                        elif self.head == item:
                            destination = item
                            break
                    self.current = destination
                # Else spin the head in the closest direction to get there
                else:
                    if self.head < self.current:
                        distance = self.current - self.head
                        self.head += min(distance, self.speed)
                        self.sum_travel += min(distance, self.speed)
                    else:
                        distance = self.head - self.current
                        self.head -= min(distance, self.speed)
                        self.sum_travel += min(distance, self.speed)
        return

    # Stops the disk from running when the queue empties
    def stop(self):
        while True:
            if len(self.queue) <= 0:
                self.override = True
                print("total travel SSTF: ", self.sum_travel)
                return
