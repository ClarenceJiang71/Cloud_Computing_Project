from flask import Flask, Response, request
import json
from columbia_student_resource import AccountResource
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    message = "Please add the following format behind the current localhost url.  /api/ (your interested database)/(your interested table)/(accountId)"
    return message

@app.route("/api/contacts/payment", methods=["GET"])
def get_contacts_all_payment():

    if request.method == "GET":
        result = AccountResource.get_whole_table("payment")

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

        return rsp
    # else:
    #     result = request.form[]


@app.route("/api/contacts/payment/<accountId>", methods=["GET"])
def get_contacts_payment_by_uni(accountId):

    result = AccountResource.get_by_key("payment", accountId)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/contacts/phone", methods=["GET"])
def get_contacts_all_phone():

    result = AccountResource.get_whole_table("phone")

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/contacts/phone/<accountId>", methods=["GET"])
def get_contacts_phone_by_uni(accountId):

    result = AccountResource.get_by_key("phone", accountId)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/contacts/email", methods=["GET", "POST"])
def get_contacts_all_email():
    print("Check")
    if request.method == "GET":
        result = AccountResource.get_whole_table("email")

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")
        return rsp
    else:
        email = request.form["email"]
        # accountId = request.form["accountId"]
        print(email)
        print(type(email))
        # print(accountId)
        # print(type(accountId))


        # result = AccountResource.put("email")
        #
        # if result:
        #     rsp = Response(json.dumps(result), status=200, content_type="application.json")
        # else:
        #     rsp = Response("NOT FOUND", status=404, content_type="text/plain")

@app.route("/api/contacts/email/<accountId>", methods=["GET"])
def get_contacts_email_by_uni(accountId):

    result = AccountResource.get_by_key("email", accountId)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/contacts/address", methods=["GET"])
def get_contacts_all_address():

    result = AccountResource.get_whole_table("address")

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/contacts/address/<accountId>", methods=["GET"])
def get_contacts_address_by_uni(accountId):

    result = AccountResource.get_by_key("address", accountId)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/contacts/<accountId>", methods=["GET"])
def get_contacts_by_uni(accountId):

    result = AccountResource.get_by_union_info(accountId)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/contacts/phone/<pk>/email", methods=["GET"])
def get_email_by_phone(pk):

    result = AccountResource.get_through_two_tables("phone", pk, "email")

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

