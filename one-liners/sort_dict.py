item_prices = {'vaseline':9.99,'tea':0.20,'apples':0.50}
sorted_items = {key: item_prices[key] for key in sorted(item_prices.keys())}
print(sorted_items)

population = {'meru':700,"nairobi":1000,"turkana":250}
print(sorted(population.items(),key=lambda x:x[1]))