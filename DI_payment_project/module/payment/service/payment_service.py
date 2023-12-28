from ..adapter.toss_payments import TossPaymentAdapter
from ..command.create_sub_mall_command import CreateSubMallCommand
from ..command.update_sub_mall_command import UpdateSubMallCommand
from ..domain.sub_mall import SubMall
from ..port.inbound.payment_port import PaymentUseCase
from ..port.outbound.pg_port import PgPort


class PaymentService(PaymentUseCase):
	__pg_port: PgPort

	def __init__(self, pg_port: PgPort):
		self.__pg_port = pg_port

	def create_sub_mall(self, command: CreateSubMallCommand) -> SubMall:
		return self.__pg_port.create_sub_mall(command)

	def update_sub_mall(self, command: UpdateSubMallCommand) -> SubMall:
		return self.__pg_port.update_sub_mall(command)

	def delete_sub_mall(self, sub_mall_id):
		if isinstance(self.__pg_port, TossPaymentAdapter):
			return self.__pg_port.delete_sub_mall(sub_mall_id)
		else:
			pass

	def get_sub_mall(self) -> SubMall:
		if isinstance(self.__pg_port, TossPaymentAdapter):
			return self.__pg_port.get_sub_mall()

		else:
			pass

	@staticmethod
	def get_bank_code():
		return {
			"02": "한국산업은행",
			"03": "기업은행",
			"04": "국민은행",
			"05": "하나은행(구 외환)",
			"06": "국민은행(구 주택)",
			"07": "수협중앙회",
			"11": "농협중앙회",
			"12": "단위농협",
			"16": "축협중앙회",
			"20": "우리은행",
			"21": "구)조흥은행",
			"22": "상업은행",
			"23": "SC제일은행",
			"24": "한일은행",
			"25": "서울은행",
			"26": "구)신한은행",
			"27": "한국씨티은행",
			"31": "대구은행",
			"32": "부산은행",
			"34": "광주은행",
			"35": "제주은행",
			"37": "전북은행",
			"38": "강원은행",
			"39": "경남은행",
			"41": "비씨카드",
			"45": "새마을금고",
			"48": "신협",
			"50": "상호저축은행",
			"53": "씨티은행",
			"54": "홍콩상하이은행",
			"55": "도이치은행",
			"56": "ABN암로",
			"57": "JP모건",
			"59": "미쓰비시도쿄은행",
			"60": "BOA(Bank Of America)",
			"64": "산림조합",
			"70": "신안상호저축은행",
			"71": "우체국",
			"81": "KEB 하나은행",
			"83": "평화은행",
			"87": "신세계",
			"88": "신한은행",
			"89": "케이뱅크",
			"90": "카카오뱅크",
			"92": "토스뱅크",
		}
