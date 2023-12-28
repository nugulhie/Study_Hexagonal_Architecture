from ..module.payment.domain.sub_mall import SubMall
from .base_data_repository import BaseDataRepository
from ..models import PartnerSettlementInfo


class PartnerSettlementInfosRepository(BaseDataRepository):
    index_key = "index"
    partner_id_key = "partner_id"
    ceo_name_key = "ceo_name"
    representative_number_key = "representative_number"
    phone_number_key = "phone_number"
    email_key = "representative_email"
    account_number_key = "account_number"
    account_depositor_key = "account_depositor"
    bank_code_key = "bank_code"
    business_number_key = "business_number"
    account_type_key = "account_type"

    __object__ = PartnerSettlementInfo.objects

    def convert_to_dto(self, data):
        return SubMall(
            account_number=data["account_number"],
            account_depositor=data["account_depositor"],
            bank_code=data["bank_code"],
            representative_name=data["ceo_name"],
            representative_number=data["representative_number"],
            email=data["representative_email"],
            phone_number=data["phone_number"],
            type=data["account_type"],
            sub_mall_id=data["partner_id"],
            business_number=data["business_number"],
        )

    def set_query_set(self):
        self.query_set = {}

    def set_value_set(self):
        self.value_set = (
            self.index_key,
            self.partner_id_key,
            self.ceo_name_key,
            self.representative_number_key,
            self.phone_number_key,
            self.email_key,
            self.account_number_key,
            self.account_depositor_key,
            self.bank_code_key,
            self.business_number_key,
            self.account_type_key,
        )

    def get_data_by_kwargs(self):
        result = self.__query_instance.annotate(**self.query_set).values(
            *self.value_set
        )

        return [self.convert_to_dto(res) for res in result]

    def set_instance(self, kwargs=None, sort_by="", current_page=0):
        if kwargs is None:
            self.__query_instance = self.__object__.filter()
        else:
            self.__query_instance = self.__object__.filter(**kwargs)

    def get_datas(self):
        data = self.get_data_by_kwargs()
        return data

    def update_by_kwargs(self, **update_set):
        temp = update_set
        import copy

        update_dict = copy.deepcopy(update_set)
        for i in temp.keys():
            if temp[i] is None:
                del update_dict[i]
        self.__query_instance.update(**update_dict)
