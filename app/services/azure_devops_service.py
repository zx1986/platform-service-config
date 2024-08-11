import os
os.environ['AZURE_DEVOPS_CACHE_DIR'] = '/tmp'

from azure.devops.connection import Connection
from azure.devops.v7_1.work_item_tracking import WorkItemTrackingClient
from azure.devops.v7_1.git import GitClient
from azure.devops.v7_1.work_item_tracking.models import JsonPatchOperation
from msrest.authentication import BasicAuthentication

# Authentication
personal_access_token = os.getenv('AZURE_DEVOPS_PAT')
if not personal_access_token:
    raise EnvironmentError("AZURE_DEVOPS_PAT is not set in the environment variables")
organization_url = os.getenv('AZURE_DEVOPS_URL', 'https://dev.azure.com/zx1986')
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)
import code; code.interact(local=dict(globals(), **locals()))

# Access Work Item Tracking service
work_item_client = connection.clients.get_work_item_tracking_client()

# List Work Items
wiql = "SELECT [System.Id], [System.Title], [System.State] FROM workitems WHERE [System.WorkItemType] = 'Task'"
query_result = work_item_client.query_by_wiql(wiql).work_items


work_items = []
for item in query_result:
    work_item = work_item_client.get_work_item(item.id)
    work_items.append(work_item)

print("Work Items:")
for work_item in work_items:
    print(f"ID: {work_item.id}, Title: {work_item.fields['System.Title']}, State: {work_item.fields['System.State']}")

# Create a Work Item
document = [
    JsonPatchOperation(
        op='add',
        path='/fields/System.Title',
        value='New Task from API'
    ),
    JsonPatchOperation(
        op='add',
        path='/fields/System.Description',
        value='This task was created using the azure-devops Python library'
    )
]
project = 'hchangz'
new_work_item = work_item_client.create_work_item(document, project, 'Task')
print(f"Created work item: {new_work_item.id}")

# Access Git service and list repositories
git_client = connection.clients.get_git_client()
repositories = git_client.get_repositories(project=project)

print("\nRepositories:")
for repo in repositories:
    print(f"Repo Name: {repo.name}, ID: {repo.id}")
