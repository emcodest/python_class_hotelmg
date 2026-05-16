from customer import collect_info
from booking import get_room
from checking import hotel_record

start_app = True
while(start_app):
    start_app = False
    # collect customer info
    info_data = collect_info.show_info()
    try:
        # allow customer to choose room and  collect payment
        ndays = int(info_data["days"])
        c_name = info_data["name"]
        booking_data = get_room.display(ndays, c_name)
        # check in customer
        hotel_record.add_record(booking_data)
        # exit app or continue
        print("Do you want to exit ? YES or NO")
        ex_app = input()
        if ex_app == "YES":
            start_app = True
        else:
            start_app= False
    except Exception as ex:
        print("Something went wrong", ex)