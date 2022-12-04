
COINS = {}
URL_CRYPTO = "https://api.coincap.io/v2/assets/"


# transforms and store all information in dict "COINS"
def getallcoininfo(text):
    for item in text["data"]:
        COINS[item["name"]] = {"rank": item["rank"], "symbol": item["symbol"], "priceUsd": item["priceUsd"],
                               "marketCapUsd": item["marketCapUsd"], "maxSupply": item["maxSupply"], "supply": item["supply"],
                               "volumeUsd24Hr": item["volumeUsd24Hr"], "changePercent24Hr": item["changePercent24Hr"]}


# if input "coin" is on dict "COINS" print all info about the coin
def searchcoininfo(coin):
    if coin in COINS:
        print(f"COIN -> {coin} ({COINS[coin]['rank']})")
        print(f"SYMBOL -> {COINS[coin]['symbol']}")
        print(f"Price (USD) -> {COINS[coin]['priceUsd']}")
        print(f"marketCap (USD) -> {COINS[coin]['marketCapUsd']}")
        print(f"CHANGE%24H -> {COINS[coin]['changePercent24Hr']}")
        print(f"VOLUMEUSD24h -> {COINS[coin]['volumeUsd24Hr']}")
        print(f"SUPPLY-> {COINS[coin]['supply']}")
        print(f"MAXSUPPLY -> {COINS[coin]['maxSupply']}")
    else:
        print("Coin not found")


def cryptotable():
    print("|   {:<4}   |   {:<21}   |   {:<7}   |   {:<12}   |   {:<9}   |"
          .format("RANK", "NAME", "SYMBOL", "PRICE", "CHANGE%24H"))
    for item in COINS:  # for each item in COINS, print a line with lots of info
        print("|   {:<4}   |   {:<21}   |   {:<7}   |   {:<12.3f}   |   {:<9.3f}   |"
              .format(COINS[item]['rank'], item, COINS[item]['symbol'], float(COINS[item]['priceUsd']),
                      float(COINS[item]['changePercent24Hr'])))


def cryptomenu(cleartext):
    getallcoininfo(cleartext)  # transforms and store all information in dict "COINS"
    while True:
        print("=-=      Coincap API     =-=")
        print("1 - [Show] all coin names ")
        print("2 - [Search] coin info")
        print("3 - Coin [Table]")
        print("0 - [Exit]")
        print("=-=           -          =-=")
        option = input(": ").lower()
        match option:
            case "show" | "1":
                for item in COINS:
                    print(item)
            case "search" | "2":
                coin = input("Coin name: ")
                searchcoininfo(coin)
            case "table" | "3":
                cryptotable()
            case "exit" | "0":
                print("Goodbye")
                break
