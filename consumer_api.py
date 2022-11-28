import requests

BASIC_LOCATIONS = "Caerleon,Bridgewatch,Martlock,Lymhurst,FortSterling,Thetford"
API_URL_BASE = "https://www.albion-online-data.com/api/v2"
URL_GET_PRICE = "/stats/prices/{}"

StringList = list[str]

class AlbionController:
    def get_items_price(item_codes : StringList):


        api_url = API_URL_BASE + URL_GET_PRICE.format(','.join(item_codes).strip())

        print(api_url)

        try:
            response = requests.get(api_url, params= {'qualities': '2', 'locations': BASIC_LOCATIONS})
            return response
        except requests.exceptions.RequestException as e:  
             raise SystemExit(e)
