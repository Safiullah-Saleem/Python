# Inventory with product details
inventory = {
    1: {"id": 1, "name": "Laptop", "price": 60000, "stock": 5},
    2: {"id": 2, "name": "Smartphone", "price": 30000, "stock": 10},
    3: {"id": 3, "name": "Headphones", "price": 2000, "stock": 20},
    4: {"id": 4, "name": "Keyboard", "price": 1500, "stock": 15},
}

# Cart
cart = {"items": [], "total": 0}


def display_products():
    print("Available Products:")
    for product in inventory.values():
        print(
            f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Stock: {product['stock']}"
        )


def add_to_cart(product_id):
    product = inventory.get(product_id)
    if product and product["stock"] > 0:
        product["stock"] -= 1
        for item in cart["items"]:
            if item["id"] == product_id:
                item["quantity"] += 1
                item["subtotal"] += product["price"]
                cart["total"] += product["price"]
                break
        else:
            cart["items"].append(
                {
                    "id": product_id,
                    "name": product["name"],
                    "price": product["price"],
                    "quantity": 1,
                    "subtotal": product["price"],
                }
            )
            cart["total"] += product["price"]
        print("Product added to cart successfully!")
    else:
        print("Product is out of stock or invalid ID.")


def view_cart():
    print("Cart Items:")
    if cart["items"]:
        for item in cart["items"]:
            print(
                f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}, Subtotal: {item['subtotal']}"
            )
        print(f"Total: {cart['total']}")
    else:
        print("Cart is empty.")


def submit_feedback():
    feedback = input("Enter your feedback: ")
    print(f"Feedback received: {feedback}")
    print("Feedback submitted successfully!")


def main():
    while True:
        print("\n1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Submit Feedback")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_products()
        elif choice == "2":
            product_id = int(input("Enter the product ID to add to cart: "))
            add_to_cart(product_id)
        elif choice == "3":
            view_cart()
        elif choice == "4":
            submit_feedback()
        elif choice == "5":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
