from rest_framework.status import (
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_403_FORBIDDEN,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_408_REQUEST_TIMEOUT,
    HTTP_404_NOT_FOUND,
)

class ServerErrorInterface(Exception):
    # 상세한 에러 코드를 위한 변수입니다.
    code: str = "0005"
    status_code: int = HTTP_500_INTERNAL_SERVER_ERROR

    # optional Debug용 메시지
    # debug_message : str = None

    def __init__(
        self, message: str = "알 수 없는 에러", title: str = "서버에러", tag: str = "ADMN"
    ):
        self.message = message
        self.title = title
        self.tag = tag
        self.__validate__()

    # 개발자가 tag와 code 선언을 하지 못했을 때, 검증을 위한 exception
    def __validate__(self) -> Exception:
        if self.tag is None or self.code is None or self.title is None:
            raise AssertionError()
        else:
            pass

    # 에러 발생 시 메시지를 넘기기 위한 함수
    def __str__(self) -> str:
        if self.message is None or self.code is None:
            raise NotImplementedError()
        return self.message


class LogicError(ServerErrorInterface):
    code = "0001"
    status_code = HTTP_400_BAD_REQUEST


class InputError(ServerErrorInterface):
    code = "0002"
    status_code = HTTP_400_BAD_REQUEST


class QueryError(ServerErrorInterface):
    code = "0003"
    status_code = HTTP_500_INTERNAL_SERVER_ERROR


class ValidationError(ServerErrorInterface):
    code = "0004"
    status_code = HTTP_400_BAD_REQUEST

    def __init__(
        self,
        message: str = "알 수 없는 에러",
        title: str = "서버에러",
        tag: str = "ADMN",
        error: str = None,
    ):
        self.error = error
        super().__init__(message=message, title=title, tag=tag)


class ServerError(ServerErrorInterface):
    code = "0005"
    status_code = HTTP_500_INTERNAL_SERVER_ERROR


class TypeError(ServerErrorInterface):
    code = "0006"
    status_code = HTTP_500_INTERNAL_SERVER_ERROR


class AuthenticationError(ServerErrorInterface):
    code = "0007"
    status_code = HTTP_401_UNAUTHORIZED


class TimeOutError(ServerErrorInterface):
    code = "0008"
    status_code = HTTP_408_REQUEST_TIMEOUT


class NetworkError(ServerErrorInterface):
    code = "0009"
    status_code = HTTP_500_INTERNAL_SERVER_ERROR


class AuthorityError(ServerErrorInterface):
    code = "0010"
    status_code = HTTP_403_FORBIDDEN


class ThirdPartyError(ServerErrorInterface):
    code = "0011"
    status_code = HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, message: str, title: str, tag: str, third_party: str):
        self.third_party = third_party
        super().__init__(message=message, title=title, tag=tag)


class NotFoundError(ServerErrorInterface):
    code = "0012"
    status_code = HTTP_404_NOT_FOUND
