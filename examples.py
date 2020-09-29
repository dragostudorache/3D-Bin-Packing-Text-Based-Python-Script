import _3dbp as threeD
# Testing-----------------------------------

# create bin
bin = threeD.Bin("Container1", 5, 3, 4)

# create items
items_list = []
items_list.append(threeD.Item("Item01", 2, 2, 3))
items_list.append(threeD.Item("Item02", 1, 4, 1))
items_list.append(threeD.Item("Item03", 2, 4, 1))
items_list.append(threeD.Item("Item04", 2, 2, 2))
items_list.append(threeD.Item("Item05", 1, 1, 1))
items_list.append(threeD.Item("Item06", 3, 2, 1))
items_list.append(threeD.Item("Item07", 3, 1, 2))
items_list.append(threeD.Item("Item08", 3, 1, 1))
items_list.append(threeD.Item("Item09", 1, 2, 1))
items_list.append(threeD.Item("Item10", 1, 2, 1))
items_list.append(threeD.Item("Item11", 1, 1, 1))
items_list.append(threeD.Item("Item12", 2, 1, 2))

print("BEFORE packing:")
for item in items_list:
    item.print_data()
print("---------------------------------------------------")
print("There are", len(items_list), "items and the total volume of items is", threeD.get_items_total_volume(items_list))
bin.print_data()

# packing
threeD.bp3D(bin, items_list)

print("\nAFTER packing:")
for item in bin.items:
    item.print_data()
bin.print_data()

#-----------------------------------------------------------------------
# RANDOM TESTS
import random

print("\n\nRANDOM TESTS:")
number_of_tests = 10
average_space_wasted = 0

for i in range(number_of_tests):
    # dimensions
    containers_dimensions_range = (10, 15)

    # generate container
    w = random.randrange(containers_dimensions_range[0], containers_dimensions_range[1])
    h = random.randrange(containers_dimensions_range[0], containers_dimensions_range[1])
    d = random.randrange(containers_dimensions_range[0], containers_dimensions_range[1])
    test_bin = threeD.Bin("Container" + str(i), w, h, d)

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
        test_items_list.append(threeD.Item("Item" + str(wi + hi + di), wi, hi, di))
    print("BEFORE packing:")
    print("There are", len(test_items_list), "items and the total volume of items is", threeD.get_items_total_volume(test_items_list))
    test_bin.print_data()

    # packing
    threeD.bp3D(test_bin, test_items_list)

    print("AFTER packing:")
    test_bin.print_data()
    space_wasted = test_bin.remaining_space - (test_bin.width * test_bin.height * test_bin.depth - T_volume)
    space_wasted = space_wasted * 100 / T_volume
    print('%.2f'%space_wasted, "\b% space wasted")
    print("\n")
    average_space_wasted += space_wasted

print("Average space wasted:", average_space_wasted / number_of_tests)