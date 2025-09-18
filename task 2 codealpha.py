import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3300,
    "MSFT": 300
}

portfolio = {}
total_investment = 0

print("Welcome to Stock Portfolio Tracker")

# Let user input stocks and quantities
while True:
    stock = input("Enter stock symbol (AAPL, TSLA, GOOGL, AMZN, MSFT) or 'done' to finish: ").upper()
    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("Stock symbol not found. Please enter a valid one.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity <= 0:
            print("Quantity must be a positive integer.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Add to portfolio
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

# Calculate total investment
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares x ${price} = ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

# Save result to a CSV file
filename = "portfolio.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Price per Share", "Investment"])
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        investment = price * qty
        writer.writerow([stock, qty, price, investment])
    writer.writerow([])
    writer.writerow(["Total Investment", "", "", total_investment])

print(f"\nPortfolio saved to {filename}")
