from tkinter import messagebox      #Ներմուծում ենք գրադարանները
import json
import os
from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
import re
from firebase import firebase
from datetime import datetime
import ctypes
user32 = ctypes.windll.user32

class Design:                   #Այս ֆայլի դիզայնի կլասը
    def __init__(self):
        self.pc_width = int(user32.GetSystemMetrics(0))
        self.pc_height = int(user32.GetSystemMetrics(1))
        self.sign_up_label_tk_width = 400
        self.sign_up_label_tk_height = 350
        self.sign_in_tk_width = 400
        self.sign_in_tk_height = 170
        self.add_order_tk_width = 325
        self.add_order_tk_height = 350
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

    def get_add_order_geometry(self):      #մեթոդ, որը չափսեր է տալիս կլասին և տեղադրում էկրանի կենտրոնում 
        return (str(self.add_order_tk_width) +
                "x" + str(self.add_order_tk_height) +
                "+" + str(int((self.pc_width - self.add_order_tk_width) / 2)) +
                "+" + str(int((self.pc_height - self.add_order_tk_height) / 2)))

    def get_sign_up_geometry(self):         #մեթոդ, որը չափսեր է տալիս կլասին և տեղադրում էկրանի կենտրոնում 
        return (str(self.sign_up_label_tk_width) +
                "x" + str(self.sign_up_label_tk_height) +
                "+" + str(int((self.pc_width - self.sign_up_label_tk_width) / 2)) +
                "+" + str(int((self.pc_height - self.sign_up_label_tk_height) / 2)))

    def get_sign_in_geometry(self):         #մեթոդ, որը չափսեր է տալիս կլասին և տեղադրում էկրանի կենտրոնում 
        return (str(self.sign_in_tk_width) +
                "x" + str(self.sign_in_tk_height) +
                "+" + str(int((self.pc_width - self.sign_in_tk_width) / 2)) +
                "+" + str(int((self.pc_height - self.sign_in_tk_height) / 2)))

    def get_show_booking_geometry(self):        #մեթոդ, որը չափսեր է տալիս կլասին և տեղադրում էկրանի կենտրոնում 
        return str(self.show_booking_tk_width) + "x" + str(self.show_booking_tk_height) + "+" + str(
            int((self.pc_width - self.show_booking_tk_width) / 2)) + "+" + str(
            int((self.pc_height - self.show_booking_tk_height) / 2))

    def get_booking_label_geometry(self):       #մեթոդ, որը չափսեր է տալիս կլասին և տեղադրում էկրանի կենտրոնում 
        return str(self.booking_label_tk_width) + "x" + str(self.booking_label_tk_height) + "+" + str(
            int((self.pc_width - self.booking_label_tk_width) / 2)) + "+" + str(
            int((self.pc_height - self.booking_label_tk_height) / 2))
design = Design()

class Sign_up_label:        #Գրանցվելու պատուհանի կլասը
    def __init__(self):
        entry_x = 200
        label_x = 35
        self.tk = Tk()
        self.tk.resizable(False, False)
        self.tk.geometry(design.get_sign_up_geometry())
        self.frame = Frame(self.tk, width=design.pc_width, height=design.pc_height, bg=design.bg).pack()
        self.firstName = Label(self.tk, text="Անուն", font=design.font, fg=design.fg_label,
                               bg=design.bg).place(x=label_x, y=55)
        self.lastName = Label(self.tk, text="Ազգանուն", font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=label_x, y=105)
        self.phoneNumber = Label(self.tk, text="Հեռ․ համար", font=design.font, fg=design.fg_label,
                                 bg=design.bg).place(x=label_x, y=155)
        self.password = Label(self.tk, text="Գաղտնաբառ", font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=label_x, y=205)
        self.firstNameEt = StringVar()
        Entry(self.tk, width=25, textvariable=self.firstNameEt).place(x=entry_x, y=58)
        self.lastNameEt = StringVar()
        Entry(self.tk, width=25, textvariable=self.lastNameEt).place(x=entry_x, y=108)
        self.phone_number_et = StringVar()
        Entry(self.tk, width=25, textvariable=self.phone_number_et).place(x=entry_x, y=158)
        self.passwordEt = StringVar()
        Entry(self.tk, width=25, textvariable=self.passwordEt).place(x=entry_x, y=208)

    def get_first_name(self):
        return self.firstNameEt.get()

    def get_last_name(self):
        return self.lastNameEt.get()

    def get_phone(self):
        return self.phone_number_et.get()

    def get_password(self):
        return self.passwordEt.get()

    def show_dialog(self, sign_up_btn):
        Button(self.tk, text="Գրանցվել", width=40, height=2, bg=design.bg_button, command=sign_up_btn)\
            .place(x=56, y=270)
        self.tk.mainloop()

    def hide(self):
        self.tk.destroy()


