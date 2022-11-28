from consumer_api import AlbionController
from ItemPriceEvaluated import ItemPriceEvaluated

items = input("Add item codes that you want to check prices (separated by comma): ").split(",")

for item in items:
    item = item.strip()

json_response = AlbionController.get_items_price(items)

print("Calculating....")

results = []

for item in items:
    item = item.strip()
    itemPriceEvaluated = ItemPriceEvaluated()
    itemPriceEvaluated.name = item
    itemPriceEvaluated.caerleon = 0
    itemPriceEvaluated.city = None
    itemPriceEvaluated.bestPrice = 0
    itemPriceEvaluated.profit = 0
    for priceInfo in json_response.json():
        if priceInfo['item_id'] == item:
            minPrice = 0
            if priceInfo['city'] == "Caerleon":
                itemPriceEvaluated.caerleon = priceInfo['sell_price_min']
            elif itemPriceEvaluated.bestPrice == 0 or itemPriceEvaluated.bestPrice > priceInfo['sell_price_min']:
                itemPriceEvaluated.bestPrice = priceInfo['sell_price_min']
                itemPriceEvaluated.city = priceInfo['city']
                itemPriceEvaluated.profit = itemPriceEvaluated.caerleon - (itemPriceEvaluated.bestPrice * 1.03)
    print(itemPriceEvaluated.print())

