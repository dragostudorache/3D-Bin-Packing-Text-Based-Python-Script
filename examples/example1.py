from _3dbp import Bin, Item, Items_List, bp3D, get_items_total_volume
# create bin
bin = Bin("Container1", 5, 3, 4)

# create items
items_list = Items_List()
items_list.add_item(Item("Item01", 2, 2, 3))
items_list.add_item(Item("Item02", 1, 4, 1))
items_list.add_item(Item("Item03", 2, 4, 1))
items_list.add_item(Item("Item04", 2, 2, 2))
items_list.add_item(Item("Item05", 1, 1, 1))
items_list.add_item(Item("Item06", 3, 2, 1))
items_list.add_item(Item("Item07", 3, 1, 2))
items_list.add_item(Item("Item08", 3, 1, 1))
items_list.add_item(Item("Item09", 1, 2, 1))
items_list.add_item(Item("Item10", 1, 2, 1))
items_list.add_item(Item("Item11", 1, 1, 1))
items_list.add_item(Item("Item12", 2, 1, 2))

print("BEFORE packing:")
for item in items_list.items:
    item.print_data()
print("---------------------------------------------------\n")

print("There are", len(items_list.items), "items and the total volume of items is", get_items_total_volume(items_list.items))
bin.print_data()

# packing
bp3D(bin, items_list.items)

print("\nAFTER packing:")
for item in bin.items:
    item.print_data()
print("---------------------------------------------------\n")

bin.print_data()