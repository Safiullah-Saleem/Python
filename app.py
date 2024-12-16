import streamlit as st

# Inventory with product details
inventory = {
    1: {"id": 1, "name": "Laptop", "price": 60000, "stock": 5},
    2: {"id": 2, "name": "Smartphone", "price": 30000, "stock": 10},
    3: {"id": 3, "name": "Headphones", "price": 2000, "stock": 20},
    4: {"id": 4, "name": "Keyboard", "price": 1500, "stock": 15},
}

# Cart
cart = {"items": [], "total": 0}


# Display available products
def display_products():
    st.subheader("Available Products")
    for product in inventory.values():
        st.write(
            f"**{product['name']}** - Price: {product['price']} - Stock: {product['stock']}"
        )


# Add a product to the cart
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
        st.success(f"{product['name']} added to the cart successfully!")
    else:
        st.error("Product is out of stock or invalid ID.")


# View cart items
def view_cart():
    st.subheader("Cart Items")
    if cart["items"]:
        for item in cart["items"]:
            st.write(
                f"**{item['name']}** - Price: {item['price']} - Quantity: {item['quantity']} - Subtotal: {item['subtotal']}"
            )
        st.write(f"**Total: {cart['total']}**")
    else:
        st.warning("Your cart is empty.")


# Submit feedback
def submit_feedback():
    feedback = st.text_area("Enter your feedback:")
    if st.button("Submit Feedback"):
        st.success("Feedback submitted successfully!")
        st.write(f"**Your Feedback:** {feedback}")


# Main function
def main():
    st.title("E-Commerce Store")
    menu = ["View Products", "Add to Cart", "View Cart", "Submit Feedback"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "View Products":
        display_products()
    elif choice == "Add to Cart":
        display_products()
        product_id = st.number_input(
            "Enter the product ID to add to cart:", min_value=1, step=1
        )
        if st.button("Add to Cart"):
            add_to_cart(product_id)
    elif choice == "View Cart":
        view_cart()
    elif choice == "Submit Feedback":
        submit_feedback()


if __name__ == "__main__":
    main()
