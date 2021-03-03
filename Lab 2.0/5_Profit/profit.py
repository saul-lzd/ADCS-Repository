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
    "cost_price": 2.77,
    "sell_price": 7.95,
    "inventory": 8500
}, {
    "cost_price": 2.77,
    "sell_price": 7.95,
    "inventory": 8500
}, {
    "cost_price": 2.77,
    "sell_price": 7.95,
    "inventory": 8500
}, {
    "cost_price": 2.77,
    "sell_price": 7.95,
    "inventory": 8500
}, {
    "cost_price": 2.77,
    "sell_price": 7.95,
    "inventory": 8500
}, {
    "cost_price": 2.77,
    "sell_price": 7.95,
    "inventory": 8500
}, {
    "cost_price": 2.77,
    "sell_price": 7.95,
    "inventory": 8500
}]


def main():
    for item in stock:
        print_separator()
        print("Item: ", item)
        print("Profit: ", calc_profit(item))

    print_separator()


def calc_profit(item):
    cost = item['inventory'] * item['cost_price']
    sell = item['inventory'] * item['sell_price']
    return round(sell - cost)


def print_separator():
    print("-" * 70)


if __name__ == "__main__":
    main()
