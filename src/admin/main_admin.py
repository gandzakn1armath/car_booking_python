from tkinter import *           #Ներմուծում ենք գրադարանները
from tkinter import messagebox
from datetime import datetime
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
import re
from firebase import firebase
import ctypes
user32 = ctypes.windll.user32

class Design:#Ադմինի դիզայն կլաս
    def __init__(self):
        self.pc_width = int(user32.GetSystemMetrics(0))
        self.pc_height = int(user32.GetSystemMetrics(1))
        self.car_label_tk_width = 1000
        self.car_label_tk_height = 500
        self.booking_label_tk_width = 631
        self.booking_label_tk_height = 450
        self.show_booking_tk_width = 350
        self.show_booking_tk_height = 600
        self.fg_label = 'black'
        self.bg = 'silver'
        self.bg_button = 'light gray'
        self.frame_for_design = 'black'
        self.font = 'century 12 bold'
        self.font_show_booking = 'century 12'

    def get_show_booking_geometry(self):
        return str(self.show_booking_tk_width) + "x" + str(self.show_booking_tk_height) + "+" + str(
            int((self.pc_width - self.show_booking_tk_width) / 2)) + "+" + str(
            int((self.pc_height - self.show_booking_tk_height) / 2))

    def get_booking_label_geometry(self):
        return str(self.booking_label_tk_width) + "x" + str(self.booking_label_tk_height) + "+" + str(
            int((self.pc_width - self.booking_label_tk_width) / 2)) + "+" + str(
            int((self.pc_height - self.booking_label_tk_height) / 2))

    def get_car_label_geometry(self):
        return str(self.car_label_tk_width) + "x" + str(self.car_label_tk_height) + "+" + str(
            int((self.pc_width - self.car_label_tk_width) / 2)) + "+" + str(
            int((self.pc_height - self.car_label_tk_height) / 2))

design = Design()


class Show_booking: #Պատվերի ցույց տալու կլաս
    def __init__(self,
                 start_date,
                 end_date,
                 name,
                 surname,
                 phone_number,
                 take_place,
                 delivery_place,
                 brand,
                 model,
                 price_hour,
                 total_price,
                 status):
        self.orderStatus = status
        self.tk = Tk()
        self.tk.resizable(False, False)
        self.tk.geometry(design.get_show_booking_geometry())
        self.frame = Frame(self.tk, width=design.pc_width, height=design.pc_height, bg=design.bg).pack()
        self.start_time = Label(self.tk, text="Սկիզբ", font=design.font_show_booking, fg='white', bg=design.bg) \
            .place(x=50, y=0)
        self.start = Label(self.tk, text=start_date, font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=20, y=50)
        self.finish_time = Label(self.tk, text="Ավարտ", font=design.font_show_booking, fg='white', bg=design.bg) \
            .place(x=225, y=0)
        self.end = Label(self.tk, text=end_date, font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=205, y=50)
        self.first_name = Label(self.tk, text="Անուն", font=design.font_show_booking, fg='white', bg=design.bg) \
            .place(x=0, y=100)
        self.name = Label(self.tk, text=name, font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=150, y=100)
        self.lastName = Label(self.tk, text="Ազգանուն", font=design.font_show_booking, fg='white', bg=design.bg) \
            .place(x=0, y=150)
        self.surname = Label(self.tk, text=surname, font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=150, y=150)
        self.phoneNumber = Label(self.tk, text="Հեռ․ համար", font=design.font_show_booking, fg='white', bg=design.bg) \
            .place(x=0, y=200)
        self.phone_number = Label(self.tk, text=phone_number, font=design.font, fg=design.fg_label,
                                  bg=design.bg).place(x=150, y=200)
        self.getAddress = Label(self.tk, text="Վերցնելու Վայրը", font=design.font_show_booking, fg='white',
                                bg=design.bg).place(x=0, y=250)
        self.takeAddress = Label(self.tk, text=take_place, font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=0, y=300)
        self.giveAddress = Label(self.tk, text="Հանձնելու Վայրը", font=design.font_show_booking, fg='white',
                                 bg=design.bg).place(x=175, y=250)
        self.deliveryAddress = Label(self.tk, text=delivery_place, font=design.font, fg=design.fg_label,
                                     bg=design.bg).place(x=175, y=300)
        self.brand = Label(self.tk, text="Մակնիշ", font=design.font_show_booking, fg='white', bg=design.bg) \
            .place(x=0, y=350)
        self.brand1 = Label(self.tk, text=brand, font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=0, y=400)
        self.model = Label(self.tk, text="Մոդել", font=design.font_show_booking, fg='white', bg=design.bg) \
            .place(x=125, y=350)
        self.model1 = Label(self.tk, text=model, font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=110, y=400)
        self.price = Label(self.tk, text="Արժեքը/ժ", font=design.font_show_booking, fg='white', bg=design.bg) \
            .place(x=250, y=350)
        self.price1 = Label(self.tk, text=price_hour, font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=260, y=400)
        self.totalPrice = Label(self.tk, text="Ընդհանուր Գումար", font=design.font_show_booking, fg='white',
                                bg=design.bg).place(x=0, y=450)
        self.finalPrice = Label(self.tk, text=total_price, font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=170, y=450)
        self.statusLabel = Label(self.tk, text="Պատվերի Վիճակ", font=design.font_show_booking, fg='white',
                                 bg=design.bg).place(x=0, y=500)
        self.status = Label(self.tk, text=status, font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=150, y=500)
        self.close = Button(self.tk, text="Փակել", width=15, height=2, bg=design.bg_button, command=self.hide).place(
            x=50,
            y=550)

    def hide(self):#Թաքցնել պատուհանը
        self.tk.destroy()

    def show_dialog(self, started):#Ցույց տալ պատուհանը
        if self.orderStatus == "PENDING":
            self.start = Button(self.tk, text="Սկսել", width=15, height=2, bg=design.bg_button,
                                command=started)
            self.start.place(x=180, y=550)
        elif self.orderStatus == "STARTED":
            self.start = Button(self.tk, text="Ավարտել", width=15, height=2, bg=design.bg_button,
                                command=started)
            self.start.place(x=180, y=550)

        self.tk.mainloop()