class Sign_in_dialog:
    def __init__(self):
        entry_x = 200
        label_x = 35
        self.tk = Tk()
        self.tk.resizable(False, False)
        self.tk.geometry(design.get_sign_in_geometry())
        self.frame = Frame(self.tk, width=design.pc_width, height=design.pc_height, bg=design.bg).pack()
        self.phoneNumber = Label(self.tk, text="Հեռ․ համար", font=design.font, fg=design.fg_label,
                                 bg=design.bg).place(x=label_x, y=20)
        self.password = Label(self.tk, text="Գաղտնաբառ", font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=label_x, y=70)
        self.phone_number_et = StringVar()
        Entry(self.tk, width=25, textvariable=self.phone_number_et).place(x=entry_x, y=28)
        self.passwordEt = StringVar()
        Entry(self.tk, width=25, textvariable=self.passwordEt).place(x=entry_x, y=78)

    def get_phone(self):
        return self.phone_number_et.get()

    def get_password(self):
        return self.passwordEt.get()

    def show_dialog(self, sign_in_btn, log_in_btn):  #Ստեղծում ենք գրանցվելու պատուհանը
        Button(self.tk, text="Գրանցվել", width=20, height=2, bg=design.bg_button, command=sign_in_btn)\
            .place(x=30, y=120)
        Button(self.tk, text="Մուտք", width=20, height=2, bg=design.bg_button, command=log_in_btn).place(x=210, y=120)
        self.tk.mainloop()

    def hide(self):    #Թաքցնում ենք պատուհանը
        self.tk.destroy()


class Show_booking_user:     #Օգտատտիրոջ պատվերի ցույց տալու պատուհանը
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
        self.tk = Tk()
        self.tk.resizable(False, False)
        self.tk.geometry(design.get_show_booking_geometry())
        self.frame = Frame(self.tk, width=design.pc_width, height=design.pc_height, bg=design.bg).pack()
        self.startTime = Label(self.tk, text="Սկիզբ", font=design.font_show_booking, fg='white', bg=design.bg) \
            .place(x=50, y=0)
        self.start = Label(self.tk, text=start_date, font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=20, y=50)
        self.finishTime = Label(self.tk, text="Ավարտ", font=design.font_show_booking, fg='white', bg=design.bg) \
            .place(x=225, y=0)
        self.end = Label(self.tk, text=end_date, font=design.font, fg=design.fg_label, bg=design.bg) \
            .place(x=205, y=50)
        self.firstName = Label(self.tk, text="Անուն", font=design.font_show_booking, fg='white', bg=design.bg) \
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
            x=125,
            y=550)

    def hide(self):     #Թաքցնում ենք պատուհունը
        self.tk.destroy()

    def show_dialog(self):    #Ստեղծում ենք պատուհանը
        self.tk.mainloop()


