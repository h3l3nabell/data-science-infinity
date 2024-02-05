#dictionaries

my_dict = {}

#vs set
a_set = {1,2,3}

planet_dict = {
    "Mercury" : 8,
    "Venus" : 6,
    "Earth" : 5,
    "Mars" : 7,
    "Jupiter" : 1,
    "Saturn" : 2,
    "Uranus" : 3,
    "Neptune" : 4
    }

len(planet_dict)

planet_dict["Mars"]
planet_dict["Earth"]
#key error
planet_dict["Tatooine"]

planet_dict.get("Neptune")
planet_dict.get("Tatooine", 0)

"Saturn" in planet_dict
planet_dict.keys()
planet_dict.values()

planet_dict["Pluto"] = 9
print(planet_dict)

planet_dict["Uranus"] = 4
planet_dict["Neptune"] = 3
print(planet_dict)

planet_dict.pop("Earth")
print(planet_dict)