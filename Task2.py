prices = [500, 1200, 800, 2500, 300]

def apply_discount(price, discount=10):
    final_price = price - (price * discount / 100)
    return final_price

print("Discount 10%:", apply_discount(1000))
print("Discount 25%:", apply_discount(1000, 25))


def total(*args):
    return sum(args)

print("Total:", total(5, 10, 15))


def describe(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


above_1000 = [price for price in prices if price > 1000]
print("\nAbove 1000:", above_1000)

with_gst = list(map(lambda price: round(price * 1.18, 2), prices))
print("With GST:", with_gst)

below_1000 = list(filter(lambda price: price < 1000, prices))
print("Below 1000:", below_1000)

total_sales = 0
i = 0

while i < len(prices):
    total_sales += prices[i]
    i += 1

print("While loop total:", total_sales)