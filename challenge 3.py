# Items in cart and Total bill

products = [{"Name":"Laptop","Price":5000,},
            {"Name":"Iphone","Price":40000,},
            {"Name":"Headphones","Price":2000,}]
cart = []
while True:
    choice = input("Do you wish to continue shopping?")

    if choice=="yes":
        for index,item in enumerate(products):
            print(f"{index}.{item['Name']}:{item['Price']}")
        id = int(input("Enter index of the product you wish to add to cart"))

        if products[id] in cart:
                products[id]["quantity"]+=1
        else:
            products[id]["quantity"]=1
            cart.append(products[id])

        total = 0
        print("Your cart contains: ")
        for product in cart:
            print(f"Current cart is - {product['Name']}:{product['Price']}:{product['quantity']}")
            total = total + int(product['Price']*product['quantity'])
        print(f"Total bill: Rs.{total}")

    else:
        print("Thank you for shopping.")
        break