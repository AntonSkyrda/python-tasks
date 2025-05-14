orders = {}


def add_order(
        order_number: int,
        product_name: str,
        quantity: int,
) -> None:
    if order_number not in orders.keys():
        orders[order_number] = {
            "product_name": product_name,
            "quantity": quantity,
        }
    else:
        print("Order number is exists")


def print_orders(order_number_in: int = None) -> None:
    if order_number_in is None:
        print(orders)
        return
    try:
        print(orders[order_number_in])
    except KeyError:
        print(f"Order with number {order_number_in} does not exist")


add_order(1, "Apple", 24)
add_order(2, "Banana", 24)
# print_orders(1)
# print_orders()
print_orders(4)
