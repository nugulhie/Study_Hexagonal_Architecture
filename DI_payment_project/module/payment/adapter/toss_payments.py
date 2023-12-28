import base64

from ..command.create_sub_mall_command import CreateSubMallCommand
from ..command.update_sub_mall_command import UpdateSubMallCommand
from ..domain.sub_mall import SubMall
from ..port.outbound.pg_port import PgPort
from util.exception import ThirdPartyError
from django.conf import settings


class TossPaymentAdapter(PgPort):
    __url = "https://api.tosspayments.com/v1"
    __secret_key = settings.TOSS_SECRET_KEY
    __encode_key: str

    def __init__(self):
        import base64

        secret_string = self.__secret_key + ":"
        __encoded_secret = secret_string.encode("ascii")
        self.__encode_key = base64.b64encode(__encoded_secret).decode("ascii")

    def __post(self, url, headers, body=None, parameter=None):
        import requests

        destination = self.__url + url
        response = requests.post(url=destination, headers=headers, json=body)

        return self.__interceptor(response)

    def __get(self, url, headers):
        import requests

        destination = self.__url + url
        response = requests.get(url=destination, headers=headers)

        return self.__interceptor(response)

    @staticmethod
    def __interceptor(response):
        import json

        if response.status_code == 500:
            raise ThirdPartyError(
                tag="TOSS", title="통신에러", message="토스 서버 오류", third_party="TOSS"
            )
        elif response.status_code == 400:
            result = json.loads(response.content)
            raise ThirdPartyError(
                tag="TOSS", title="서버에러", message=result["message"], third_party="TOSS"
            )
        elif response.status_code == 200:
            return json.loads(response.content)
        else:
            result = json.loads(response.content)
            raise ThirdPartyError(
                tag="TOSS", title="서버에러", message=result["message"], third_party="TOSS"
            )

    def create_sub_mall(self, command: CreateSubMallCommand) -> SubMall:
        headers = {"Authorization": "Basic " + self.__encode_key}
        converted_dict = {
            "subMallId": command.sub_mall_id,
            "account": {
                "bank": command.bank_code,
                "accountNumber": command.account_number,
                "holderName": command.account_depositor,
            },
            "type": command.bank_type,
            "email": command.email,
            "companyName": command.company_name,
            "representativeName": command.representative_name,
            "businessNumber": command.business_number,
            "phoneNumber": command.phone_number,
        }
        response = self.__post(
            url="/payouts/sub-malls", body=converted_dict, headers=headers
        )

        return response

    def update_sub_mall(self, command: UpdateSubMallCommand) -> SubMall:
        headers = {"Authorization": "Basic " + self.__encode_key}
        command.phone_number = command.phone_number.replace(" ", "")
        command.phone_number = command.phone_number.replace("+82", "0")
        command.phone_number = command.phone_number.replace("-", "")
        converted_dict = {
            "subMallId": command.sub_mall_id,
            "account": {
                "bank": command.bank_code,
                "accountNumber": command.account_number,
                "holderName": command.account_depositor,
            },
            "companyName": command.company_name,
            "representativeName": command.representative_name,
            "businessNumber": command.business_number,
            "email": command.email,
            "phoneNumber": command.phone_number,
        }
        response = self.__post(
            url=f"/payouts/sub-malls/{command.sub_mall_id}",
            body=converted_dict,
            headers=headers,
        )
        return response

    def delete_sub_mall(self, sub_mall_id):
        headers = {"Authorization": "Basic " + self.__encode_key}
        response = self.__post(
            url=f"/payouts/sub-malls/{sub_mall_id}/delete", headers=headers
        )
        return response

    def get_sub_mall(self) -> SubMall:
        headers = {"Authorization": "Basic " + self.__encode_key}
        response = self.__get(url="/payouts/sub-malls", headers=headers)
        return response
