import mongo_query_comp as mongo
import process_coordinates as pcoord

def search_place_app():
    f = mongo.filt
    p = mongo.project
    result = mongo.mongo_query_comp(f, p)
    pcoord.process_coordinates(result)

search_place_app()