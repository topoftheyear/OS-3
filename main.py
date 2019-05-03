import time
import random
import disk_thread

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


def timer(disk, number_of_elements, name):
    start_time = time.time()
    new_disk = disk_processing(disk, number_of_elements)
    t = time.time() - start_time
    print(f'{name}: {t} seconds')
    # print(*new_disk.disk)
    return t


def disk_processing(disk, number_of_elements):
    thread = disk_thread.Thread(disk.start)
    thread.start()

    for x in range(number_of_elements):
        item = random.randint(0, disk.size() - 1)
        disk.append(item)

    disk.stop()

    return disk


if __name__ == '__main__':
    main()
