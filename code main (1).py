import sys

import f as f

file_in = open("sample_input.txt", "r")
readText = file_in.read()
file_in.close()
lis = readText.split('\n')
cost = {}
for i in lis:
    if len(i.split(':')) == 2:
        if i.split(':')[0] == "Number of employees":
            num_emp = int(i.split(':')[1])
        elif i.split(':')[1] != '':
            cost[i.split(':')[0]] = int(i.split(':')[1])
            cost = dict(sorted(cost.items(), key=lambda item: item[1]))
            map_keys = {}
            i = 1
for k, v in cost.items():
    map_keys[i] = k
    i += 1
    # number of employees from list with least cost diff------------
min_cost = float('inf')
min_i = -1
for i in range(1, len(cost) - num_emp):
    if min_cost > cost[map_keys[i + num_emp - 1]] - cost[map_keys[i]]:
        min_cost = cost[map_keys[i + num_emp - 1]] - cost[map_keys[i]]
        min_i = i
file_out = open("sample_output.txt", "w")
file_out.write("The goodies selected for distribution are:\n")
for i in range(min_i, min_i + num_emp):
    file_out.write("\n" + map_keys[i] + ": " + str(cost[map_keys[i]]))


    x = "\nAnd the difference between the chosen goodie with highest price and the lowest price is " + str(min_cost)
file_out.write(x)
file_out.close()
