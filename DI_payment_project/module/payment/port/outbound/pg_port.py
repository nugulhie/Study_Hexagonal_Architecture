from typing import Protocol

from ...command.create_sub_mall_command import CreateSubMallCommand
from ...command.update_sub_mall_command import UpdateSubMallCommand
from ...domain.sub_mall import SubMall


class PgPort(Protocol):
    def create_sub_mall(self, command: CreateSubMallCommand) -> SubMall:
        raise NotImplementedError()

    def update_sub_mall(self, command: UpdateSubMallCommand) -> SubMall:
        raise NotImplementedError()

    def delete_sub_mall(self, sub_mall_id):
        raise NotImplementedError()

    def get_sub_mall(self) -> SubMall:
        raise NotImplementedError()
