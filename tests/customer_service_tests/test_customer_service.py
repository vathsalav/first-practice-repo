from custom_exception.bad_id import BadId
from custom_exception.bad_name import BadName
from data_access_layer.customer_data_access.customer_dao_imp import CustomerDAOImp
from entities.customer_class_info import Customer
from service_layer.customer_service.customer_service_imp import CustomerServiceImp

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)


def test_catch_non_string_first_name():
    try:
        customer_service.service_create_customer_record(Customer(0, 31290, "this is fine"))
        assert False
    except BadName as e:
        assert str(e) == "Please enter a valid first name"


def test_catch_non_string_last_name():
    try:
        customer_service.service_create_customer_record(Customer(0, "this is fine", 984938))
        assert False
    except BadName as e:
        assert str(e) == "Please enter a valid last name"


def test_catch_first_name_too_long():
    try:
        customer_service.service_create_customer_record(
            Customer(0, "This is a way too long name for our app", "This is fine"))
        assert False
    except BadName as e:
        assert str(e) == "First name is too long: It should not be more than 20 characters"


def test_catch_last_name_too_long():
    try:
        customer_service.service_create_customer_record(
            Customer(0, "This is fine", "This is a way too long name for our app"))
        assert False
    except BadName as e:
        assert str(e) == "Last name is too long: It should not be more than 20 characters"


def test_catch_non_int_typecastable_value():
    try:
        customer_service.service_delete_customer_record_by_id("one")
    except BadId as e:
        assert str(e) == "Please provide a valid customer Id"
