import random
import os

MAX_WIDTH = 40
MAX_HEIGHT = 40
MAX_NODE_COUNT = 1000

def is_duplicated(position, list) :
    for element in list :
        if element[0] == position[0] and element[1] == position[1] :
            return 1

    return 0

def clear() :
    os.system("clear")
    print("=="*MAX_WIDTH)

def distance(node1, node2) :
    return ((node2[0] - node1[0]) ** 2 + (node2[1] - node1[1])**2)**(1/2)

node_list = []

clear()

while True :
    x = random.randint(0, MAX_HEIGHT - 1)
    y = random.randint(0, MAX_HEIGHT - 1)
    position = (x, y)
    
    if is_duplicated(position, node_list) == 1 :
        continue
    else :
        node_list.append(position)

    if len(node_list) == MAX_NODE_COUNT :
        break

for h in range(0, MAX_HEIGHT) :
    for w in range(0, MAX_WIDTH) :
        if (h, w) in node_list : 
            print("o ", end="")
        else :
            print("  ", end="")
    print()

k = int(input("k = "))
# k = 3
clear()
mode_node_list = []

# 중복이 없다고 가정
for _ in range(0, k) :
    mode_node_list.append(node_list[random.randint(0, MAX_NODE_COUNT - 1)])

for h in range(0, MAX_HEIGHT) :
    for w in range(0, MAX_WIDTH) :
        if (h, w) in mode_node_list :
            print("\033[31m" + "x " + "\033[0m", end="")
        elif (h, w) in node_list : 
            print("o ", end="")
        else :
            print("  ", end="")
    print()

input()
clear()

color_list = [31, 32, 33, 34, 35, 36, 37, 90, 91, 92, 93, 94, 95, 96, 97]
for h in range(0, MAX_HEIGHT) :
    for w in range(0, MAX_WIDTH) :
        if (h, w) in mode_node_list :
            print(f"\033[{color_list[mode_node_list.index((h, w))]}mx \033[0m", end="")
        elif (h, w) in node_list : 
            close_node_index = 0
            close_node_distance = distance((h, w), mode_node_list[0])

            for i in range(1, len(mode_node_list)) :
                if distance((h, w), mode_node_list[i]) < close_node_distance :
                    close_node_index = i
                    close_node_distance = distance((h, w), mode_node_list[i])

            # print(f"\033[{color_list[close_node_index]}m{close_node_index} \033[0m", end="")
            print(f"\033[{color_list[close_node_index]}mo \033[0m", end="")
        else :
            print("  ", end="")
    print()