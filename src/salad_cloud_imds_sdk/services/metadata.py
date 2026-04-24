from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    DeletionCost,
    Metadata,
    ReallocatePrototype,
    SaladCloudImdsError,
    Status,
    Token,
)


class MetadataService(BaseService):
    """
    Service class for MetadataService operations.
    Provides methods to interact with MetadataService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    @cast_models
    def get_deletion_cost(self, metadata: Metadata) -> DeletionCost:
        """Gets the deletion cost of the current container instance

        :param metadata: A custom request header required by all operations.
        :type metadata: Metadata
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: DeletionCost
        """

        Validator(Metadata).validate(metadata)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/v1/deletion-cost",
            )
            .add_header("Metadata", metadata)
            .add_error(403, SaladCloudImdsError)
            .add_error(404, SaladCloudImdsError)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return DeletionCost._unmap(response)

    @cast_models
    def replace_deletion_cost(
        self, request_body: DeletionCost, metadata: Metadata
    ) -> None:
        """Replaces the deletion cost of the current container instance

        :param request_body: The request body.
        :type request_body: DeletionCost
        :param metadata: A custom request header required by all operations.
        :type metadata: Metadata
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: None
        """

        Validator(DeletionCost).validate(request_body)
        Validator(Metadata).validate(metadata)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/v1/deletion-cost",
            )
            .add_header("Metadata", metadata)
            .add_error(400, SaladCloudImdsError)
            .add_error(403, SaladCloudImdsError)
            .add_error(404, SaladCloudImdsError)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def reallocate(self, request_body: ReallocatePrototype, metadata: Metadata) -> None:
        """Reallocates the current container instance to another SaladCloud node

        :param request_body: The request body.
        :type request_body: ReallocatePrototype
        :param metadata: A custom request header required by all operations.
        :type metadata: Metadata
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: None
        """

        Validator(ReallocatePrototype).validate(request_body)
        Validator(Metadata).validate(metadata)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/v1/reallocate",
            )
            .add_header("Metadata", metadata)
            .add_error(400, SaladCloudImdsError)
            .add_error(403, SaladCloudImdsError)
            .add_error(404, SaladCloudImdsError)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def recreate(self, metadata: Metadata) -> None:
        """Recreates the current container instance on the same SaladCloud node

        :param metadata: A custom request header required by all operations.
        :type metadata: Metadata
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: None
        """

        Validator(Metadata).validate(metadata)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/v1/recreate",
            )
            .add_header("Metadata", metadata)
            .add_error(400, SaladCloudImdsError)
            .add_error(403, SaladCloudImdsError)
            .add_error(404, SaladCloudImdsError)
            .serialize()
            .set_method("POST")
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def restart(self, metadata: Metadata) -> None:
        """Restarts the current container instance on the same SaladCloud node

        :param metadata: A custom request header required by all operations.
        :type metadata: Metadata
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: None
        """

        Validator(Metadata).validate(metadata)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/v1/restart",
            )
            .add_header("Metadata", metadata)
            .add_error(400, SaladCloudImdsError)
            .add_error(403, SaladCloudImdsError)
            .add_error(404, SaladCloudImdsError)
            .serialize()
            .set_method("POST")
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def get_status(self, metadata: Metadata) -> Status:
        """Gets the health statuses of the current container instance

        :param metadata: A custom request header required by all operations.
        :type metadata: Metadata
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Status
        """

        Validator(Metadata).validate(metadata)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/v1/status",
            )
            .add_header("Metadata", metadata)
            .add_error(403, SaladCloudImdsError)
            .add_error(404, SaladCloudImdsError)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return Status._unmap(response)

    @cast_models
    def get_token(self, metadata: Metadata) -> Token:
        """Gets the identity token of the current container instance

        :param metadata: A custom request header required by all operations.
        :type metadata: Metadata
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Token
        """

        Validator(Metadata).validate(metadata)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/v1/token",
            )
            .add_header("Metadata", metadata)
            .add_error(403, SaladCloudImdsError)
            .add_error(404, SaladCloudImdsError)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return Token._unmap(response)
