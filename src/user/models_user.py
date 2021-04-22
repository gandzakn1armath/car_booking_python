import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
import re
from firebase import firebase
from datetime import datetime
from threading import Thread


class User:
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
