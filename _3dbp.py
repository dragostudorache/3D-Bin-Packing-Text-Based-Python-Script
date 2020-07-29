import copy
from math import ceil

class Bin(object):
    def __init__(self, name, width, height, depth):
        self.name = name

        # dimensions
        self.width = width
        self.height = height
        self.depth = depth

        # conditions
        if self.width <= 0 or self.height <= 0 or self.depth <= 0:
            print("Wrong bin dimensions")
            exit(10)

        # bin's items
        self.items = []

        self.remaining_space = self.width * self.height * self.depth

        # 3D representation for the bin
        self.vector_3D = []
        self.build_vector()

    def build_vector(self):
        # 3D - Vector
        for i in range(0, self.width):
            new_list1 = []

            for j in range(0, self.height):
                new_list2 = []

                for k in range(0, self.depth):
                    new_list2.append(0)

                new_list1.append(new_list2)

            self.vector_3D.append(new_list1)

    def print_data(self):
        print(self.name, "|", self.width, "x", self.height, "x", self.depth, "|", len(self.items), "items |", self.remaining_space, "remaining space")

    def pack(self, item, position, type):
        #print("PACKED", position, item.rotate(type))
        # add item to packed items
        self.items.append(item)

        # edit 3D vector
        for i in range(position[0], position[0] + item.rotate(type)[0]):
            for j in range(position[1], position[1] + item.rotate(type)[1]):
                for k in range(position[2], position[2] + item.rotate(type)[2]):
                    self.vector_3D[i][j][k] = 1

        # edit remaining space
        volume = item.width * item.height * item.depth
        self.remaining_space -= volume

        # edit item's info
        item.pos = copy.deepcopy(list(position))
        item.RT = type

        '''
        print("The Vector")
        for i in range(self.width):
            for j in range(self.height):
                print(self.vector_3D[i][j])
        print("---------------")
        '''

    def can_be_packed(self, item, position, type):
        for i in range(position[0], position[0] + item.rotate(type)[0]):
            for j in range(position[1], position[1] + item.rotate(type)[1]):
                for k in range(position[2], position[2] + item.rotate(type)[2]):
                    # check for bin's limits
                    if i >= self.width or j >= self.height or k >= self.depth:
                        return False

                    # check if the space is already used
                    if self.vector_3D[i][j][k] == 1:
                        return False

        # check if the item above another item has at least half of its dimension on the underitem
        if position[1] >= 1:
            for i in range(position[0], ceil((position[0] + item.rotate(type)[0]) / 2)):
                    for k in range(position[2], ceil((position[2] + item.rotate(type)[2]) / 2)):
                        if self.vector_3D[i][position[1] - 1][k] == 0:
                            return False

        #print(item.name, "is going to be packed at", position, "and its dimension is", item.rotate(type))
        return True

class Item(object):
    def __init__(self, name, width, height, depth):
        self.name = name

        # dimensions w x h x d
        self.width = width
        self.height = height
        self.depth = depth

        if self.width <= 0 or self.height <= 0 or self.depth <= 0:
            print("Wrong item dimensions")
            exit(20)

        # position in the bin, if it'll be packed
        self.pos = [-1, -1, -1]

        # rotation type - [0; 5], see Item.rotate to know how the item is rotated
        self.RT = 0

    def print_data(self):
        print(self.name, "|", self.width, "x", self.height, "x", self.depth, "|", self.pos, "| self.RT =", self.RT)

    # rotations
    def rotate(self, type):
        if type == 0: # normal position
            return (self.width, self.height, self.depth)
        elif type == 1: # rotate Z
            return (self.height, self.width, self.depth)
        elif type == 2: # rotate Y
            return (self.width, self.depth, self.height)
        elif type == 3: # rotate X, rotate Y
            return (self.depth, self.width, self.height)
        elif type == 4: # rotate X
            return (self.depth, self.height, self.width)
        else: # rotate X, rotate Z
            return (self.height, self.depth, self.width)

def get_items_total_volume(item_list):
    volume_T = 0
    for item in item_list:
        volume = item.width * item.height * item.depth
        volume_T += volume

    return volume_T

def sort_by_volume(item_list):
    for i in range(len(item_list)):
        for j in range(len(item_list)):
            if item_list[i].width * item_list[i].height * item_list[i].depth > item_list[j].width * item_list[j].height * item_list[j].depth:
                item_list[i], item_list[j] = item_list[j], item_list[i]

    return item_list

def bp3D(current_bin, Items):
    # conditions
    if type(current_bin) != Bin:
        print("Incorrect current_bin parameter!")
        exit(30)

    if type(Items) != list or len(Items) == 0 or type(Items[0]) != Item:
        print("Incorrect Items parameter!")
        exit(31)

    # Documentation link from where the strategy and the algorithm was taken.
       # https://www.researchgate.net/publication/228974015_Optimizing_Three-Dimensional_current_bin_Packing_Through_Simulation
    # Consider that the strategy and the algorithm from this code have been heavily changed for my needs.
    notPacked = copy.deepcopy(Items)

    # sort items by volume
    notPacked = sort_by_volume(notPacked)

    # put the first item in the current_bin
    for i in range(6):
        if notPacked[0].rotate(i)[0] > current_bin.width or \
            notPacked[0].rotate(i)[1] > current_bin.height or \
            notPacked[0].rotate(i)[2] > current_bin.depth:
            pass
        else:
            current_bin.pack(notPacked[0], (0, 0, 0), i)
            del notPacked[0]
            break

    while True:
        # if no change is detected the loop will stop
        not_changes = True

        for i in range(len(notPacked)):
            current_item = notPacked[i]

            for j in range(len(current_bin.items)):
                current_bin_item = current_bin.items[j]

                # choose the available position
                for p in range(3):
                    pivot = [-1, -1, -1]

                    if p == 0: # back lower right corner of current_bin_item
                        pivot = [
                            current_bin_item.pos[0] + current_bin_item.rotate(current_bin_item.RT)[0],
                            current_bin_item.pos[1],
                            current_bin_item.pos[2]
                        ]
                    elif p == 1: # front lower left corner
                        pivot = [
                            current_bin_item.pos[0],
                            current_bin_item.pos[1],
                            current_bin_item.pos[2] + current_bin_item.rotate(current_bin_item.RT)[2]
                        ]
                    else: # back upper left corner
                        pivot = [
                            current_bin_item.pos[0],
                            current_bin_item.pos[1] + current_bin_item.rotate(current_bin_item.RT)[1],
                            current_bin_item.pos[2]
                        ]

                    # try to find a rotation type for packing
                    for k in range(6):
                        if current_bin.can_be_packed(current_item, pivot, k):
                            current_bin.pack(current_item, pivot, k)
                            del notPacked[i]
                            not_changes = False
                            break

                    if not_changes == False:
                        break

                if not_changes == False:
                    break

            if not_changes == False:
                break

        if not_changes:
            break