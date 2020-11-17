import process_surroundings as ps

def process_coordinates(list_of_dicts):
    for dic in list_of_dicts:
        ps.process_surroundings(dic['latitude'], dic['longitude'])