class User_page:            #Օգտատտիրոջ պատուհանի կլասը
    def __init__(self, user):
        self.user = user
        self.name = str(user["firstName"]) + " " + str(user["lastName"])
        self.tk = Tk()
        self.tk.resizable(False, False)
        self.tk.title(str(user["firstName"]) + " " + str(user["lastName"]))
        self.tk.geometry(design.get_booking_label_geometry())
        self.frame = Frame(self.tk, width=design.pc_width, height=design.pc_height, bg=design.bg).pack()
        self.blackFrame = Frame(self.tk, width=320, height=333, bg=design.frame_for_design).place(x=0, y=45)
        self.blackFrame2 = Frame(self.tk, width=315, height=333, bg=design.frame_for_design).place(x=317, y=45)
        self.nameSurname = Label(self.tk, text=self.name, font=design.font, fg=design.fg_label,
                                 bg=design.bg).place(x=200, y=0)
        self.newOrders = Label(self.tk, text="Ընթացիկ", font=design.font, fg=design.fg_label,
                               bg=design.bg).place(x=90, y=18)
        self.new_order_list_box = Listbox(self.tk, height=20, width=50)
        self.new_order_list_box.place(x=7, y=50)
        self.endedOrders = Label(self.tk, text="Ավարտված", font=design.font, fg=design.fg_label,
                                 bg=design.bg).place(x=420, y=18)
        self.ended_order_list_box = Listbox(self.tk, height=20, width=50)
        self.ended_order_list_box.place(x=323, y=50)

    def show_dialog(self, add_btn, see, exit_account):  #Ստեղծում ենք պատուհանը
        button1 = Button(self.tk, text="Ստեղծել", width=15, height=2, bg=design.bg_button, command=add_btn)
        button1.place(x=100, y=390)

        button2 = Button(self.tk, text="Տեսնել պատվերը", width=15, height=2, bg=design.bg_button, command=see)
        button2.place(x=300, y=390)

        exit = Button(self.tk, text="Դուրս գալ\nհաշվից", width=15, height=2, bg=design.bg_button, command=exit_account)
        exit.place(x=450, y=390)
        self.tk.mainloop()

    def init_new_orders(self, new_order_list):
        self.newOrderList = new_order_list
        index = 0
        for item in new_order_list:
            self.new_order_list_box.insert(index, item)
            index += 1

    def init_finish_orders(self, finish_order_list):
        self.finishOrderList = finish_order_list
        index = 0
        for item in finish_order_list:
            self.ended_order_list_box.insert(index, item)
            index += 1

    def add_order(self, order):
        self.new_order_list_box.insert(END, order)

    def hide(self):     #Թաքցնում ենք պատուհունը
        self.tk.destroy()


class Add_order:                #Պատվերի ավելացնելու կլասը

    def __init__(self):
        self.tk = Tk()
        self.tk.resizable(False, False)
        self.tk.geometry(design.get_add_order_geometry())
        self.frame = Frame(self.tk, width=design.pc_width, height=design.pc_height, bg=design.bg).pack()
        self.carListbox = Listbox(self.tk, exportselection=0, height=15, width=50)
        self.carListbox.place(x=10, y=10)
        self.takePlaceEt = StringVar()
        self.address = Entry(self.tk, width=20, textvariable=self.takePlaceEt)
        self.address.place(x=150, y=263)
        self.takePlace = Label(self.tk, text="Մեկնման վայր", font=design.font, fg=design.fg_label,
                               bg=design.bg).place(x=0, y=260)

    def init_cars(self, cars: list):
        self.cars = cars
        index = 0
        if not self.cars:
            return
        for item in cars:
            index += 1
            self.carListbox.insert(index, item)

    def show_dialog(self, save):        #Ստեղծում ենք պատուհանը
        Button(self.tk, text="Ստեղծել", width=15, height=2, bg=design.bg_button, command=save).place(x=110, y=300)
        self.tk.mainloop()

    def hide(self):    #Թաքցնում ենք պատուհունը
        self.tk.destroy()

    def get_pickup_address(self):
        return self.address.get()

