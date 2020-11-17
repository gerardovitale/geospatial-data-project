import json
import time
import urllib.error
import urllib.parse
import urllib.request
import os
from dotenv import load_dotenv

# Google Nearby Search API url:
BASE_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

def google_place(latitude, longitude, category, keyword):
    load_dotenv('../../../../geospatial-data-project/.env') # Load GGOLGE KEY from the .env
    GOOGLE_KEY = os.getenv("GOOGLE_KEY")
    # Set parameters
    params = urllib.parse.urlencode(
        {
            "location": f"{latitude},{longitude}",
            "key":GOOGLE_KEY,
            "keyword":keyword,
            "type":category,
            "rankby":"distance"
        }
    )

    url = f"{BASE_URL}?{params}"
    current_delay = 0.1  # Set the initial retry delay to 100ms.
    max_delay = 5  # Set the maximum retry delay to 5 seconds.
    
    while True:
        try:
            # Get the API response.
            response = urllib.request.urlopen(url)
        except urllib.error.URLError:
            pass  # Fall through to the retry loop.
        else:
            # If we didn't get an IOError then parse the result.
            result = json.load(response)

            if result["status"] == "OK":
                return result['results']
            elif result["status"] != "UNKNOWN_ERROR":
                # Many API errors cannot be fixed by a retry, e.g. INVALID_REQUEST or
                # ZERO_RESULTS. There is no point retrying these requests.
                raise Exception(result["error_message"])

        if current_delay > max_delay:
            raise Exception("Too many retry attempts.")
        
        print("Waiting", current_delay, "seconds before retrying.")

        time.sleep(current_delay)
        current_delay *= 2  # Increase the delay each time we retry.