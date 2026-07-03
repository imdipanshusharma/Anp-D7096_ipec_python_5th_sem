# Create an empty list
products = []

# Input details of 10 products
for i in range(10):
    print(f"\nEnter details of Product {i+1}")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    products.append((name, price))

# Convert list to tuple
products = tuple(products)

# Find lowest and highest priced products
lowest = products[0]
highest = products[0]

count = 0

for product in products:
    if product[1] < lowest[1]:
        lowest = product
    if product[1] > highest[1]:
        highest = product
    if product[1] > 4000:
        count += 1

# Display results
print("\nLowest Priced Product:")
print("Name:", lowest[0], "Price:", lowest[1])

print("\nHighest Priced Product:")
print("Name:", highest[0], "Price:", highest[1])

print("\nNumber of products with price greater than 4000:", count)


'''Enter details of Product 1
Enter product name: samsung S23
Enter product price: 78000

Enter details of Product 2
Enter product name: iqoo
Enter product price: 12000

Enter details of Product 3
Enter product name: vivo
Enter product price: 36000

Enter details of Product 4
Enter product name: iphone 13
Enter product price: 36000

Enter details of Product 5
Enter product name: redmi
Enter product price: 3200

Enter details of Product 6
Enter product name: lenovo 
Enter product price: 36000

Enter details of Product 7
Enter product name: ipad
Enter product price: 25000

Enter details of Product 8
Enter product name: display 
Enter product price: 3600

Enter details of Product 9
Enter product name: samsung s25 ultra
Enter product price: 123000

Enter details of Product 10
Enter product name: vivo v33
Enter product price: 23000

Lowest Priced Product:
Name: redmi Price: 3200.0

Highest Priced Product:
Name: samsung s25 ultra Price: 123000.0

Number of products with price greater than 4000: 8'''