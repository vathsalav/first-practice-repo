from abc import ABC, abstractmethod

from entities.account_class import Account


class AccountDAOInterface(ABC):

    @abstractmethod
    def insert_into_account_table(self, account_obj: Account) -> Account:
        pass

    @abstractmethod
    def get_account_info_from_account_table(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def update_account_info_from_account_table(self, balance: float) -> Account:
        pass

    @abstractmethod
    def delete_account_info_from_account_table(self, account_id: int) -> bool:
        pass







