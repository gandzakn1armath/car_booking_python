import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
import re
from firebase import firebase
from datetime import datetime
import threading



class Data_manager:
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
