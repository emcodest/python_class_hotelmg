from booking import get_room
# display mode of payment and total amount to pay
def calculate_rate(duration_in_days: int, name_of_room: str):
    for rm in get_room.room_list:
        if rm["name"] == name_of_room:
            total_pay = rm["price"] * duration_in_days
            return total_pay
    return -1

def collect_pay(days, name):
    # get rate to pay
    pay_price = calculate_rate(days, name)
    if pay_price == -1:
        raise Exception("Unable to get rate")
    print(f"Pay N{pay_price} now: ")
    amount_paid = input()
    if float(amount_paid) != float(pay_price):
         raise Exception("Invalid payment")