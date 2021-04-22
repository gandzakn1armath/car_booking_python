from src.user.models_user import User, Data_manager
from tkinter import messagebox
from src.user.dialogs_user import Sign_up_label, User_page, Sign_in_dialog, Add_order, Show_booking_user
import json
import os
from datetime import datetime

selected_index = None
data_manager = Data_manager()
user = User()
sign: Sign_in_dialog
user_page: User_page
sign_up_label: Sign_up_label
add_order: Add_order


def sign_up():
    global sign_up_label
    try:
        sign.hide()
    except:
        pass
    sign_up_label = Sign_up_label()
    sign_up_label.show_dialog(show_sign_up_dialog)

def start_order_query(user_id, status):
    data_manager.startOrdersQueryUser(user_id, status, init_orders)


def start_finish_order_query(user_id, status):
    data_manager.startOrdersQueryUser(user_id, status, finish_orders)


def show_user_page(user,id):
    global sign_up_label, user_page
    user_page = User_page(user)
    start_order_query(id, ["PENDING", "STARTED"])
    start_finish_order_query(id, ["FINISHED"])
    try:
        sign_up_label.hide()
    except:
        pass
    user_page.show_dialog(start_query, seeOrder, exit_account)


def sign_in():
    if not (sign.get_phone() and sign.get_password()):
        messagebox.showerror("Ուշադրություն", "Հեռ․ համարը կամ գաղտնաբառը դատարկ է")
        return
    user_result = data_manager.check_user_name_and_pass(sign.get_phone(), sign.get_password())
    if not user_result:
        messagebox.showerror("Ուշադրություն", "Հեռ․ համարի կամ գաղտնաբառի սխալ")
        return
    file1 = open("../UserInfo.txt", "a+", encoding="utf-8")
    obj = json.dumps({'firstName': user_result["firstName"],
                      'lastName': user_result["lastName"],
                      'phoneNumber': user_result["phoneNumber"],
                      'password': user_result["password"],
                      'id': user_result["id"]
                      })
    file1.write(obj + " \n")
    file1.close()
    sign.hide()
    try:
        sign_up_label.hide()
    except:
        pass
    show_user_page(user_result,user_result["id"])

def sign_up_result(message, id):
    if message:

        file1 = open("../UserInfo.txt", "a+", encoding="utf-8")
        obj = json.dumps({'firstName': sign_up_label.get_first_name(),
                          'lastName': sign_up_label.get_last_name(),
                          'phoneNumber': sign_up_label.get_phone(),
                          'password': sign_up_label.get_password(),
                          'id': id
                          })
        file1.write(obj + " \n")
        file1.close()
        messagebox.showinfo("ՈՒշադրություն", "Դուք հաջողությամբ գրանցվեցիք")
        show_user_page(message, id)
    else:
        messagebox.showerror("ՈՒշադրություն", "Տեղի ունեցավ սխալ խնդրում ենք փորձել կրկին")

def show_sign_up_dialog():
    if not user.set_name(sign_up_label.get_first_name()):
        messagebox.showerror("Ուշադրություն", "Անվան սխալ ֆորմատ")
        return

    if not user.set_surname(sign_up_label.get_last_name()):
        messagebox.showerror("Ուշադրություն", "Ազգանունի սխալ ֆորմատ")
        return

    if not user.set_phone_number(sign_up_label.get_phone()):
        messagebox.showerror("Ուշադրություն", "Հեռախոսահամարի սխալ ֆորմատ")
        return
    if data_manager.is_phone_number_exist(sign_up_label.get_phone()):
        messagebox.showerror("Ուշադրություն", "Հեռախոսահամարի արդեն զբաղված է")
        return

    if not user.set_password(sign_up_label.get_password()):
        messagebox.showerror("Ուշադրություն",
                             "Գաղտնաբառը պետք է լինի 6 նիշից ավելի\n "
                             "Գաղտնաբառը պիտի պարունակի մեծատառ\n "
                             "Գաղտնաբառը պիտի պարունակի թիվ")
        return
    data_manager.save_data(user, sign_up_result)




