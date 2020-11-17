import properties.client as mongo

filt = {
    'ipo.valuation_amount':{'$gte':1_000_000},
    'offices.city':'San Francisco'
}
project = {
    '_id':0,
    'offices.latitude':1,
    'offices.longitude':1
}

def mongo_query_comp(filt, project):
    res = mongo.db.companies_unwinded.find(filt, project)
    return [ coord['offices'] for coord in res ]