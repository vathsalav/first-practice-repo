from data_access_layer.customer_data_access.customer_dao_imp import CustomerDAOImp
from entities.customer_class_info import Customer

customer_dao = CustomerDAOImp()


def test_create_customer_record_success():
    test_customer = Customer(0, "Sash", "sam")
    returned_customer = customer_dao.insert_into_customer_table(test_customer)
    assert returned_customer.customer_id != test_customer.customer_id


def test_delete_customer_record_success():
    result = customer_dao.delete_from_customer_table_by_id(-1)
    assert result
