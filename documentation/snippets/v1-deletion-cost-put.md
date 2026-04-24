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
