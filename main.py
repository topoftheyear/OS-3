import time
import random
import disk_thread

from FIFO import FIFO


def main():
    # First in first out
    disk = FIFO(speed=2088)
    timer(disk, 10000)


def timer(disk, number_of_elements):
    start_time = time.time()
    new_disk = disk_processing(disk, number_of_elements)
    print(f'FIFO basic: {time.time() - start_time} seconds')
    # print(*new_disk.disk)


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
