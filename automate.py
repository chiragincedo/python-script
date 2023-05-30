import requests

def get_pull_request_diff_files(username, password, repository, pull_request_id):
    base_url = 'https://api.bitbucket.org/2.0'
    endpoint = f'/repositories/{repository}/pullrequests/{pull_request_id}/diffstat'
    url = base_url + endpoint
    auth = (username, password)

    # Send GET request to Bitbucket API
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        data = response.json()
        diff_files = data['values']
        return diff_files
    else:
        print(f"Failed to retrieve pull request diff files. Error: {response.text}")
        

def get_pull_requests(username, password, repository):
    base_url = 'https://api.bitbucket.org/2.0'
    endpoint = f'/repositories/{repository}/pullrequests'
    url = base_url + endpoint
    auth = (username, password)

    # Send GET request to Bitbucket API
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        data = response.json()
        pull_requests = data['values']
        return pull_requests
    else:
        print(f"Failed to retrieve pull requests. Error: {response.text}")

# Example usage
username = 'chirag220401'
password = 'ATBBxjZHPdLXBAqMCDMFmHhehrtr09F40C37'
repository = 'chirag-demo-project1/demo-repo1'

pull_requests = get_pull_requests(username, password, repository)
for pr in pull_requests:
    pr_id = pr['id']
    pr_title = pr['title']
    source_branch = pr['source']['branch']['name']
    destination_branch = pr['destination']['branch']['name']
    print(f"Pull Request #{pr_id}: {pr_title}")
    print(f"Source Branch: {source_branch}")
    print(f"Destination Branch: {destination_branch}")
    diff_files = get_pull_request_diff_files(username, password, repository, pr_id)
    for file in diff_files:
       filename = file['new']['path']
       print(f"File: {filename}")



