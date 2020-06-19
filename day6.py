def create_planet(name):
    """
    Creates a planet where the 'name' is the name of the planet, and everything within
    the orbit list orbits the planet
    """
    planet = { 'name': name,
                'orbit': []}
    return planet

def set_orbit(planet, name):
    """
    Sets a new planet within the orbit of existing planet
    """
    new_planet = create_planet(name)
    planet['orbit'].append(new_planet)

def read_file(fileName):
    inFile = open(fileName, 'r')
    list_planets = []
    for line in inFile:
        line = line.rstrip().split(')')
        list_planets.append(line)
    return list_planets

def create_system(list_planets):
    first_O = list_planets[0]
    # Create the first planet
    COM = set_orbit(create_planet(first_O[0]), first_O[1])
    for planet in list_planets[1:]:
        search = search_system(COM, planet[0])
        if search[1]:
            set_orbit(search[0], planet[1])
        else:
            print('Not found')
            print(planet)
    return COM

def search_system(system, planet):
    """
    Searches a given system for a planet. Returns the planet, and True if found, returns False and the original COM if not found
    """
    # Recursive function to search if an orbit contains the planet name
    if system['name'] == planet:
        return system, True
    # If reaches the end of an orbital pathway without finding, it will return False
    elif system['orbit'] == []:
        return system, False
    else:
        check = search_system(system['orbit'][0], planet)
        if check[1]:
            return check
        if len(system['orbit']) > 1:
            search_system(system['orbit'][1:], planet)
    return system, False

#COM = create_planet('COM')
#second = set_orbit(COM, 'B')
#print(search_system(COM, 'B'))

planets = read_file('day6.txt')
print(planets)
system = create_system(planets)
print(system)