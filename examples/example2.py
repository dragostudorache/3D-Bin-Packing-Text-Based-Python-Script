# RANDOM TESTS
import random
from _3dbp import Bin, Item, Items_List, bp3D, get_items_total_volume

number_of_tests = 10
average_space_wasted = 0

for i in range(number_of_tests):
    # dimensions
    containers_dimensions_range = (10, 15)

    # generate container
    w = random.randrange(containers_dimensions_range[0], containers_dimensions_range[1])
    h = random.randrange(containers_dimensions_range[0], containers_dimensions_range[1])
    d = random.randrange(containers_dimensions_range[0], containers_dimensions_range[1])
    test_bin = Bin("Container" + str(i), w, h, d)

    # generate items
    test_items_list = []
    T_volume = 0
    while True:
        wi = random.randrange(1, w // 2 + 1)
        hi = random.randrange(1, h // 2 + 1)
        di = random.randrange(1, d // 2 + 1)
        if T_volume + wi * hi * di > w * h * d:
            break
        else:
            vol = wi * hi * di
            T_volume += vol
        test_items_list.append(Item("Item" + str(wi + hi + di), wi, hi, di))
    print("There are", len(test_items_list), "items and the total volume of items is", get_items_total_volume(test_items_list))
    print("BEFORE packing:")
    test_bin.print_data()

    # packing
    bp3D(test_bin, test_items_list)

    print("AFTER packing:")
    test_bin.print_data()
    space_wasted = test_bin.remaining_space - (test_bin.width * test_bin.height * test_bin.depth - T_volume)
    space_wasted = space_wasted * 100 / T_volume
    print('%.2f'%space_wasted, "\b% space wasted")
    print("---------------------------------------------------")
    average_space_wasted += space_wasted

average_space_wasted /= number_of_tests
print("Average space wasted:", '%.2f'%average_space_wasted, "\b%")