from dataclasses import dataclass


@dataclass
class CreateSubMallCommand:
    sub_mall_id: str
    bank_code: str
    account_number: str
    account_depositor: str
    email: str
    phone_number: str
    company_name: str | None
    representative_name: str | None
    representative_number: str | None
    business_number: str | None
    bank_type: str | int = 0