class Car_label:#Ավտոմեքենաների կլասը
    def __init__(self, add_car, edit, delete_selected, back):
        entry_x = 100
        entry_width = 20
        self.tk = Tk()
        self.tk.resizable(False, False)
        self.tk.geometry(design.get_car_label_geometry())
        self.frame = Frame(self.tk, width=design.pc_width, height=design.pc_height, bg=design.bg).pack()
        self.blackFrame = Frame(self.tk, width=700, height=410, bg=design.frame_for_design).place(x=307, y=0)
        self.brandLabel = Label(self.tk, text="Մակնիշ", font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=0, y=50)
        self.modelLabel = Label(self.tk, text="Մոդել", font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=0, y=100)
        self.priceLabel = Label(self.tk, text="Արժեք Դ/Ժ", font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=0, y=150)
        self.brandEt = StringVar()
        Entry(self.tk, width=entry_width, textvariable=self.brandEt).place(x=entry_x, y=58)
        self.modelEt = StringVar()
        Entry(self.tk, width=entry_width, textvariable=self.modelEt).place(x=entry_x, y=108)
        self.priceEt = StringVar()
        Entry(self.tk, width=entry_width, textvariable=self.priceEt).place(x=entry_x, y=158)
        self.addBtnName = StringVar(value=str("Ավելացնել"))
        self.add = Button(self.tk, textvariable=self.addBtnName, width=25, height=2, bg=design.bg_button,
                          command=add_car).place(x=100, y=450)
        self.editBtn = Button(self.tk, text="Փոփոխել", width=25, height=2, bg=design.bg_button, command=edit) \
            .place(x=400, y=450)
        self.delete = Button(self.tk, text="Ջնջել", width=25, height=2, bg=design.bg_button,
                             command=delete_selected).place(x=700, y=450)

        self.back = Button(self.tk, text="Հետ գնալ", width=10, height=2, bg=design.bg_button,
                           command=back).place(x=10, y=450)
        self.car_listbox = Listbox(self.tk, exportselection=0, height=25, width=113)
        self.car_listbox.place(x=315, y=0)

    def show_dialog(self):#Ցույց տալ պատուհանը
        self.tk.mainloop()

    def init_cars(self, cars: list):
        try:
            self.car_listbox.delete(0, END)
        except:
            pass
        self.cars = cars
        index = 0
        if not self.cars:
            return
        for item in self.cars:
            index += 1
            self.car_listbox.insert(index, item)

    def get_brand(self):
        return self.brandEt.get()

    def get_model(self):
        return self.modelEt.get()

    def set_brand(self, brand):
        self.brandEt.set(brand)

    def set_model(self, model):
        self.modelEt.set(model)

    def set_price(self, price):
        self.priceEt.set(price)

    def get_price(self):
        return self.priceEt.get()

    def clear_brand(self):
        self.brandEt.set("")

    def clear_model(self):
        self.modelEt.set("")

    def clear_price(self):
        self.priceEt.set("")

    def add_car(self, car):
        self.cars.append(car)
        self.car_listbox.insert(END, car)

    def update_car(self, car, select_index):
        self.cars[select_index] = car
        self.car_listbox.delete(select_index)
        self.car_listbox.insert(select_index, car)

    def change_save_btn_name(self, is_save):
        if is_save:
            self.addBtnName.set("Պահպանել")
        else:
            self.addBtnName.set("Ավելացնել")

    def hide(self):#Թաքցնել պատուհանը
        self.tk.destroy()


