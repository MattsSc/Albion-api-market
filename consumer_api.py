import requests

BASIC_LOCATIONS = "Caerleon,Bridgewatch,Martlock,Lymhurst,FortSterling,Thetford"
RUNES_CODES = "{0}_RUNE,{0}_SOUL,{0}_RELIC"
API_URL_BASE = "https://www.albion-online-data.com/api/v2"
URL_GET_PRICE = "/stats/prices/{}"

StringList = list[str]

class AlbionController:
    def get_items_price(item_codes : StringList):
        api_url = API_URL_BASE + URL_GET_PRICE.format(','.join(item_codes).strip())

        try:
            response = requests.get(api_url, params= {'qualities': '2', 'locations': BASIC_LOCATIONS})
            return response
        except requests.exceptions.RequestException as e:  
             raise SystemExit(e)


    def get_runes_price(tier: str):
        api_url = API_URL_BASE + URL_GET_PRICE.format(RUNES_CODES.format(tier))

        try:
            response = requests.get(api_url, params= {'qualities': '2', 'locations': BASIC_LOCATIONS})
            return response
        except requests.exceptions.RequestException as e:  
                raise SystemExit(e)