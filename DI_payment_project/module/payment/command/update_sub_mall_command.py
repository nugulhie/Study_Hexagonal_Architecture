from dataclasses import dataclass
from util.STATIC_LITERAL_VALUE import ACCOUNT_TYPE


@dataclass
class UpdateSubMallCommand:
    sub_mall_id: str
    bank_code: str
    account_number: str
    account_depositor: str
    company_name: str | None = None
    representative_name: str | None = None
    representative_number: str | None = None
    business_number: str | None = None
    email: str | None = None
    phone_number: str | None = None
    account_type: str | None = ACCOUNT_TYPE[0]  # CORPORATE
