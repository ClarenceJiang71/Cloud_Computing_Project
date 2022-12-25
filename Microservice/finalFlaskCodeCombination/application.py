from flask import Flask, Response, request
import json
from contact_resource import ContactResource
from order_resource import OrderResource
from product_resource import ProductResource
from shop_resource import ShopResource
from customer_resource import CustomerResource
from flask_cors import CORS
from smartystreets_python_sdk import StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup
from composite_resource import CompositeResource

smartystreet_auth_id = "70b15887-070e-9ea2-3b30-093a216b0ba4"
smartystreet_auth_token = "HUL2wtOv89nE35qo1NBS"
smartystreet_credentials = StaticCredentials(smartystreet_auth_id, smartystreet_auth_token)
smartystreet_client = ClientBuilder(smartystreet_credentials).build_us_street_api_client()

# Create the Flask application object.
app = Flask(__name__)

CORS(app)

@app.route("/api/shop/<shopID>", methods=["GET","DELETE","PUT"])
def change_shop_by_shopID(shopID):

    if request.method == 'GET':

        result = ShopResource.get_by_key(shopID)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

        return rsp
    elif request.method == 'DELETE':

        result = ShopResource.delete_by_key(shopID)

        if result:
            rsp = Response(json.dumps({'status': 200}), status = 200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

        return rsp

@app.route("/api/shop/", methods=["POST",'PUT'])
def update_shop():
    if request.method == 'POST':
        shop = request.get_json()
        result = ShopResource.add(shop)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("Internal server error", status=500, content_type="text/plain")

        return rsp

    elif request.method == 'PUT':
        shop = request.get_json()
        result = ShopResource.update(shop)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("Internal server error", status=500, content_type="text/plain")

        return rsp

@app.route("/api/customer/<emailID>", methods=["GET", "DELETE"])
def get_or_delete_customer(emailID):
    if request.method == "GET":
        result = CustomerResource.get_customer_by_emailID(emailID)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    elif request.method == "DELETE":

        result = CustomerResource.delete_customer_by_emailID(emailID)

        if result:
            rsp = Response(json.dumps({'status': 200}), status = 200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/customer/", methods=["POST", "PUT"])
def post_or_put_customer():
    if request.method == 'POST':
        customer = request.get_json()
        result = CustomerResource.create_customer(customer)

        if result:
            # rsp = Response(json.dumps(result), status=200, content_type="application.json")
            rsp = Response(json.dumps({'status': 200}), status=200, content_type="application.json")
        else:
            rsp = Response("Internal server error", status=500, content_type="text/plain")

        return rsp

    elif request.method == "PUT":
        customer = request.get_json()
        result = CustomerResource.update_customer(customer)
        print(result)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status==500, content_type="text/plain")

    return rsp

@app.route("/api/address/<accountId>", methods=["GET", "DELETE"])
def get_contacts_address_by_uni(accountId):
    if request.method == 'GET':
        result = ContactResource.get_by_key("address", accountId)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

        return rsp
    elif request.method == 'DELETE':

        result = ContactResource.delete_by_key(accountId)

        if result:
            rsp = Response(json.dumps({'status': 200}), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

        return rsp

@app.route("/api/address/", methods=["POST",'PUT'])
def update_address():
    if request.method == 'POST':
        address = request.get_json()
        value = evaluate(address)
        if not value:
            rsp = Response("Wrong address error", status=500, content_type="text/plain")
            return rsp

        result = ContactResource.add(address)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("Internal server error", status=500, content_type="text/plain")

        return rsp

    elif request.method == 'PUT':
        address = request.get_json()
        value = evaluate(address)
        if not value:
            rsp = Response("Wrong address error", status=500, content_type="text/plain")
            return rsp

        result = ContactResource.update(address)


        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("Internal server error", status=500, content_type="text/plain")

        return rsp

@app.route("/api/product/<productID>", methods=["GET", "DELETE"])
def get_product_by_productID(productID):
    if request.method == 'GET':

        result = ProductResource.get_by_key(productID)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

        return rsp
    elif request.method == 'DELETE':

        result = ProductResource.delete_by_key(productID)

        if result:
            rsp = Response(json.dumps({'status': 200}), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

        return rsp

@app.route("/api/product/", methods=["POST",'PUT'])
def update_product():
    if request.method == 'POST':
        product = request.get_json()
        result = ProductResource.add(product)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("Internal server error", status=500, content_type="text/plain")

        return rsp

    elif request.method == 'PUT':
        product = request.get_json()
        result = ProductResource.update(product)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("Internal server error", status=500, content_type="text/plain")

        return rsp
@app.route("/api/order/<orderID>", methods=["GET", "DELETE"])
def get_order_by_orderID(orderID):
    if request.method == 'GET':

        result = OrderResource.get_by_key(orderID)

        if result:
            rsp = Response(json.dumps(result, default=str), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

        return rsp
    elif request.method == 'DELETE':
        result = OrderResource.delete_by_key(orderID)

        if result:
            rsp = Response(json.dumps({'status': 200}), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

        return rsp

@app.route("/api/order/", methods=["POST",'PUT'])
def update_order():
    if request.method == 'POST':
        order = request.get_json()
        result = OrderResource.add(order)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("Internal server error", status=500, content_type="text/plain")

        return rsp

    elif request.method == 'PUT':
        order = request.get_json()
        result = OrderResource.update(order)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("Internal server error", status=500, content_type="text/plain")

        return rsp

def evaluate(address):
    lookup = Lookup()
    lookup.street = address["street"]
    lookup.secondary = address["aptNo"]
    lookup.city = address["city"]
    lookup.state = address["state"]
    lookup.zip = address["zip"]

    try:
        smartystreet_client.send_lookup(lookup)
    except exceptions.SmartyException as err:
        print(err)
        return

    result = lookup.result

    if not result:
        print("This is not a valid address")
        return False
    return True

@app.route("/api/composite/<emailID>", methods=["GET"])
def get_composite(emailID):
    if request.method == "GET":
        result = CompositeResource.get_composite_by_emailID(emailID)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


#
# @app.route('/')
# def index():
#     message = "Please add the following format behind the current localhost url.  /api/ (your interested database)/(your interested table)/(accountId)"
#     return message
#
# @app.route("/api/contacts/payment", methods=["GET"])
# def get_contacts_all_payment():
#
#     if request.method == "GET":
#         result = ContactResource.get_whole_table("payment")
#
#         if result:
#             rsp = Response(json.dumps(result), status=200, content_type="application.json")
#         else:
#             rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#         return rsp
#     # else:
#     #     result = request.form[]
#
#
# @app.route("/api/contacts/payment/<accountId>", methods=["GET"])
# def get_contacts_payment_by_uni(accountId):
#
#     result = ContactResource.get_by_key("payment", accountId)
#
#     if result:
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     return rsp
#
# @app.route("/api/contacts/phone", methods=["GET"])
# def get_contacts_all_phone():
#
#     result = ContactResource.get_whole_table("phone")
#
#     if result:
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     return rsp
#
#
# @app.route("/api/contacts/phone/<accountId>", methods=["GET"])
# def get_contacts_phone_by_uni(accountId):
#
#     result = ContactResource.get_by_key("phone", accountId)
#
#     if result:
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     return rsp
#
# @app.route("/api/contacts/email", methods=["GET"])
# def get_contacts_all_email():
#     if request.method == "GET":
#         result = ContactResource.get_whole_table("email")
#
#         if result:
#             rsp = Response(json.dumps(result), status=200, content_type="application.json")
#         else:
#             rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#         return rsp
#     # else:
#     #     email = request.form["email"]
#     #     # accountId = request.form["accountId"]
#     #     print(email)
#     #     print(type(email))
#     #     # print(accountId)
#     #     # print(type(accountId))
#     #
#     #
#     #     # result = AccountResource.put("email")
#     #     #
#     #     # if result:
#     #     #     rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     #     # else:
#     #     #     rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
# @app.route("/api/contacts/email/<accountId>", methods=["GET"])
# def get_contacts_email_by_uni(accountId):
#
#     result = ContactResource.get_by_key("email", accountId)
#
#     if result:
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     return rsp
#
# @app.route("/api/contacts/address", methods=["GET"])
# def get_contacts_all_address():
#
#     result = ContactResource.get_whole_table("address")
#
#     if result:
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     return rsp
#
# @app.route("/api/contacts/address/<accountId>", methods=["GET"])
# def get_contacts_address_by_uni(accountId):
#
#     result = ContactResource.get_by_key("address", accountId)
#
#     if result:
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     return rsp
#
#
# @app.route("/api/contacts/<accountId>", methods=["GET"])
# def get_contacts_by_uni(accountId):
#
#     result = ContactResource.get_by_union_info(accountId)
#
#     if result:
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     return rsp
#
#
# @app.route("/api/contacts/phone/<pk>/email", methods=["GET"])
# def get_email_by_phone(pk):
#
#     result = ContactResource.get_through_two_tables("phone", pk, "email")
#
#     if result:
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     return rsp
#
#
# # Start from here is the customer microservice
# @app.route("/api/account/<emailID>", methods=["GET", "DELETE"])
# def get_or_delete_account(emailID):
#     if request.method == "GET":
#         result = AccountResource.get_account_by_emailID(emailID)
#
#         if result:
#             rsp = Response(json.dumps(result), status=200, content_type="application.json")
#         else:
#             rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     if request.method == "DELETE":
#         result = AccountResource.delete_account_by_emailID(emailID)
#
#         if result:
#             rsp = Response(json.dumps(result), status=200, content_type="application.json")
#         else:
#             rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     return rsp
#
#
# @app.route("/api/account/", methods=["POST", "PUT"])
# def post_or_put_account():
#     if request.method == "POST":
#         account = request.get_json()
#         result = AccountResource.create_account(account)
#
#         if result:
#             rsp = Response(json.dumps(result), status=200, content_type="application.json")
#         else:
#             rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     if request.method == "PUT":
#         account = request.get_json()
#         result = AccountResource.update_account(account)
#
#         if result:
#             rsp = Response(json.dumps(result), status=200, content_type="application.json")
#         else:
#             rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     return rsp
#
#
# # ======================================================================================================================
# # ======================================================================================================================
#
#
# # Customer
#
#
#
# # ======================================================================================================================
# # ======================================================================================================================
#
#
# # Membership
# @app.route("/api/membership/<emailID>", methods=["GET", "DELETE"])
# def get_or_delete_membership(emailID):
#     if request.method == "GET":
#         result = MembershipResource.get_membership_by_emailID(emailID)
#
#         if result:
#             rsp = Response(json.dumps(result), status=200, content_type="application.json")
#         else:
#             rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     if request.method == "DELETE":
#         result = MembershipResource.delete_membership_by_emailID(emailID)
#
#         if result:
#             rsp = Response(json.dumps(result), status=200, content_type="application.json")
#         else:
#             rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     return rsp
#
#
# @app.route("/api/membership/", methods=["POST", "PUT"])
# def post_or_put_membership():
#     if request.method == "POST":
#         membership = request.get_json()
#         result = MembershipResource.create_membership(membership)
#
#         if result:
#             rsp = Response(json.dumps(result), status=200, content_type="application.json")
#         else:
#             rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     if request.method == "PUT":
#         customer = request.get_json()
#         result = MembershipResource.update_membership(membership)
#
#         if result:
#             rsp = Response(json.dumps(result), status=200, content_type="application.json")
#         else:
#             rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     return rsp
#
#
#
#
# # Start here is the product microservice
#
# @
# def get_order_by_orderID(orderID):
#
#     result = OrderResource.get_by_key(orderID)
#
#     if result:
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("Internal server error", status=500, content_type="text/plain")
#
#     return rsp
#
#
#
#
# @app.route("/api/product/<productID>", methods=["GET"])
# def get_product_by_productID(productID):
#
#     result = ProductResource.get_by_key(productID)
#
#     if result:
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#
#     return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

