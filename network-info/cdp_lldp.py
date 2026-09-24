import meraki
import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()

# Client
if "MERAKI_API" in os.environ:
    pass
else:
    sys.exit("Error: MERAKI_API needs to be defined")

dashboard = meraki.DashboardAPI(
    api_key = os.getenv("MERAKI_API"),
    output_log = False,
    print_console = False
)

org = dashboard.organizations.getOrganizations()
org_id = org[0].get("id")

# Serial numbers
devices = dashboard.organizations.getOrganizationDevices(org_id)
for device in devices:
    device_type = device.get("productType")
    if  device_type == "switch":
        print(json.dumps(device, indent=4))

# if "productType" == "switch":
#     print(net_device)

# # LLDP / CDP
# serials = []

# for serial in serials:
#     response = dashboard.devices.getDeviceLldpCdp(
#         serial
#     )

#     print (response)