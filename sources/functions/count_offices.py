# This function recieves a list of dictionaries as argument,
# specifically a json from a mongo dataset.
# The function 'count_offices' return a dictionary with 
# the name and the number of offices for each company in the dataset.

def count_offices(diclst):
    return {dic['name']:len(dic['offices']) for dic in diclst}