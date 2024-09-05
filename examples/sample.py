from salad_cloud_imds_sdk import SaladCloudImdsSdk, Environment

sdk = SaladCloudImdsSdk(base_url=Environment.DEFAULT.value, timeout=10000)

result = sdk.metadata.get_container_status()

print(result)
