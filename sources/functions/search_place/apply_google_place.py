import properties.client as mongo
import google_place as sp

# Lest's apply google_place function.
# The following builds a list of nearby places
# and stores it in mongoDB (local).
def apply_google_place(latitude, longitude, category, keyword=''): #, minprice=''
    # Get json from Google API "Search Place (Nearby Search)" based on 
    # latitude, longitude, category, keyword
    data_json = sp.google_place(latitude, longitude, category, keyword)
    # In this case, it just would be considered the first three result for each
    i = 3 if len(data_json) > 3 else len(data_json)
    # creating a list of nearby places
    places = [
        {
            '_id':place['place_id'],
            'name': place['name'],
            'coordinates': place['geometry']['location'],
            'types': place['types'],
            'geoJSON': {
                "type": "Point",
                "coordinates": [ place['geometry']['location']['lng'],place['geometry']['location']['lat'] ]
            }
        } for place in data_json[:i] 
    ]
    # storing it in mongoDB 
    try:
        mongo.db.searched_places.insert_many(places)
    except:
        pass