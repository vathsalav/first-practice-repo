from flask import Flask, jsonify, request

from custom_exception.bad_id import BadId
from custom_exception.bad_name import BadName
from custom_exception.connection_problem import ConnectionProblem
from custom_exception.nothing_deleted import NothingDeleted
from data_access_layer.customer_data_access.customer_dao_imp import CustomerDAOImp
from entities.customer_class_info import Customer

from service_layer.customer_service.customer_service_imp import CustomerServiceImp

app: Flask = Flask(__name__)
customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)

@app.route("/customer", methods=["POST"])
def create_customer():
    try:
        customer_info_as_dictionary = request.get_json()
        customer = Customer(
            customer_info_as_dictionary["customerId"],
            customer_info_as_dictionary["firstName"],
            customer_info_as_dictionary["lastName"]
        )
        customer_result = customer_service.service_create_customer_record(customer)
        customer_as_dictionary = customer_result.convert_to_dictionary()
        customer_as_json = jsonify(customer_as_dictionary)
        return customer_as_json, 201
    except BadName as e:
        error_message = {"errorMessage": str(e)}
        error_json = jsonify(error_message)
        return error_json, 404
    except ConnectionProblem as e:
        error_message = {"errorMessage": str(e)}
        error_json = jsonify(error_message)
        return error_json, 404


@app.route("/customer/<customer_id>", methods=["DELETE"])
def delete_customer_by_id(customer_id: str):
    try:
        result = customer_service.service_delete_customer_record_by_id(customer_id)
        result_dictionary = {"result":result}
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except NothingDeleted as e:
        error_message = {"errorMessage": str(e)}
        error_json = jsonify(error_message)
        return error_json, 404
    except ConnectionProblem as e:
        error_message = {"errorMessage": str(e)}
        error_json = jsonify(error_message)
        return error_json, 404
    except BadId as e:
        error_message = {"errorMessage": str(e)}
        error_json = jsonify(error_message)
        return error_json, 404

    app.run()


