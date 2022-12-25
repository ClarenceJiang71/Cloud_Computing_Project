from flask import Flask, Response, request
from datetime import datetime
import json
from shop_resource import ShopResource
from order_resource import OrderResource
from product_resource import ProductResource
from flask_cors import CORS
from sns import NotificationMiddlewareHandler

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)



@app.get("/api/health")
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "COMS6156-sprint1-microservice2",
        "health": "Good",
        "at time": t
    }

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result


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
            rsp = Response(json.dumps({'status':200}), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")
        print(rsp)
        return rsp


@app.route("/api/shop/", methods=["POST",'PUT'])
def update_shop():
    if request.method == 'POST':
        shop = request.get_json()
        result = ShopResource.add(shop)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
            sns = NotificationMiddlewareHandler.get_sns_client()
            print("Got SNS Client!")
            tps = NotificationMiddlewareHandler.get_sns_topics()
            print("SNS Topics = \n", json.dumps(tps, indent=2))

            message = {"test": "new shop created"}
            NotificationMiddlewareHandler.send_sns_message(
                "arn:aws:sns:us-east-1:606830512180:6156-shop",
                message
            )

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



def get_order_by_orderID(orderID):

    result = OrderResource.get_by_key(orderID)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("Internal server error", status=500, content_type="text/plain")

    return rsp




@app.route("/api/product/<productID>", methods=["GET"])
def get_product_by_productID(productID):

    result = ProductResource.get_by_key(productID)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

