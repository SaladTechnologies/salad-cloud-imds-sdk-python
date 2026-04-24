```python
from salad_cloud_imds_sdk import SaladCloudImdsSdk
from salad_cloud_imds_sdk.models import Metadata

sdk = SaladCloudImdsSdk(
    timeout=10000
)

result = sdk.metadata.get_token(metadata="true")

print(result)

```
