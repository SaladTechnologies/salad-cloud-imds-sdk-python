from typing import Awaitable, Union
from .utils.to_async import to_async
from ..metadata import MetadataService
from ...models import DeletionCost, Metadata, ReallocatePrototype, Status, Token


class MetadataServiceAsync(MetadataService):
    """
    Async Wrapper for MetadataServiceAsync
    """

    def get_deletion_cost(self, metadata: Metadata) -> Awaitable[DeletionCost]:
        return to_async(super().get_deletion_cost)(metadata)

    def replace_deletion_cost(
        self, request_body: DeletionCost, metadata: Metadata
    ) -> Awaitable[None]:
        return to_async(super().replace_deletion_cost)(request_body, metadata)

    def reallocate(
        self, request_body: ReallocatePrototype, metadata: Metadata
    ) -> Awaitable[None]:
        return to_async(super().reallocate)(request_body, metadata)

    def recreate(self, metadata: Metadata) -> Awaitable[None]:
        return to_async(super().recreate)(metadata)

    def restart(self, metadata: Metadata) -> Awaitable[None]:
        return to_async(super().restart)(metadata)

    def get_status(self, metadata: Metadata) -> Awaitable[Status]:
        return to_async(super().get_status)(metadata)

    def get_token(self, metadata: Metadata) -> Awaitable[Token]:
        return to_async(super().get_token)(metadata)
