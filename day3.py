infile = open('day3.txt', 'r')
wire1 = infile.readline()
wire2 = infile.readline()

# wire1 = 'R8,U5,L5,D3'
# wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
# wire1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
wire1 = wire1.split(',')

# wire2 = 'U7,R6,D4,L4'
# wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
# wire2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
wire2 = wire2.split(',')


def wire_path(wires):
    """
    Calculates a defined wire path for a given set of directions

    :param wires: List of directions
    :return: List containing each point that the wire will cross
    """
    start = [[0,0]]
    position = -1
    for move in wires:
        start_x = start[position][0]
        start_y = start[position][1]
        movement = int(move[1:])
        for step in range(1, movement+1):
            if move[0] == 'R':
                end = [start_x + step, start_y]
            if move[0] == 'U':
                end = [start_x, start_y + step]
            if move[0] == 'L':
                end = [start_x - step, start_y]
            if move[0] == 'D':
                end = [start_x, start_y - step]
            start.append(end)
    return start

path1 = wire_path(wire1)
path2 = wire_path(wire2)

def common_locations(pathway1, pathway2):
    common_locations = []
    count = 0
    for location in pathway1:
        if location in pathway2:
            common_locations.append(location)
        if count % 2500 == 0:
            print(str(count/len(pathway1) * 100) + '%')
        count += 1
    print(common_locations)
    return common_locations

#common_locations = common_locations(path1, path2)

# Code was already run and printed values were pasted below
common_locations = [[0, 0], [-30, 776], [-26, 966], [539, 1880], [280, 2577], [-56, 2577], [-131, 2281], [-579, 1687], [-584, 1687], 
                    [-662, 1872], [-662, 1922], [-662, 1978], [-56, 2317], [90, 2688], [-1877, 3966], [-2256, 3966], [-2256, 4008], 
                    [-1877, 4008], [-4285, 4018], [-4048, 4005], [-3844, 4005], [-3344, 4229], [-3344, 4522], [-3344, 4781]]

# Calcualtes manhattan distance for each of the common points, and prints min value
#distances = [abs(x[0]) + abs(x[1]) for x in common_locations[1:]]
#print(distances)
#print(min(distances))


dist_steps =[]
for inter in common_locations[1:]:
    steps = []
    step_1 = 0
    # Will append the value of steps before reaching the common_locations in each path
    for step in path1:
        if inter != step:
            step_1 += 1
        else:
            steps.append(step_1)
    step_2 = 0
    for step in path2:
        if inter != step:
            step_2 += 1
        else:
            steps.append(step_2)
    dist_steps.append(steps[0] + steps[1])
print(min(dist_steps))
    

#dist_steps = 