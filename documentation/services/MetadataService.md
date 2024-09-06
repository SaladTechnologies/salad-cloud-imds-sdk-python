# MetadataService

A list of all methods in the `MetadataService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                             |
| :-------------------------------------------- | :------------------------------------------------------ |
| [reallocate_container](#reallocate_container) | Reallocates the running container to another Salad Node |
| [get_container_status](#get_container_status) | Gets the health statuses of the running container       |
| [get_container_token](#get_container_token)   | Gets the identity token of the running container        |

## reallocate_container

Reallocates the running container to another Salad Node

- HTTP Method: `POST`
- Endpoint: `/v1/reallocate`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [ReallocateContainer](../models/ReallocateContainer.md) | ✅       | The request body. |

**Example Usage Code Snippet**

```python
from salad_cloud_imds_sdk import SaladCloudImdsSdk, Environment
from salad_cloud_imds_sdk.models import ReallocateContainer

sdk = SaladCloudImdsSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = ReallocateContainer(
    reason="commodo"
)

result = sdk.metadata.reallocate_container(request_body=request_body)

print(result)
```

## get_container_status

Gets the health statuses of the running container

- HTTP Method: `GET`
- Endpoint: `/v1/status`

**Return Type**

`ContainerStatus`

**Example Usage Code Snippet**

```python
from salad_cloud_imds_sdk import SaladCloudImdsSdk, Environment

sdk = SaladCloudImdsSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.metadata.get_container_status()

print(result)
```

## get_container_token

Gets the identity token of the running container

- HTTP Method: `GET`
- Endpoint: `/v1/token`

**Return Type**

`ContainerToken`

**Example Usage Code Snippet**

```python
from salad_cloud_imds_sdk import SaladCloudImdsSdk, Environment

sdk = SaladCloudImdsSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.metadata.get_container_token()

print(result)
```
