from tkinter import *
from src.user.design_user import Design

design = Design()


class Sign_up_label:
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

    def show_dialog(self, sign_in_btn, log_in_btn):
        Button(self.tk, text="Գրանցվել", width=20, height=2, bg=design.bg_button, command=sign_in_btn)\
            .place(x=30, y=120)
        Button(self.tk, text="Մուտք", width=20, height=2, bg=design.bg_button, command=log_in_btn).place(x=210, y=120)
        self.tk.mainloop()

    def hide(self):
        self.tk.destroy()


class Show_booking_user:
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

    def hide(self):
        self.tk.destroy()

    def show_dialog(self):
        self.tk.mainloop()


class User_page:
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

    def show_dialog(self, add_btn, see, exit_account):
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

    def hide(self):
        self.tk.destroy()


class Add_order:

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

    def show_dialog(self, save):
        Button(self.tk, text="Ստեղծել", width=15, height=2, bg=design.bg_button, command=save).place(x=110, y=300)
        self.tk.mainloop()

    def hide(self):
        self.tk.destroy()

    def get_pickup_address(self):
        return self.address.get()
