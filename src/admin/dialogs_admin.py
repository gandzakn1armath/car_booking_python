from tkinter import *
from src.admin.design_admin import Design

design = Design()


class Show_booking:
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

    def hide(self):
        self.tk.destroy()

    def show_dialog(self, started):
        if self.orderStatus == "PENDING":
            self.start = Button(self.tk, text="Սկսել", width=15, height=2, bg=design.bg_button,
                                command=started)
            self.start.place(x=180, y=550)
        elif self.orderStatus == "STARTED":
            self.start = Button(self.tk, text="Ավարտել", width=15, height=2, bg=design.bg_button,
                                command=started)
            self.start.place(x=180, y=550)

        self.tk.mainloop()


class Car_label:
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

    def show_dialog(self):
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

    def hide(self):
        self.tk.destroy()


class Booking_label:
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

    def show_dialog(self, add_button, show_item):
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

    def hide(self):
        self.tk.destroy()
