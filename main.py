import time
import random
import disk_thread
from numpy.random import choice
from tqdm import tqdm

from FIFO import FIFO
from LIFO import LIFO
from CSCAN import CSCAN
from SCAN import SCAN
from SSTF import SSTF


def main():
    # First in first out
    disk = FIFO()
    timer(disk, 1000, "FIFO Basic")

    # Last in first out
    disk = LIFO()
    timer(disk, 1000, "LIFO Basic")

    # SSTF
    disk = SSTF()
    timer(disk, 1000, "Shortest-Service-Time-First Basic")

    # SCAN
    disk = SCAN()
    timer(disk, 1000, "SCAN Basic")

    # C-SCAN
    disk = CSCAN()
    timer(disk, 1000, "C-SCAN Basic")

    # FIFO seek for table
    disk = FIFO()
    timer_fixed_array(disk, [55,58,39,18,90,160,150,38,184], "FIFO Fixed Array")

    # LIFO seek for table
    disk = LIFO()
    timer_fixed_array(disk, [55,58,39,18,90,160,150,38,184], "LIFO Fixed Array")

    # SSTF seek for table
    disk = SSTF()
    timer_fixed_array(disk, [55,58,39,18,90,160,150,38,184], "SSTF Fixed Array")

    # SCAN seek for table
    disk = SCAN()
    timer_fixed_array(disk, [55,58,39,18,90,160,150,38,184], "SCAN Fixed Array")

    # CSCAN seek for table
    disk = CSCAN()
    timer_fixed_array(disk, [55,58,39,18,90,160,150,38,184], "CSCAN Fixed Array")

    # FIFO Small, Fast and Weighted
    disk = FIFO(
        speed=4,
        size=100,
    )
    timer(
        disk,
        1000,
        "FIFO Weighted",
        weighted=True,
        weight=-10
    )


# Weighted is a boolean that will determine if the numbers added will be weighted or not
# Weight is a number that will determine how steep the linear weight will be, higher is smoother
def timer(disk, number_of_elements, name, weighted=False, weight=0):
    start_time = time.time()
    new_disk = disk_processing(disk, number_of_elements, weighted, weight)
    t = time.time() - start_time
    print(f'{name}: {t} seconds')
    # print(*new_disk.disk)
    return t


def disk_processing(disk, number_of_elements, weighted=False, weight=0):
    thread = disk_thread.Thread(disk.start)
    thread.start()

    for x in range(number_of_elements):
        if not weighted:
            item = random.randint(0, disk.size() - 1)
            disk.append(item)
        else:
            # Generates a list of weights
            weights = gen_weights(disk, weight)
            # Randomly picks one and adds it to the list
            disk.append(choice(range(disk.size()), p=weights))

    disk.stop()

    return disk


# The larger the weight given, the more balanced the scaling will be
def gen_weights(disk, weight=0):
    weights = [0] * disk.size()
    head = disk.head

    for x in range(disk.size()):
        num = disk.size() - abs(head - x) + weight
        num = max(num, 0)
        weights[x] = num

    total = sum(weights)
    for x in range(disk.size()):
        weights[x] = weights[x] / total

    return weights


def timer_fixed_array(disk, array_of_elements, name):
    start_time = time.time()
    new_disk = disk_processing_fixed_array(disk, array_of_elements)
    t = time.time() - start_time
    print(f'{name}: {t} seconds')
    # print(*new_disk.disk)
    return t


def disk_processing_fixed_array(disk, array_of_elements):
    thread = disk_thread.Thread(disk.start)
    thread.start()

    for x in array_of_elements:
        disk.append(x)

    disk.stop()

    return disk


if __name__ == '__main__':
    main()