class Booking_label:#Պատվերների կլաս
    def __init__(self):
        self.tk = Tk()
        self.tk.resizable(False, False)
        self.tk.geometry(design.get_booking_label_geometry())
        self.frame = Frame(self.tk, width=design.pc_width, height=design.pc_height, bg=design.bg).pack()
        self.blackFrame = Frame(self.tk, width=320, height=333, bg=design.frame_for_design).place(x=0, y=45)
        self.blackFrame2 = Frame(self.tk, width=315, height=333, bg=design.frame_for_design).place(x=317, y=45)
        self.newOrders = Label(self.tk, text="Նոր պատվերներ", font=design.font, fg=design.fg_label,
                               bg=design.bg).place(x=75, y=0)
        self.new_order_list_box = Listbox(self.tk, height=20, width=50)
        self.new_order_list_box.place(x=7, y=50)
        self.endedOrders = Label(self.tk, text="Ավարտված պատվերներ", font=design.font, fg=design.fg_label,
                                 bg=design.bg).place(x=370, y=0)
        self.ended_order_list_box = Listbox(self.tk, height=20, width=50)
        self.ended_order_list_box.place(x=323, y=50)

    def show_dialog(self, add_button, show_item):#Ցույց nտալ պատուհանը
        add_car = Button(self.tk, text="Ավելացնել\nավտոմեքենա", width=15, height=2, bg=design.bg_button,
                         command=add_button)
        add_car.place(x=100, y=400)
        show_order = Button(self.tk, text="Ցույց\nտալ", width=15, height=2, bg=design.bg_button, command=show_item)
        show_order.place(x=415, y=400)
        self.tk.mainloop()

    def init_new_orders(self, new_order_list):
        try:
            self.new_order_list = []
            self.new_order_list_box.delete(0, END)
        except:
            pass
        self.new_order_list = new_order_list
        index = 0
        for item in new_order_list:
            self.new_order_list_box.insert(index, item)
            index += 1

    def init_finish_orders(self, finish_order_list):
        try:
            self.finish_order_list = []
            self.ended_order_list_box.delete(0, END)
        except:
            pass
        self.finish_order_list = finish_order_list
        index = 0
        for item in finish_order_list:
            self.ended_order_list_box.insert(index, item)
            index += 1

    def hide(self):#Թաքցնել պատուհանը
        self.tk.destroy()

