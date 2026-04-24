# MetadataService

A list of all methods in the `MetadataService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description                                                           |
| :---------------------------------------------- | :-------------------------------------------------------------------- |
| [get_deletion_cost](#get_deletion_cost)         | Gets the deletion cost of the current container instance              |
| [replace_deletion_cost](#replace_deletion_cost) | Replaces the deletion cost of the current container instance          |
| [reallocate](#reallocate)                       | Reallocates the current container instance to another SaladCloud node |
| [recreate](#recreate)                           | Recreates the current container instance on the same SaladCloud node  |
| [restart](#restart)                             | Restarts the current container instance on the same SaladCloud node   |
| [get_status](#get_status)                       | Gets the health statuses of the current container instance            |
| [get_token](#get_token)                         | Gets the identity token of the current container instance             |

## get_deletion_cost

Gets the deletion cost of the current container instance

- HTTP Method: `GET`
- Endpoint: `/v1/deletion-cost`

**Parameters**

| Name     | Type                              | Required | Description                                         |
| :------- | :-------------------------------- | :------- | :-------------------------------------------------- |
| metadata | [Metadata](../models/Metadata.md) | ✅       | A custom request header required by all operations. |

**Return Type**

`DeletionCost`

**Example Usage Code Snippet**

```python
from salad_cloud_imds_sdk import SaladCloudImdsSdk
from salad_cloud_imds_sdk.models import Metadata

sdk = SaladCloudImdsSdk(
    timeout=10000
)

result = sdk.metadata.get_deletion_cost(metadata="true")

print(result)
```

## replace_deletion_cost

Replaces the deletion cost of the current container instance

- HTTP Method: `PUT`
- Endpoint: `/v1/deletion-cost`

**Parameters**

| Name         | Type                                      | Required | Description                                         |
| :----------- | :---------------------------------------- | :------- | :-------------------------------------------------- |
| request_body | [DeletionCost](../models/DeletionCost.md) | ✅       | The request body.                                   |
| metadata     | [Metadata](../models/Metadata.md)         | ✅       | A custom request header required by all operations. |

**Return Type**

`SaladCloudImdsError`

**Example Usage Code Snippet**

```python
from salad_cloud_imds_sdk import SaladCloudImdsSdk
from salad_cloud_imds_sdk.models import DeletionCost, Metadata

sdk = SaladCloudImdsSdk(
    timeout=10000
)

request_body = DeletionCost(
    deletion_cost=100
)

result = sdk.metadata.replace_deletion_cost(
    request_body=request_body,
    metadata="true"
)

print(result)
```

## reallocate

Reallocates the current container instance to another SaladCloud node

- HTTP Method: `POST`
- Endpoint: `/v1/reallocate`

**Parameters**

| Name         | Type                                                    | Required | Description                                         |
| :----------- | :------------------------------------------------------ | :------- | :-------------------------------------------------- |
| request_body | [ReallocatePrototype](../models/ReallocatePrototype.md) | ✅       | The request body.                                   |
| metadata     | [Metadata](../models/Metadata.md)                       | ✅       | A custom request header required by all operations. |

**Return Type**

`SaladCloudImdsError`

**Example Usage Code Snippet**

```python
from salad_cloud_imds_sdk import SaladCloudImdsSdk
from salad_cloud_imds_sdk.models import ReallocatePrototype, Metadata

sdk = SaladCloudImdsSdk(
    timeout=10000
)

request_body = ReallocatePrototype(
    reason="Insufficient VRAM"
)

result = sdk.metadata.reallocate(
    request_body=request_body,
    metadata="true"
)

print(result)
```

## recreate

Recreates the current container instance on the same SaladCloud node

- HTTP Method: `POST`
- Endpoint: `/v1/recreate`

**Parameters**

| Name     | Type                              | Required | Description                                         |
| :------- | :-------------------------------- | :------- | :-------------------------------------------------- |
| metadata | [Metadata](../models/Metadata.md) | ✅       | A custom request header required by all operations. |

**Return Type**

`SaladCloudImdsError`

**Example Usage Code Snippet**

```python
from salad_cloud_imds_sdk import SaladCloudImdsSdk
from salad_cloud_imds_sdk.models import Metadata

sdk = SaladCloudImdsSdk(
    timeout=10000
)

result = sdk.metadata.recreate(metadata="true")

print(result)
```

## restart

Restarts the current container instance on the same SaladCloud node

- HTTP Method: `POST`
- Endpoint: `/v1/restart`

**Parameters**

| Name     | Type                              | Required | Description                                         |
| :------- | :-------------------------------- | :------- | :-------------------------------------------------- |
| metadata | [Metadata](../models/Metadata.md) | ✅       | A custom request header required by all operations. |

**Return Type**

`SaladCloudImdsError`

**Example Usage Code Snippet**

```python
from salad_cloud_imds_sdk import SaladCloudImdsSdk
from salad_cloud_imds_sdk.models import Metadata

sdk = SaladCloudImdsSdk(
    timeout=10000
)

result = sdk.metadata.restart(metadata="true")

print(result)
```

## get_status

Gets the health statuses of the current container instance

- HTTP Method: `GET`
- Endpoint: `/v1/status`

**Parameters**

| Name     | Type                              | Required | Description                                         |
| :------- | :-------------------------------- | :------- | :-------------------------------------------------- |
| metadata | [Metadata](../models/Metadata.md) | ✅       | A custom request header required by all operations. |

**Return Type**

`Status`

**Example Usage Code Snippet**

```python
from salad_cloud_imds_sdk import SaladCloudImdsSdk
from salad_cloud_imds_sdk.models import Metadata

sdk = SaladCloudImdsSdk(
    timeout=10000
)

result = sdk.metadata.get_status(metadata="true")

print(result)
```

## get_token

Gets the identity token of the current container instance

- HTTP Method: `GET`
- Endpoint: `/v1/token`

**Parameters**

| Name     | Type                              | Required | Description                                         |
| :------- | :-------------------------------- | :------- | :-------------------------------------------------- |
| metadata | [Metadata](../models/Metadata.md) | ✅       | A custom request header required by all operations. |

**Return Type**

`Token`

**Example Usage Code Snippet**

```python
from salad_cloud_imds_sdk import SaladCloudImdsSdk
from salad_cloud_imds_sdk.models import Metadata

sdk = SaladCloudImdsSdk(
    timeout=10000
)

result = sdk.metadata.get_token(metadata="true")

print(result)
```
