class SCAN:
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
        direction = -1  # -1 is go negative down queue, 1 is up queue
        # If not stopped
        while not self.override:

            # If there are items in the queue, spin the head to add it
            if len(self.queue) > 0:

                # If current head is in the queue, remove it from the queue
                if self.head in self.queue:
                    self.queue.remove(self.head)
                # Else spin direction specified
                else:
                    chosen = False
                    closest = 0
                    while not chosen:
                        if direction > 0:  # positive direction
                            # Find closest element to current head
                            closest = 200
                            for thing in self.queue:
                                if closest > thing > self.head:
                                    closest = thing
                            if closest == 200:  # if not found, switch direction
                                direction = -1
                            else:
                                chosen = True
                                distance = closest - self.head
                                self.head += min(self.speed, distance)
                                self.sum_travel += min(self.speed, distance)
                        elif direction < 0:  # negative direction
                            closest = -1
                            for thing in self.queue:
                                if closest < thing < self.head:
                                    closest = thing
                            if closest == -1:
                                direction = 1  # if not found, switch direction
                            else:
                                chosen = True
                                distance = self.head - closest
                                self.head -= min(self.speed, distance)
                                self.sum_travel += min(self.speed, distance)
        return

    # Stops the disk from running when the queue empties
    def stop(self):
        while True:
            if len(self.queue) <= 0:
                self.override = True
                print("total travel SCAN: ", self.sum_travel)
                return
