# This function recieves a list of dictionaries as argument,
# specifically a json from a mongo dataset.
# The function 'count_categories' return a dictionary with 
# the category_code and the number of times that appears
#  for each company in the dataset.

def count_categories(diclst):
    categories = [
        dic['category_code']
            for dic in diclst 
                if 'category_code' in dic.keys()
    ]
    return {k:categories.count(k) for k in categories}