class User:            #Օգտատտիրոջ տվյալների վալիդացման կլասը
    def __init__(self):
        self.id = None

    def set_name(self, name):
        self.firstName = name
        if not name.strip().replace(" ", "").isalpha():
            return False
        if len(name) == 1:
            return False
        return True

    def set_surname(self, surname):
        self.lastName = surname
        if not surname.strip().replace(" ", "").isalpha():
            return False
        if len(surname) == 1:
            return False
        return True

    def set_phone_number(self, phoneNumber):
        try:
            self.phoneNumber = str(phoneNumber)
            if self.phoneNumber[0] == "0":
                phone = self.phoneNumber.replace("0", "+374", 1)
                s = carrier._is_mobile(number_type(phonenumbers.parse(phone)))
                return s
            return self.phoneNumber
        except:
            return False

    def set_password(self, password):
        if not password.strip().replace(" ", "") or len(password) <= 5:
            return False
        elif re.search('[0-9]', password) is None:
            return False
        elif re.search('[A-Z]', password) is None:
            return False
        self.password = password
        return True

    def get_data(self):
        return {
            'firstName': str(self.firstName),
            'lastName': str(self.lastName),
            'phoneNumber': str(self.phoneNumber),
            'password': str(self.password),
        }


class Data_manager:             #Տվյալների ստացման, օգտագործման կլասը
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

    def save(self):
        try:
            id = self.firebase.post('/User', self.user.get_data())
            self.resultListener(self.user.get_data(), id["name"])
        except:
            self.resultListener(None, None)
            pass

    def save_data(self, user: User, resultListener):
        self.resultListener = resultListener
        self.user = user
        self.save()

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



    def saveOrderData(self, firstName, lastName, phoneNumber, userId, takePlace, deliverPlace, status, brand, model,
                      price,
                      saveOrderResult):

        self.saveOrderResult = saveOrderResult
        self.order = {
            'user_firstName': firstName,
            'user_lastName': lastName,
            'user_phoneNumber': phoneNumber,
            'user_id': userId,
            'pickup_address': takePlace,
            'service_address': deliverPlace,
            'status': status,
            'car_brand': brand,
            'car_model': model,
            'car_price': price,
            'startDate': "",
            'endDate': ""
        }
        self.saveOrder()

    def saveOrder(self):
        try:
            resultOrder = self.firebase.post('/Order', self.order)
            id = resultOrder["name"]
            firstName = self.order["user_firstName"]
            lastName = self.order["user_lastName"]
            phoneNumber = self.order["user_phoneNumber"]
            takePlace = self.order["pickup_address"]
            deliverPlace = self.order["service_address"]
            status = self.order["status"]
            brand = self.order["car_brand"]
            model = self.order["car_model"]
            price = self.order["car_price"]
            userText = brand + " " + model + " / " + price + "դ/ժ/ " + takePlace + " / " + status
            adminText = firstName + "  " + lastName + "  " + phoneNumber + " " + brand + " " + model + " / " + \
                        price + "դ/ժ / " + takePlace + " / " + deliverPlace + " / " + status
            self.userTextList.append(userText)
            self.adminTextList.append(adminText)
            self.saveOrderResult(userText)
            self.orderIds.append(id)
            self.admin_order.append(self.order)
            self.userOrder.append(self.order)
        except:
            self.saveOrderResult(None)

    def startOrdersQueryUser(self, user_id, status, order_query_result):
        self.orderQueryResult = order_query_result
        self.queryOrdersForUser(user_id, status)

    def queryOrdersForUser(self, user_id, status):
        try:
            self.orders = self.firebase.get('/Order', None)
            equalStatus = status[0]
            if not self.orders:
                self.orderQueryResult("error")
                return

            for objectId in self.orders:
                order = self.orders[objectId]
                if order["user_id"] == user_id:
                    for s in status:
                        if order["status"] == s:
                            takePlace = order["pickup_address"]
                            brand = order["car_brand"]
                            model = order["car_model"]
                            price = order["car_price"]
                            userText = brand + " " + model + " , " + price + "դ/ժ , " + takePlace + " , " + s
                            if order["status"] != "FINISHED":
                                self.userTextList.append(userText)
                                self.userOrder.append(order)
                            else:
                                self.userFinishTextList.append(userText)
                                self.finish_orders.append(order)

            if equalStatus != "FINISHED":
                self.orderQueryResult(self.userTextList)
            else:
                self.orderQueryResult(self.userFinishTextList)
        except:
            self.orderQueryResult("error")


    def check_user_name_and_pass(self, phone, password):
        self.users = self.firebase.get('/User', None)
        if not self.users:
            return None
        for objectId in self.users:
            user = self.users[objectId]
            if phone == user["phoneNumber"] and password == user["password"]:
                user["id"] = objectId
                return user
        return None

    def is_phone_number_exist(self, phone_number):
        self.users = self.firebase.get('/User', None)
        if not self.users:
            return False
        for objectId in self.users:
            user = self.users[objectId]
            if phone_number == user["phoneNumber"]:
                return True
        return False


