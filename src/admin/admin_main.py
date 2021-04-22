from src.admin.dialogs_admin import Show_booking, Car_label, Booking_label
from tkinter import *
from tkinter import messagebox
from src.admin.models_admin import Data_manager
from datetime import datetime

is_save_btn_active = False
selected_index = None
data_manager = Data_manager()
car_label: Car_label
booking_label: Booking_label
show_booking: Show_booking
order_status = ""
order_id = ""


def started_and_finished():
    global show_booking, order_status, selected_index
    show_booking.hide()
    data_manager.update_status(selected_index, order_status)
    start_order_query()
    start_finish_order_query()


def show_order():
    global show_booking, selected_index, order_status
    if booking_label.new_order_list_box.curselection() or booking_label.ended_order_list_box.curselection():
        order = {}
        if booking_label.new_order_list_box.curselection():
            selected_index = booking_label.new_order_list_box.curselection()[0]
            order = data_manager.admin_order[selected_index]
        elif booking_label.ended_order_list_box.curselection():
            selected_index = booking_label.ended_order_list_box.curselection()[0]
            order = data_manager.admin_finish_order[selected_index]

        name = order["user_firstName"]
        surname = order["user_lastName"]
        phone = order["user_phoneNumber"]
        take_place = order["pickup_address"]
        deliver_place = order["service_address"]
        status = order["status"]
        order_status = status
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

        show_booking = Show_booking(order["startDate"], order["endDate"],
                                    name,
                                    surname,
                                    phone,
                                    take_place,
                                    deliver_place,
                                    brand,
                                    model,
                                    price, str(all_price) + " դրամ", status)
        show_booking.show_dialog(started_and_finished)
    else:
        messagebox.showerror("ՈՒշադրություն", "Դուք չեք ընտրել պատվերը")


def save_car_result(result):
    if result:
        car_label.add_car(result)
    else:
        messagebox.showerror("ՈՒշադրություն", "Պահպանման սխալ")


def create_car():
    data_manager.save_car_data(car_label.get_brand(), car_label.get_model(), car_label.get_price(), save_car_result)
    car_label.clear_brand()
    car_label.clear_model()
    car_label.clear_price()


def validation():
    if not data_manager.set_brand(car_label.get_brand()):
        messagebox.showerror("Ուշադրություն", "Մակնիշի սխալ ֆորմատ")
        return

    if not data_manager.set_model(car_label.get_model()):
        messagebox.showerror("Ուշադրություն", "Մոդելի սխալ ֆորմատ")
        return

    if not data_manager.set_price(car_label.get_price()):
        messagebox.showerror("Ուշադրություն", "Գնի սխալ ֆորմատ")
        return
    create_car()


def checkResult(result):
    if result == "error":
        car_label.add_car(result)
    else:
        messagebox.showerror("ՈՒշադրություն", "Այդ ավտոմեքենան գրանցված է")


def delete_car():
    selected = car_label.car_listbox.curselection()[0]
    data_manager.delete_car_by_index(selected)
    car_label.car_listbox.delete(ACTIVE)


def edit_car():
    global is_save_btn_active, selected_index
    if car_label.car_listbox.curselection():
        is_save_btn_active = True
        selected_index = car_label.car_listbox.curselection()[0]
        car_label.change_save_btn_name(True)
        car = data_manager.cars_list[selected_index]
        car_label.set_brand(car["brand"])
        car_label.set_model(car["model"])
        car_label.set_price(car["price"])


def result(result):
    if result == "car":
        data_manager.delete_car_by_index(selected_index)
        car_label.car_listbox.delete(ANCHOR)
        validation()


def save_change():
    global selected_index, is_save_btn_active
    item_text = data_manager.check_new_car(car_label.get_brand(), car_label.get_model(),
                                           car_label.get_price(), selected_index)
    car_label.update_car(item_text, selected_index)
    selected_index = None
    is_save_btn_active = False
    car_label.change_save_btn_name(False)
    car_label.clear_brand()
    car_label.clear_model()
    car_label.clear_price()


def change_add_to_save():
    if is_save_btn_active:
        save_change()
    else:
        validation()


def show_bookings():
    global booking_label
    booking_label = Booking_label()
    start_order_query()
    start_finish_order_query()
    booking_label.show_dialog(add_car, show_order)


def on_back():
    global car_label
    car_label.hide()
    show_bookings()


def car_query_result(result):
    global car_label, booking_label
    if result != "error":
        booking_label.hide()
        car_label = Car_label(change_add_to_save, edit_car, delete_car, on_back)
        car_label.init_cars(result)
    else:
        messagebox.showerror("Օօպս ինչ որ մի բան այնպես չգնաց, խնդրում ենք փորձել կրկին")


def add_car():
    data_manager.start_cars_query(car_query_result)


def init_orders(result):
    if result != "error":
        booking_label.init_new_orders(result)


def finish_orders(result):
    if result != "error":
        booking_label.init_finish_orders(result)


def start_order_query():
    data_manager.start_query_current_orders_admin(init_orders)


def start_finish_order_query():
    data_manager.start_query_finish_orders_admin(finish_orders)


show_bookings()
