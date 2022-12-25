from flask import Flask, Request, Response, request
import json
from account_resource import AccountResource
from customer_resource import CustomerResource
from membership_resource import MembershipResource
from flask_cors import CORS

application = Flask(__name__)

CORS(application)


@application.route("/api/account/<emailID>", methods=["GET", "DELETE"])
def get_or_delete_account(emailID):
    if request.method == "GET":
        result = AccountResource.get_account_by_emailID(emailID)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    if request.method == "DELETE":
        result = AccountResource.delete_account_by_emailID(emailID)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.route("/api/account/", methods=["POST", "PUT"])
def post_or_put_account():
    if request.method == "POST":
        account = request.get_json()
        result = AccountResource.create_account(account)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    if request.method == "PUT":
        account = request.get_json()
        result = AccountResource.update_account(account)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


# ======================================================================================================================
# ======================================================================================================================


# Customer
@application.route("/api/customer/<emailID>", methods=["GET", "DELETE"])
def get_or_delete_customer(emailID):
    if request.method == "GET":
        result = CustomerResource.get_customer_by_emailID(emailID)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    if request.method == "DELETE":
        result = CustomerResource.delete_customer_by_emailID(emailID)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.route("/api/customer/", methods=["POST", "PUT"])
def post_or_put_customer():
    if request.method == "POST":
        customer = request.get_json()
        result = CustomerResource.create_customer(customer)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    if request.method == "PUT":
        customer = request.get_json()
        result = CustomerResource.update_customer(customer)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


# ======================================================================================================================
# ======================================================================================================================


# Membership
@application.route("/api/membership/<emailID>", methods=["GET", "DELETE"])
def get_or_delete_membership(emailID):
    if request.method == "GET":
        result = MembershipResource.get_membership_by_emailID(emailID)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    if request.method == "DELETE":
        result = MembershipResource.delete_membership_by_emailID(emailID)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.route("/api/membership/", methods=["POST", "PUT"])
def post_or_put_membership():
    if request.method == "POST":
        membership = request.get_json()
        result = MembershipResource.create_membership(membership)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    if request.method == "PUT":
        customer = request.get_json()
        result = MembershipResource.update_membership(membership)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    application.run(port=8000)