#Ստեղծում ենք կլասնեփրի օբյեկտները և որոշ փոփոխականներ
selected_index = None
data_manager = Data_manager()
user = User()
sign: Sign_in_dialog
user_page: User_page
sign_up_label: Sign_up_label
add_order: Add_order

def sign_up():#Գրանցվել
    global sign_up_label
    try:
        sign.hide()
    except:
        pass
    sign_up_label = Sign_up_label()
    sign_up_label.show_dialog(show_sign_up_dialog)

def start_order_query(user_id, status):#Սկսում ենք պատվերների հավաքումը
    data_manager.startOrdersQueryUser(user_id, status, init_orders)


def start_finish_order_query(user_id, status):#Սկսում ենք ավարտված պատվերների հավաքումը
    data_manager.startOrdersQueryUser(user_id, status, finish_orders)


def show_user_page(user,id): #Ցույց ենք տալիս օգտատիրոջ էջը
    global sign_up_label, user_page
    user_page = User_page(user)
    start_order_query(id, ["PENDING", "STARTED"])
    start_finish_order_query(id, ["FINISHED"])
    try:
        sign_up_label.hide()
    except:
        pass
    user_page.show_dialog(start_query, seeOrder, exit_account)


def sign_in():  #Մուտք
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

def sign_up_result(message, id): #Գրանցվելու արդյունքը
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

def show_sign_up_dialog(): #օգտատիրոջ տվյալների վալիդացման մեթոդ
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




def save_order_result(message):#Պատվերի պահպանման արդյունքը
    if message:
        messagebox.showinfo("ՈՒշադրություն", "Ձեր պատվերը հաջողությամբ ավելացվեց")
        add_order.hide()
        user_page.add_order(message)
    else:
        messagebox.showerror("ՈՒշադրություն", "Տեղի ունեցավ սխալ խնդրում ենք փորձել կրկին")


def save_order():  #Պատվերի պահպանման մեթոդ
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


def car_query_result(result): #Ավտոմեքենաների պահպանման արդյունքը
    global add_order, user_page
    if result != "error":
        add_order = Add_order()
        add_order.init_cars(result)
        add_order.show_dialog(save_order)
    else:
        messagebox.showerror("Օօպս ինչ որ մի բան այնպես չգնաց, խնդրում ենք փորձել կրկին")


def first_start(): #Կոդի առաջին անգամ ավտիվացնելու մեթոդ
    global sign
    sign = Sign_in_dialog()
    sign.show_dialog(sign_up, sign_in)


def start_query():#Սկսում ենք ավտոմեքենաների հավաքումը
    data_manager.start_cars_query(car_query_result)


def init_orders(result):#Պատվերի ինիցիալիզացիա
    if result != "error":
        user_page.init_new_orders(result)


def finish_orders(result):#Ավարտված պատվերների ինիցիալիզացիա
    if result != "error":
        user_page.init_finish_orders(result)

def seeOrder():#Պատվերի տեսնելու մեթոդ
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


def exit_account(): #Հաշվից դուրս գալու մեթոդ
    try:
        os.remove("../UserInfo.txt")
    except:
        pass
    user_page.hide()
    first_start()




def second_start(): #Կոդի երկրորդ անգամ ավտիվացնելու մեթոդ
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
