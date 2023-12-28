from urllib import parse

from ..port.outbound.pg_port import PgPort
from util.STATIC_LITERAL_VALUE import SUB_MALL, CREATE, UPDATE
from util.exception import ThirdPartyError, LogicError


class InicisAdapter(PgPort):
    __url = (
        "https://iniweb.inicis.com/DefaultWebApp/mall/cr/open/OpMallUrlConnection.jsp"
    )
    __mid: str
    __secret_key: str
    __key_file_pw: str

    def __init__(self):
        from django.conf import settings

        self.__mid = settings.INI_MID
        self.__secret_key = settings.INI_KEY
        self.__key_file_pw = settings.INI_KEY_FILE_PW

    def __post(self, url, headers, body=None, parameter=None):
        import requests

        response = requests.post(url=url, headers=headers, json=body)

        return self.__interceptor(response)

    def __get(self, url, headers):
        import requests

        destination = self.__url + url
        response = requests.get(url=destination, headers=headers)

        return self.__interceptor(response)

    @staticmethod
    def url_encoder(url, data):
        try:
            param = "&".join("%s=%s" % (k, v) for k, v in data.items())
            encoded_url = url + "?" + param
            return encoded_url
        except Exception as e:
            raise LogicError(
                tag="INICIS",
                message="오류가 발생했습니다.\n솔닥 고객센터로 문의해주시길 바랍니다.",
                title="서버 오류",
            )

    @staticmethod
    def __interceptor(response):

        try:
            result = response.text.replace("\r", "").replace("\n", "").split("&", 1)
            result_code = result[0].replace("resultcode=", "")
            result_msg = result[1].replace("resultmsg=", "")
            result = {"resultCode": result_code, "resultMsg": result_msg}
        except Exception as e:
            raise ThirdPartyError(
                tag="INICIS",
                title="서버에러",
                message="오류가 발생하였습니다.\n고객센터로 문의해주시길 바랍니다.",
                third_party="INICIS",
            )
        if result["resultCode"] == "00":
            return result
        else:
            title = "서버 오류"
            message = "오류가 발생하였습니다.\n고객센터로 문의해주시길 바랍니다."
            if result["resultCode"] == "01":
                message = "미등록된 IP에서 접근하였습니다."
            elif result["resultCode"] == "02":
                title = "입력 오류"
                message = "잘못된 값이 입력 되었습니다.\n입력 값을 확인해주세요."
            elif result["resultCode"] == "03":
                title = "이름 오류"
                message = result["resultMsg"][
                    result["resultMsg"].find(":") + 1 : len(result["resultMsg"]) - 1
                ]
                message = f"{message}"
            elif result["resultCode"] == "04":
                title = "계좌 오류"
                message = "이미 등록되어있는 계좌입니다.\n고객센터로 문의해주세요."
            elif result["resultCode"] == "05":
                title = "계좌 오류"
                message = "유효하지 않는 계좌입니다.\n계좌를 확인해 주세요."
            raise ThirdPartyError(
                tag="INICIS",
                title=title,
                message=message,
                third_party="INICIS",
            )

    def create_sub_mall(self, command):
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
        }
        convert_dict = {
            # Soldoc MID
            "id_merchant": self.__mid,
            # 서브몰 id
            "id_mall": command.sub_mall_id,
            # 등록 종류
            "cl_id": SUB_MALL,
            # 사업자 등록번호
            "no_comp": command.business_number,
            # 상호
            "nm_comp": parse.quote_plus(command.company_name, encoding="euc-kr"),
            # 대표자 이름
            "nm_boss": parse.quote_plus(command.representative_name, encoding="euc-kr"),
            # 예금주 이름
            "nm_regist": parse.quote_plus(command.account_depositor, encoding="euc-kr"),
            # 은행 코드
            "cd_bank": command.bank_code,
            # 계좌번호
            "no_acct": command.account_number,
            # 대표번호
            "no_tel": command.representative_number.replace("-", ""),
            # 생성 : 1, 수정 : 2
            "cl_gubun": CREATE,
        }
        request_url = self.url_encoder(url=self.__url, data=convert_dict)
        return self.__post(url=request_url, headers=headers)

    def update_sub_mall(self, command):
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
        }
        convert_dict = {
            # Soldoc MID
            "id_merchant": self.__mid,
            # 서브몰 id
            "id_mall": command.sub_mall_id,
            # 등록 종류
            "cl_id": SUB_MALL,
            # 사업자 등록번호
            "no_comp": command.business_number,
            # 상호
            "nm_comp": parse.quote_plus(command.company_name, encoding="euc-kr"),
            # 대표자 이름
            "nm_boss": parse.quote_plus(command.representative_name, encoding="euc-kr"),
            # 예금주 이름
            "nm_regist": parse.quote_plus(command.account_depositor, encoding="euc-kr"),
            # 은행 코드
            "cd_bank": command.bank_code,
            # 계좌번호
            "no_acct": command.account_number,
            # 대표번호
            "no_tel": command.representative_number.replace("-", ""),
            # 생성 : 1, 수정 : 2
            "cl_gubun": UPDATE,
        }
        request_url = self.url_encoder(url=self.__url, data=convert_dict)
        return self.__post(url=request_url, headers=headers)

    def delete_sub_mall(self, command):
        raise ThirdPartyError(
            tag="INICIS", message="지원하지 않는 기능입니다.", title="서버에러", third_party="INICIS"
        )

    def get_sub_mall(self, command):
        raise ThirdPartyError(
            tag="INICIS", message="지원하지 않는 기능입니다.", title="서버에러", third_party="INICIS"
        )
