from abc import ABC, abstractmethod

from entities.customer_class_info import Customer


class CustomerDAOInterface(ABC):

    @abstractmethod
    def insert_into_customer_table(self, customer_obj: Customer) -> Customer:
        pass

    @abstractmethod
    def delete_from_customer_table_by_id(self, customer_id: int) -> bool:
        pass



