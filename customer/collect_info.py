# collect name, phone and stay duration



def show_info():
    print("Enter Name: ")
    name = input()
    print("Enter Phone: ")
    phone = input()
    print("How many days ?: ")
    days = input()
    return {"name": name, "phone": phone, "days": days}
