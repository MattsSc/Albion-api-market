from albion_service import AlbionService

#Init Service
albionService = AlbionService()

items = input("Add item codes that you want to check prices (separated by comma): ").split(",")

print("Calculating....")

for result in albionService.get_best_price_for_items(items):
    print(result)


    

