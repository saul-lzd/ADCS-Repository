# Calculate the profit made for the given stock
# author: Saul DLD

stock = [{
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
}, {
    "cost_price": 225.89,
    "sell_price": 550.00,
    "inventory": 100
}, {
    "cost_price": 2.77,
    "sell_price": 7.95,
    "inventory": 8500
}, {
    "cost_price": 5.88,
    "sell_price": 9.20,
    "inventory": 200
}, {
    "cost_price": 85.90,
    "sell_price": 100,
    "inventory": 750
}, {
    "cost_price": 0.50,
    "sell_price": 3.50,
    "inventory": 10000
}, {
    "cost_price": 47.00,
    "sell_price": 48.00,
    "inventory": 840
}, {
    "cost_price": 1.20,
    "sell_price": 8.50,
    "inventory": 360
}, {
    "cost_price": 47.10,
    "sell_price": 55.50,
    "inventory": 140
}, {
    "cost_price": 2.50,
    "sell_price": 6.50,
    "inventory": 40
}]


def main():
    for item in stock:
        print_separator()
        print("Item: ", item)
        print("Profit: $", calc_profit(item))

    print_separator()


def calc_profit(item):
    cost = item['inventory'] * item['cost_price']
    sell = item['inventory'] * item['sell_price']
    return round(sell - cost)


def print_separator():
    print("-" * 70)


if __name__ == "__main__":
    main()
