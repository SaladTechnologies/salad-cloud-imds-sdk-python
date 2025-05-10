```python
from salad_cloud_imds_sdk import SaladCloudImdsSdk
from salad_cloud_imds_sdk.models import ReallocatePrototype

sdk = SaladCloudImdsSdk(
    timeout=10000
)

request_body = ReallocatePrototype(
    reason="Insufficient VRAM"
)

result = sdk.metadata.reallocate(request_body=request_body)

print(result)

```
