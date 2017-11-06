class Planets(object):
    # Initialize the Lists & Dictionaries for the Planets
    def __init__(self):
        self.planets_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
        self.planets = {'Mercury': {'name': 'Mercury', 'gravity': 3.59, 'distance_from_sun': 58000000, 'surface': 'Rocky', 'moons': 'No', 'rings': 'No', 'mass_to_earth': 0.055},
                        'Venus': {'name': 'Venus', 'gravity': 8.87, 'distance_from_sun': 108000000, 'surface': 'Rocky', 'moons': 'No', 'rings': 'No', 'mass_to_earth': 0.815},
                        'Earth': {'name': 'Earth', 'gravity': 9.81, 'distance_from_sun': 150000000, 'surface': 'Rocky', 'moons': 'Yes', 'rings': 'No', 'mass_to_earth': 1},
                        'Mars': {'name': 'Mars', 'gravity': 3.77, 'distance_from_sun': 228000000, 'surface': 'Rocky', 'moons': 'Yes', 'rings': 'No', 'mass_to_earth': 0.10744},
                        'Jupiter': {'name': 'Jupiter', 'gravity': 25.95, 'distance_from_sun': 778000000, 'surface': 'Gaseous', 'moons': 'Yes', 'rings': 'Yes', 'mass_to_earth': 317.82},
                        'Saturn': {'name': 'Saturn', 'gravity': 11.08, 'distance_from_sun': 1427000000, 'surface': 'Gaseous', 'moons': 'Yes', 'rings': 'Yes', 'mass_to_earth': 95.16},
                        'Uranus': {'name': 'Uranus', 'gravity': 10.67, 'distance_from_sun': 2871000000, 'surface': 'Gaseous', 'moons': 'Yes', 'rings': 'Yes', 'mass_to_earth': 14.371},
                        'Neptune': {'name': 'Neptune', 'gravity': 14.07, 'distance_from_sun': 4498000000, 'surface': 'Gaseous', 'moons': 'Yes', 'rings': 'Yes', 'mass_to_earth': 17.147}}

    def getGravity(self, name):
        """ Returns the Gravitational Acceleration of that Specific Planet. """
        return self.planets[name]['gravity']

    def addPlanet(self, name, gravity, distance_from_sun, surface, moons, rings, mass_to_earth):
        """ Adds a Planet to the List and to the Planets Dictionary. """
        self.planets_list.append(name)
        self.planets[name] = {'name': name, 'gravity': gravity, 'distance_from_sun': distance_from_sun, 'surface': surface,
                              'moons': moons, 'rings': rings, 'mass_to_earth': mass_to_earth}

    def getPlanet(self, name):
        """ Returns the Attributes of a Specific Planet. """
        return self.planets[name].items()

    def getPlanetsList(self):
        """ Return a List of the Existing Planets. """
        return self.planets_list