class Data_manager:#Տվյալները ստացող, օգտագործոց կլաս
    def __init__(self):
        self.cars_list = []
        self.carIds = []
        self.carNames = []
        self.userTextList = []
        self.userFinishTextList = []
        self.finish_orders = []
        self.adminTextList = []
        self.admin_order = []
        self.adminFinishTextList = []
        self.admin_finish_order = []
        self.userOrder = []
        self.orderIds = []
        self.finishOrderIds = []
        self.firebase = firebase.FirebaseApplication("https://carbooking-cfd78.firebaseio.com/", None)

    def set_brand(self, brand):
        if not brand.strip().replace(" ", ""):
            return False
        if len(brand) == 1:
            return False
        return True

    def set_model(self, model):
        if not model.strip().replace(" ", ""):
            return False
        if len(model) == 1:
            return False
        return True

    def set_price(self, price):
        if not price.strip().replace(" ", ""):
            return False
        if len(price) == 1:
            return False
        return True

    def save_car_data(self, brand, model, price, saveCarResult):
        self.saveCarResult = saveCarResult
        self.carData = {
            'brand': brand,
            'model': model,
            'price': price
        }
        self.saveCar()

    def saveCar(self):
        try:
            resultCar = self.firebase.post('/Car', self.carData)
            id = resultCar["name"]
            brand = self.carData["brand"]
            model = self.carData["model"]
            price = self.carData["price"]
            itemText = brand + " " + model + " " + price + "դ/ժ "
            self.carIds.append(id)
            self.carNames.append(itemText)
            self.cars_list.append(self.carData)
            self.saveCarResult(itemText)
        except:
            self.saveCarResult(None)
    def update_status(self, index, status):
        if status == "PENDING":
            now = datetime.now()
            # dd/mm/YY H:M:S
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            order = self.admin_order[index]
            order["startDate"] = dt_string
            order["status"] = "STARTED"
            self.firebase.put('Order', self.orderIds[index], order)
        elif status == "STARTED":
            now = datetime.now()
            # dd/mm/YY H:M:S
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            order = self.admin_order[index]
            order["endDate"] = dt_string
            order["status"] = "FINISHED"
            self.firebase.put('Order', self.orderIds[index], order)

    def delete_car_by_index(self, position):
        id = self.carIds[position]
        print(id)
        self.firebase.delete('/Car', id)
        del self.cars_list[position]
        del self.carIds[position]
        del self.carNames[position]
    def check_new_car(self, brand, model, price, selectIndex):
        id = self.carIds[selectIndex]
        self.carData = {
            'brand': brand,
            'model': model,
            'price': price
        }
        itemText = brand + " " + model + " " + price + "դ/ժ"
        self.carNames[selectIndex] = itemText
        self.cars_list[selectIndex] = self.carData
        self.firebase.put('/Car', id, self.carData)
        return itemText

    def start_cars_query(self, carQueryResult):
        self.carQueryResult = carQueryResult
        self.queryCars()

    def queryCars(self):
        try:
            self.cars = self.firebase.get('/Car', None)
            self.cars_list = []
            self.carIds = []
            self.carNames = []
            if not self.cars:
                self.carQueryResult(self.carNames)
                return

            for objectId in self.cars:
                car = self.cars[objectId]
                self.brand = car["brand"]
                self.model = car["model"]
                self.price = car["price"]
                itemText = self.brand + " " + self.model + " " + self.price + "դ/ժ"
                self.carIds.append(objectId)
                self.carNames.append(itemText)
                self.cars_list.append(car)
            self.carQueryResult(self.carNames)
        except:
            self.carQueryResult("error")

    def start_query_current_orders_admin(self, orderQueryResult):
        try:
            self.orders = self.firebase.get('/Order', None)
            self.adminTextList = []
            self.admin_order = []
            self.orderIds = []
            if not self.orders:
                orderQueryResult("error")
                return

            for objectId in self.orders:
                order = self.orders[objectId]
                firstName = order["user_firstName"]
                lastName = order["user_lastName"]
                phoneNumber = order["user_phoneNumber"]
                takePlace = order["pickup_address"]
                deliverPlace = order["service_address"]
                status = order["status"]
                brand = order["car_brand"]
                model = order["car_model"]
                price = order["car_price"]
                if status == "PENDING" or status == "STARTED":
                    adminText = firstName + "  " + lastName + ", " + brand + ", " + takePlace + ", " + status
                    self.adminTextList.append(adminText)
                    self.admin_order.append(order)
                    self.orderIds.append(objectId)
            orderQueryResult(self.adminTextList)
        except:
            orderQueryResult("error")

    def start_query_finish_orders_admin(self, orderQueryResult):
        try:
            self.orders = self.firebase.get('/Order', None)
            self.adminFinishTextList = []
            self.admin_finish_order = []
            self.finishOrderIds = []
            if not self.orders:
                orderQueryResult("error")
                return

            for objectId in self.orders:
                order = self.orders[objectId]
                firstName = order["user_firstName"]
                lastName = order["user_lastName"]
                phoneNumber = order["user_phoneNumber"]
                takePlace = order["pickup_address"]
                deliverPlace = order["service_address"]
                status = order["status"]
                brand = order["car_brand"]
                model = order["car_model"]
                price = order["car_price"]
                if status == "FINISHED":
                    adminText = firstName + "  " + lastName + ", " + brand + ", " + takePlace + ", " + status
                    self.adminFinishTextList.append(adminText)
                    self.admin_finish_order.append(order)
                    self.finishOrderIds.append(objectId)
            orderQueryResult(self.adminFinishTextList)
        except:
            orderQueryResult("error")



