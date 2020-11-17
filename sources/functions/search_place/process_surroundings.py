import apply_google_place as asp

def process_surroundings(latitude, longitude):
    # Additional parameters for google search place API,
    # it follows the structure below:
    # (type,keyword,minprice)
    parameters = [
        ('cafe', 'starbucks'),
        ('restaurant', 'vegan restaurant'),
        ('pet_store', 'dog groomer'),
        ('night_club', ''),
        ('airport', 'interntional airport')
    ]
    for x,y in parameters:
        asp.apply_google_place(latitude,longitude,category=x,keyword=y) # ,minprice=z)