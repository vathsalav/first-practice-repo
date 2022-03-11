from data_access_layer.customer_data_access.customer_dao_interface import CustomerDAOInterface
from entities.customer_class_info import Customer


class CustomerDAOImp(CustomerDAOInterface):

    def delete_from_customer_table(self, customer_id: int) -> bool:
        pass

    def insert_into_customer_table_by_id(self, customer_obj: Customer) -> Customer:
        pass