#Ստեղծում ենք կլասների օբյեկտները
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


def show_order():#Ցույց տալ պատվերները
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


def save_car_result(result):#Ավտոմեքենաների պահպանման արդյունքը
    if result:
        car_label.add_car(result)
    else:
        messagebox.showerror("ՈՒշադրություն", "Պահպանման սխալ")


def create_car():#Ավտոմեքենաների ստեղծում
    data_manager.save_car_data(car_label.get_brand(), car_label.get_model(), car_label.get_price(), save_car_result)
    car_label.clear_brand()
    car_label.clear_model()
    car_label.clear_price()


def validation():#Ավտոմեքենաների վալիդացիա
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


def checkResult(result):#Ավտոմեքենաների ավելացման ստուգում
    if result == "error":
        car_label.add_car(result)
    else:
        messagebox.showerror("ՈՒշադրություն", "Այդ ավտոմեքենան գրանցված է")


def delete_car():#Ավտոմեքենաների ջնջում
    selected = car_label.car_listbox.curselection()[0]
    data_manager.delete_car_by_index(selected)
    car_label.car_listbox.delete(ACTIVE)


def edit_car():#Ավտոմեքենաների փոփոխում
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


def save_change():#Փոփոխության պահպանում
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


def change_add_to_save():#Ավելացում կոճակի փոփոխումը Պահպանել կոճակի
    if is_save_btn_active:
        save_change()
    else:
        validation()


def show_bookings():#Ցույց տալ պատվերները
    global booking_label
    booking_label = Booking_label()
    start_order_query()
    start_finish_order_query()
    booking_label.show_dialog(add_car, show_order)


def on_back():#Հետ գնալ
    global car_label
    car_label.hide()
    show_bookings()


def car_query_result(result):#Ավտոմեքենաների հավաքման արդյունքը
    global car_label, booking_label
    if result != "error":
        booking_label.hide()
        car_label = Car_label(change_add_to_save, edit_car, delete_car, on_back)
        car_label.init_cars(result)
    else:
        messagebox.showerror("Օօպս ինչ որ մի բան այնպես չգնաց, խնդրում ենք փորձել կրկին")


def add_car():#Ավտոմեքենաների ավելացում
    data_manager.start_cars_query(car_query_result)


def init_orders(result):#Պատվերների ինիցիալիզացիա
    if result != "error":
        booking_label.init_new_orders(result)


def finish_orders(result):#Ավարտված պատվերների ինիցիալիզացիա
    if result != "error":
        booking_label.init_finish_orders(result)


def start_order_query():#Պատվերների հավաքում
    data_manager.start_query_current_orders_admin(init_orders)


def start_finish_order_query():#Ավարտված պատվերների ինիցիալիզացիա
    data_manager.start_query_finish_orders_admin(finish_orders)


show_bookings()
