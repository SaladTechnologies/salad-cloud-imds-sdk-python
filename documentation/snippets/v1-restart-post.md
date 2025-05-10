```python
from salad_cloud_imds_sdk import SaladCloudImdsSdk

sdk = SaladCloudImdsSdk(
    timeout=10000
)

result = sdk.metadata.restart()

print(result)

```
