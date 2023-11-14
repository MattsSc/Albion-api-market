from consumer_api import AlbionController
from ItemPriceEvaluated import ItemPriceEvaluated

StringList = list[str]

class AlbionService:
    def __init__(self):
        print("Service instanciated")

    def get_best_price_for_items(self, item_codes : StringList):
        try:
            item_codes_stripped = [s.strip() for s in item_codes]
            response = AlbionController.get_items_price(item_codes_stripped)

            results = []

            for item in item_codes_stripped:
                results.append(self.__create_item_price_evaluated(item, response))

            return results
        except Exception as e:
            print("Something weird happened")
            raise SystemExit(e)


    def __create_item_price_evaluated(self, item_name: str, response):
        itemPriceEvaluated = ItemPriceEvaluated()
        itemPriceEvaluated.name = item_name
        itemPriceEvaluated.caerleon = 0
        itemPriceEvaluated.city = None
        itemPriceEvaluated.bestPrice = 0
        itemPriceEvaluated.profit = 0
        for priceInfo in response.json():
            if priceInfo['item_id'] == item_name:
                if priceInfo['city'] == "Caerleon":
                    itemPriceEvaluated.caerleon = priceInfo['sell_price_min']
                elif itemPriceEvaluated.bestPrice == 0 or (itemPriceEvaluated.bestPrice > priceInfo['sell_price_min'] and priceInfo['sell_price_min'] != 0):
                    itemPriceEvaluated.bestPrice = priceInfo['sell_price_min']
                    itemPriceEvaluated.city = priceInfo['city']

        return itemPriceEvaluated
