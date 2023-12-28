from dataclasses import dataclass


@dataclass
class SubMall:
    # 정산계좌 계좌번호
    account_number: str
    # 정산계좌 예금주
    account_depositor: str
    # 정산계좌 은행 코드
    bank_code: str
    # 대표자 이름
    representative_name: str
    # 대표 전화번호
    representative_number: str
    # 이메일
    email: str
    # 휴대전화 번호
    phone_number: str
    # 법인, 개인 구분
    type: str
    # SubMall Id
    sub_mall_id: str
    # 사업자 번호
    business_number: str = None
