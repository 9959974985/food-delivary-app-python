import random
import string
import json
from json import JSONDecodeError


def registration(member, admin_json, users_json, name, phone, email, add, passwrd):
    '''Register Function || Return True if registered successfully else False'''
    if member.lower() == 'admin':
        f = open(admin_json, 'r+')
        d = {
            "Full Name": name,
            "Phone": phone,
            "Email": email,
            "Address": add,
            "Password": passwrd,
        }
        try:
            content = json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content, f)

        except JSONDecodeError:
            l = []
            l.append(d)
            json.dump(l, f)
        f.close()
    elif member.lower() == 'user':
        f = open(users_json, 'r+')
        d = {
            "Full Name": name,
            "Phone": phone,
            "Email": email,
            "Address": add,
            "Password": passwrd,
        }
        try:
            content = json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content, f)

        except JSONDecodeError:
            l = []
            l.append(d)
            json.dump(l, f)

        f.close()


def login(member, admin_json, users_json, email, password):
    '''Login Functionality || Return True if successfully logged in else False'''
    d = 0
    if member.lower() == 'admin':
        f = open(admin_json, 'r+')
    else:
        f = open(users_json, 'r+')
    try:
        content = json.load(f)
    except JSONDecodeError:
        return False
    for i in range(len(content)):
        if content[i]["Email"] == email and content[i]["Password"] == password:
            d = 1
            break
    f.seek(0)
    f.truncate()
    json.dump(content, f)
    f.close()
    if d == 0:
        return False
    return True


def autogenerate_foodId():
    '''Return a autogenerated random Food ID'''
    foodId = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return foodId


def autogenerate_OrderId():
    '''Return a autogenerated random Order ID'''
    
    Order_ID = ''.join(random.choices(stringascii_uppercase + string.digits, k=3))
    return Order_ID


def addItem(admin, add_item_json_file, foodId, dish, quantity, price, discount, stock):
    fp = open(add_item_json_file, "r+")
    d = {
        "created by": admin,
        "Food ID": foodId,
        "Dish": dish,
        "Quantity": quantity,
        "Price": price,
        "Food discount": discount,
        "Available stock": stock
    }
    try:
        content = json.load(fp)
        if d not in content:
            content.append(d)
            fp.seek(0)
            fp.truncate()
            json.dump(content, fp)
    except JSONDecodeError:
        l=[]
        l.append(d)
        json.dump(l, fp)
    fp.close()


def viewItem(admin, add_items_json_file):
    fp = open(add_items_json_file, "r+")
    content = json.load(fp)
    itemlist = []
    for i in content:
        if i["created by"] == admin:
            itemlist.append(i)
    fp.close()


def viewByFoodID(add_items_json_file, foodId, details):
    fp = open(add_items_json_file, "r+")
    content = json.load(fp)
    for i in content:
        if i["Food ID"] == foodId:
            details.append(i)
            break
    fp.close()


def updateItem(add_items_json_file, foodId, details_to_be_updated, new_value):
    fp = open(add_items_json_file, "r+")
    d = {details_to_be_updated: new_value}
    try:
        content = json.load(fp)
        for i in content:
            if i["Food ID"] == foodId:
                i.update(d)
                fp.seek(0)
                fp.truncate()
                json.dump(content, fp)
                break
    except JSONDecodeError:
        return False
    fp.close()
    return True


def deleteItem(add_items_json_file, foodID):
    fp = open(add_items_json_file, "r+")
    try:
        content = json.load(fp)
        for i in content:
            if i["Food ID"] == foodId:
                del content[content.index(i)]
                fp.seek(0)
                fp.truncate()
                json.dump(content, fp)
                break
    except JSONDecodeError:
        return False
    fp.close()
    return True


def updateProfile(users_json_file, name, details_to_be_updated, new_value):
    fp = open(users_json_file, "r+")
    d = {details_to_be_updated: new_value}
    try:
        content = json.load(fp)
        for i in content:
            if i["Full Name"] == name:
                i.update(d)
                fp.seek(0)
                fp.truncate()
                json.dump(content, fp)
                break
    except JSONDecodeError:
        return False
    fp.close()
    return True


def placeOrder(order_json_file, price_after_discount, price, discount, Order_ID, dish, quantity, foodID, ordered_by,
               delivery_address):
    fp = open(order_json_file, "r+")
    price_after_discount = float(float(price) - ((float(price) * float(discount[:-1])) / 100))
    d = {
        "Ordered by": Order_ID,
        "Dish": dish,
        "Price": price,
        "Discount": discount,
        "Price_after_discount": price_after_discount,
        "Quantity": quantity,
        "Food ID": foodId,
        "Total cost": quantity * price_after_discount,
        "Ordered by": ordered_by,
        "Delivery address": delivery_address
    }
    try:
        content = json.load(fp)
        content.append(d)
        fp.seek(0)
        fp.truncate()
        json.dump(content, fp)
    except:
        l=[]
        l.append(d)
        json.dump(l, fp)
    fp.close()
    return True


def orderHistory(order_json_file, Name, details):
    fp = open(order_json_file, "r+")
    try:
        content = json.load(fp)
        for i in content:
            if i["Ordered by"] == Name:
                details.append(i)
    except JSONDecodeError:
        return False
    fp.close()
    return True
