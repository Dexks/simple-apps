
FRUIT = {}
URL_FRUIT = "https://www.fruityvice.com/api/fruit/all"


# transforms and store all information in dict "FRUIT"
def getallfruitinfo(text):
    for item in text:
        FRUIT[item["name"]] = {"genus": item["genus"], "fid": item["id"], "family": item["family"],
                               "order": item["order"], "nutritions": item["nutritions"]}


# if input "fruit" is on dict "FRUIT" print all info about the fruit
def searchfruitinfo(fruit):
    if fruit in FRUIT:
        print(f"Fruit -> {fruit} ({FRUIT[fruit]['fid']})")
        print(f"Genus - {FRUIT[fruit]['genus']}")
        print(f"Family - {FRUIT[fruit]['family']}")
        print(f"Order - {FRUIT[fruit]['order']}")
        print(f"Nutritions:")
        print(f"Carbohydrates - {FRUIT[fruit]['nutritions']['carbohydrates']}")
        print(f"Protein - {FRUIT[fruit]['nutritions']['protein']}")
        print(f"Fat - {FRUIT[fruit]['nutritions']['fat']}")
        print(f"Calories - {FRUIT[fruit]['nutritions']['calories']}")
        print(f"Sugar - {FRUIT[fruit]['nutritions']['sugar']}")
    else:
        print("Fruit not found")


def fruittable():
    print("|   {:<2}   |   {:<16}   |   {:<16}   |   {:<16}   |   {:<16}   |".format("ID", "FRUIT", "GENUS", "FAMILY", "ORDER"))
    for item in FRUIT:  # for each item in FRUIT, print a line with fruit info
        print("|   {:<2}   |   {:<16}   |   {:<16}   |   {:<16}   |   {:<16}   |"
              .format(FRUIT[item]['fid'], item, FRUIT[item]['genus'], FRUIT[item]['family'], FRUIT[item]['order']))


def fruitmenu(cleartext):
    getallfruitinfo(cleartext)  # transforms and store all information in dict "FRUIT"
    while True:
        print("=-=    Fruityvice API    =-=")
        print("1 - [Show] all fruit names ")
        print("2 - [Search] fruit info")
        print("3 - Fruit [Table]")
        print("0 - [Exit]")
        print("=-=          -           =-=")
        option = input(": ").lower()
        match option:
            case "show" | "1":
                for item in FRUIT:
                    print(item)
            case "search" | "2":
                fruitname = input("Fruit name: ")
                searchfruitinfo(fruitname)
            case "table" | "3":
                fruittable()
            case "exit" | "0":
                print("Goodbye")
                break
