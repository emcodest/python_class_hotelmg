from payment import collect_payment

# display the available room name, price, collect duration and send to payment module
room_list = [
    {"name": "Standard", "price": 20000, "total": 100, "code": 1},
    {"name": "Delux", "price": 30000, "total": 20, "code": 2}
]

def display(days: int, cname: str):
    for room in room_list:
        print(f"Room: {room['name']}")
    print("Choose name: ")
    name = input()
    # make payment
    collect_payment.collect_pay(days, name)
    # successful payment lets check u in
    my_data = {"room_name": room['name'], "customer_name": cname, "days": days}
    return my_data




        





