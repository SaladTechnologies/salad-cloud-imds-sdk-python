```python
from salad_cloud_imds_sdk import SaladCloudImdsSdk, Environment
from salad_cloud_imds_sdk.models import ReallocateContainer

sdk = SaladCloudImdsSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = ReallocateContainer(
    reason="laborum culpa"
)

result = sdk.metadata.reallocate_container(request_body=request_body)

print(result)

```
