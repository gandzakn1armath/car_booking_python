import ctypes
user32 = ctypes.windll.user32

class Design:
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

    def get_add_order_geometry(self):
        return (str(self.add_order_tk_width) +
                "x" + str(self.add_order_tk_height) +
                "+" + str(int((self.pc_width - self.add_order_tk_width) / 2)) +
                "+" + str(int((self.pc_height - self.add_order_tk_height) / 2)))

    def get_sign_up_geometry(self):
        return (str(self.sign_up_label_tk_width) +
                "x" + str(self.sign_up_label_tk_height) +
                "+" + str(int((self.pc_width - self.sign_up_label_tk_width) / 2)) +
                "+" + str(int((self.pc_height - self.sign_up_label_tk_height) / 2)))

    def get_sign_in_geometry(self):
        return (str(self.sign_in_tk_width) +
                "x" + str(self.sign_in_tk_height) +
                "+" + str(int((self.pc_width - self.sign_in_tk_width) / 2)) +
                "+" + str(int((self.pc_height - self.sign_in_tk_height) / 2)))

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
