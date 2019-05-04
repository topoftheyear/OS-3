class NStepSCAN:
    def __init__(self, size=200, queue=list(), speed=1, head=100):
        self.disk = [0] * size
        self.queue = queue
        self.queue_array = [self.queue] * 10
        self.queue_size = 1000
        self.current_queue = 0
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
            for i in range(10):
                if len(self.queue_array[i]) < self.queue_size:
                    self.queue_array[i].append(item)
                    self.queue_array[i] = sorted(self.queue_array[i])
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
            if len(self.queue_array[self.current_queue]) > 0:

                # If current head is in the queue, remove it from the queue
                if self.head in self.queue_array[self.current_queue]:
                    self.queue_array[self.current_queue].remove(self.head)
                # Else spin direction specified
                else:
                    chosen = False
                    closest = 0
                    while not chosen:
                        if direction > 0:  # positive direction
                            # Find closest element to current head
                            closest = 200
                            for thing in self.queue_array[self.current_queue]:
                                if closest > thing > self.head:
                                    closest = thing
                            if closest == 200:  # if not found, switch direction
                                #print("not found, switching to negative")
                                direction = -1
                            else:
                                chosen = True
                                distance = closest - self.head
                                self.head += min(self.speed, distance)
                                self.sum_travel += min(self.speed, distance)
                                #print("move head to ", self.head)
                        elif direction < 0:  # negative direction
                            closest = -1
                            for thing in self.queue_array[self.current_queue]:
                                if closest < thing < self.head:
                                    closest = thing
                            if closest == -1:
                                #print("not found, switching to positive")
                                direction = 1  # if not found, switch direction
                            else:
                                chosen = True
                                distance = self.head - closest
                                self.head -= min(self.speed, distance)
                                self.sum_travel += min(self.speed, distance)
                                #print("move head to ", self.head)
            if len(self.queue_array[self.current_queue]) <= 0:
                self.current_queue += 1
                if self.current_queue > 9:
                    self.current_queue = 0
        return

    # Stops the disk from running when the queue empties
    def stop(self):
        while True:
            for queue in self.queue_array:
                if len(queue) > 0:
                    break
                else:
                    self.override = True
                    print("total travel N-Step: ", self.sum_travel)
                    return