def save_order_result(message):
    if message:
        messagebox.showinfo("ՈՒշադրություն", "Ձեր պատվերը հաջողությամբ ավելացվեց")
        add_order.hide()
        user_page.add_order(message)
    else:
        messagebox.showerror("ՈՒշադրություն", "Տեղի ունեցավ սխալ խնդրում ենք փորձել կրկին")


def save_order():
    file = open("../UserInfo.txt", "r", encoding="utf-8")
    array = file.readlines()
    user_data = array[0]
    first_name = json.loads(user_data)["firstName"]
    last_name = json.loads(user_data)["lastName"]
    phone_number = json.loads(user_data)["phoneNumber"]
    user_id = json.loads(user_data)["id"]
    pickup_address = add_order.get_pickup_address()
    service_address = "Gavar"
    status = "PENDING"
    if add_order.carListbox.curselection():
        selected_index = add_order.carListbox.curselection()[0]
        car = data_manager.cars_list[selected_index]
        brand = car["brand"]
        model = car["model"]
        price = car["price"]
        data_manager.saveOrderData(first_name,
                                   last_name,
                                   phone_number,
                                   user_id,
                                   pickup_address,
                                   service_address,
                                   status,
                                   brand,
                                   model,
                                   price,
                                   save_order_result)


def car_query_result(result):
    global add_order, user_page
    if result != "error":
        add_order = Add_order()
        add_order.init_cars(result)
        add_order.show_dialog(save_order)
    else:
        messagebox.showerror("Օօպս ինչ որ մի բան այնպես չգնաց, խնդրում ենք փորձել կրկին")


def first_start():
    global sign
    sign = Sign_in_dialog()
    sign.show_dialog(sign_up, sign_in)


def start_query():
    data_manager.start_cars_query(car_query_result)


def init_orders(result):
    if result != "error":
        user_page.init_new_orders(result)


def finish_orders(result):
    if result != "error":
        user_page.init_finish_orders(result)

def seeOrder():
    if user_page.new_order_list_box.curselection() or user_page.ended_order_list_box.curselection():
        order = {}
        if user_page.new_order_list_box.curselection():
            selected_index = user_page.new_order_list_box.curselection()[0]
            order = data_manager.userOrder[selected_index]
        if user_page.ended_order_list_box.curselection():
            selected_index = user_page.ended_order_list_box.curselection()[0]
            order = data_manager.finish_orders[selected_index]

        name = order["user_firstName"]
        surname = order["user_lastName"]
        phone = order["user_phoneNumber"]
        take_place = order["pickup_address"]
        deliver_place = order["service_address"]
        status = order["status"]
        brand = order["car_brand"]
        model = order["car_model"]
        price = order["car_price"]

        now = datetime.now()
        minute = 0
        if order["startDate"]:
            start_date = datetime.strptime(order["startDate"], '%Y-%m-%d %H:%M:%S')
            if status == "STARTED":
                minute = int((now - start_date).total_seconds() / 60)
            elif status == "FINISHED":
                end_date = datetime.strptime(order["endDate"], '%Y-%m-%d %H:%M:%S')
                minute = int((end_date - start_date).total_seconds() / 60)

        all_price = int(minute * (int(price) / 60))
        Show_booking_user(order["startDate"], order["endDate"],
                          name,
                          surname,
                          phone,
                          take_place,
                          deliver_place,
                          brand,
                          model,
                          price, str(all_price) + " դրամ", status) \
            .show_dialog()


def exit_account():
    try:
        os.remove("../UserInfo.txt")
    except:
        pass
    user_page.hide()
    first_start()




def second_start():
    global user_page
    file1 = open("../UserInfo.txt", "r", encoding="utf-8")
    array = file1.readlines()
    try:
        sign.hide()
    except:
        pass
    file1.close()
    data = json.loads(array[0])
    show_user_page(data,data["id"])


try:
    second_start()
except:
    first_start()
