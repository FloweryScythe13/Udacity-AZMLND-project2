from azureml.core import Workspace
from azureml.core.webservice import Webservice
from azureml.core.webservice.aci import AciWebservice

ws = Workspace.from_config()
print(ws)

my_service = "bankmarketingveclassifier"

deployed_service = AciWebservice(ws, my_service)
print("Service name: " + deployed_service.name)
print("Service state: " +deployed_service.state)

deployed_service.wait_for_deployment(show_output=True, timeout_sec=360.5)

deployed_service.update(enable_app_insights=True)