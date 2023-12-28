from abc import ABC, abstractmethod


class BaseDataRepository(ABC):
    """
    ORM dependency injection class
    query_set: get data 의 orm query set
    value_set: get data 의 value tuple
    set_instance: orm filter set / order_by / pagination 구현
    convert_to_dto: dto class
    """

    __query_instance = ""
    __sort = ""
    query_set = {}
    value_set = ()

    def __init__(self, kwargs, sort_by="", current_page=0):
        self.set_instance(kwargs, sort_by, current_page)
        self.set_query_set()
        self.set_value_set()

    @abstractmethod
    def convert_to_dto(self, data):
        raise NotImplementedError

    @abstractmethod
    def set_query_set(self):
        raise NotImplementedError

    @abstractmethod
    def set_value_set(self):
        raise NotImplementedError

    @abstractmethod
    def set_instance(self, kwargs, sort_by, current_page):
        raise NotImplementedError

    """
    CRUD function
    """

    @abstractmethod
    def get_data_by_kwargs(self, kwargs, sort_by):
        pass
