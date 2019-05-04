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
from FSCAN import FSCAN
from NStepSCAN import NStepSCAN

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

    # FSCAN
    disk = FSCAN()
    timer(disk, 1000, "F-SCAN Basic")

    # NStep
    disk = NStepSCAN()
    timer(disk, 1000, "N-Step Scan Basic")

    print("\nHead at 199 for following: \n")
    ##HEAD AT 199

    # First in first out
    disk = FIFO(head=199)
    timer_fixed_array(disk, [55, 58, 39, 18, 90, 160, 150, 38, 184], "FIFO head=199")

    # Last in first out
    disk = LIFO(head=199)
    timer_fixed_array(disk, [55, 58, 39, 18, 90, 160, 150, 38, 184], "LIFO head=199")

    # SSTF
    disk = SSTF(head=199)
    timer_fixed_array(disk, [55, 58, 39, 18, 90, 160, 150, 38, 184], "Shortest-Service-Time-First head=199")

    # SCAN
    disk = SCAN(head=199)
    timer_fixed_array(disk, [55, 58, 39, 18, 90, 160, 150, 38, 184], "SCAN head=199")

    # C-SCAN
    disk = CSCAN(head=199)
    timer_fixed_array(disk, [55, 58, 39, 18, 90, 160, 150, 38, 184], "C-SCAN head=199")

    # FSCAN
    disk = FSCAN(head=199)
    timer_fixed_array(disk, [55, 58, 39, 18, 90, 160, 150, 38, 184], "F-SCAN head=199")

    # NStep
    disk = NStepSCAN(head=199)
    timer_fixed_array(disk, [55, 58, 39, 18, 90, 160, 150, 38, 184], "N-Step Scan head=199")



    print("\nHead at 0 for following: \n")
    ##HEAD AT 0

    # First in first out
    disk = FIFO(head=0)
    timer_fixed_array(disk, [55, 58, 39, 18, 90, 160, 150, 38, 184], "FIFO head=0")

    # Last in first out
    disk = LIFO(head=0)
    timer_fixed_array(disk, [55, 58, 39, 18, 90, 160, 150, 38, 184], "LIFO head=0")

    # SSTF
    disk = SSTF(head=0)
    timer_fixed_array(disk, [55, 58, 39, 18, 90, 160, 150, 38, 184], "Shortest-Service-Time-First head=0")

    # SCAN
    disk = SCAN(head=0)
    timer_fixed_array(disk, [55, 58, 39, 18, 90, 160, 150, 38, 184], "SCAN head=0")

    # C-SCAN
    disk = CSCAN(head=0)
    timer_fixed_array(disk, [55, 58, 39, 18, 90, 160, 150, 38, 184], "C-SCAN head=0")

    # FSCAN
    disk = FSCAN(head=0)
    timer_fixed_array(disk, [55, 58, 39, 18, 90, 160, 150, 38, 184], "F-SCAN head=0")

    # NStep
    disk = NStepSCAN(head=0)
    timer_fixed_array(disk, [55, 58, 39, 18, 90, 160, 150, 38, 184], "N-Step Scan head=0")




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

    # FSCAN seek for table
    disk = FSCAN()
    timer_fixed_array(disk, [55,58,39,18,90,160,150,38,184], "FSCAN Fixed Array")

    # NStep seek for table
    disk = NStepSCAN()
    timer_fixed_array(disk, [55,58,39,18,90,160,150,38,184], "N-Step Fixed Array")

    # Time averages
    sum_time = 0
    run_amount = 15
    print("START FIFO AVERAGE")
    for x in range(run_amount):
        disk = FIFO()
        sum_time += timer(disk, 1000, "FIFO Run #")
    print("Average for FIFO: ", sum_time/run_amount, " seconds\n")

    # Time averages
    sum_time = 0
    run_amount = 15
    print("START LIFO AVERAGE")
    for x in range(run_amount):
        disk = LIFO()
        sum_time += timer(disk, 1000, "LIFO Run #")
    print("Average for LIFO: ", sum_time/run_amount, " seconds\n")

    # Time averages
    sum_time = 0
    run_amount = 15
    print("START SSTF AVERAGE")
    for x in range(run_amount):
        disk = SSTF()
        sum_time += timer(disk, 1000, "SSTF Run #")
    print("Average for SSTF: ", sum_time/run_amount, " seconds\n")

    # Time averages
    sum_time = 0
    run_amount = 15
    print("START SCAN AVERAGE")
    for x in range(run_amount):
        disk = SCAN()
        sum_time += timer(disk, 1000, "SCAN Run #")
    print("Average for SCAN: ", sum_time/run_amount, " seconds\n")

    # Time averages
    sum_time = 0
    run_amount = 15
    print("START CSCAN AVERAGE")
    for x in range(run_amount):
        disk = CSCAN()
        sum_time += timer(disk, 1000, "CSCAN Run #")
    print("Average for CSCAN: ", sum_time/run_amount, " seconds\n")

    # Time averages
    sum_time = 0
    run_amount = 15
    print("START FSCAN AVERAGE")
    for x in range(run_amount):
        disk = FSCAN()
        sum_time += timer(disk, 1000, "FSCAN Run #")
    print("Average for FSCAN: ", sum_time/run_amount, " seconds\n")

    # Time averages
    sum_time = 0
    run_amount = 15
    print("START N-Step AVERAGE")
    for x in range(run_amount):
        disk = NStepSCAN()
        sum_time += timer(disk, 1000, "N-Step Run #")
    print("Average for N-Step: ", sum_time/run_amount, " seconds\n")

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

    # LIFO Small, Fast and Weighted
    disk = LIFO(
        speed=4,
        size=100,
    )
    timer(
        disk,
        1000,
        "LIFO Weighted",
        weighted=True,
        weight=-10
    )

    # SSTF Small, Fast and Weighted
    disk = SSTF(
        speed=4,
        size=100,
    )
    timer(
        disk,
        1000,
        "STTF Weighted",
        weighted=True,
        weight=-10
    )

    # SCAN Small, Fast and Weighted
    disk = SCAN(
        speed=4,
        size=100,
    )
    timer(
        disk,
        1000,
        "SCAN Weighted",
        weighted=True,
        weight=-10
    )

    # CSCAN Small, Fast and Weighted
    disk = CSCAN(
        speed=4,
        size=100,
    )
    timer(
        disk,
        1000,
        "CSCAN Weighted",
        weighted=True,
        weight=-10
    )

    # FSCAN Small, Fast and Weighted
#    disk = FSCAN(
#        speed=4,
#        size=100,
#    )
#    timer(
#        disk,
#        1000,
#        "FSCAN Weighted",
#        weighted=True,
#        weight=-10
#    )

    # NStep Small, Fast and Weighted
    disk = NStepSCAN(
        speed=4,
        size=100,
    )
    timer(
        disk,
        1000,
        "NStep Weighted",
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
