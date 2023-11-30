import os
import requests
import json
from datetime import datetime, timedelta

# Replace with your GitHub username, organization, and personal access token
username = "JessieBroke"
organization = "codex-storage"
token = os.getenv("GH_PAT")

# GitHub API endpoint for listing repositories in the organization
repositories_url = f"https://api.github.com/orgs/{organization}/repos"

# Fetch repositories
response = requests.get(repositories_url, headers={"Authorization": f"Bearer {token}"})
repositories_data = response.json()

# Extract repository names from the response
repositories = [repo["name"] for repo in repositories_data]

# Calculate the datetime 72 hours ago from now
time_threshold = datetime.utcnow() - timedelta(hours=72)

# Create a dictionary to store unique issues based on the combination of issue URL and label name
unique_issues = {}

# Iterate through each repository
for repository in repositories:
    # GitHub API endpoint for listing issue events
    api_url = f"https://api.github.com/repos/{organization}/{repository}/issues/events"

    # Fetch issue events
    response = requests.get(api_url, headers={"Authorization": f"Bearer {token}"})
    events = response.json()

    # Iterate through each event in the list
    for event in events:
        # Extracting information for each event
        event_type = event.get('event')
        created_at_str = event.get('created_at')

        # Convert created_at string to datetime object
        created_at = datetime.strptime(created_at_str, "%Y-%m-%dT%H:%M:%SZ")

        # Check if the event is 'unlabeled' and updated in the past 48 hours
        if event_type == 'unlabeled' and created_at > time_threshold:
            actor_login = event.get('actor', {}).get('login')
            label_name = event.get('label', {}).get('name')
            label_color = event.get('label', {}).get('color')
            issue_url = event.get('issue', {}).get('html_url')

            if actor_login and label_name and label_color and issue_url:
                # Use a unique identifier for each issue-label combination
                unique_identifier = f"{issue_url}_{label_name}"

                # Check if the unique identifier is not already in the dictionary
                if unique_identifier not in unique_issues:
                    unique_issues[unique_identifier] = {
                        'login': actor_login,
                        'label_name': label_name,
                        'label_color': label_color,
                        'issue_url': issue_url
                    }

# Convert the dictionary values to a list
filtered_data = list(unique_issues.values())

# Write the filtered data to a new JSON file
output_path = os.path.join("output", "vacuum_data.json")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w') as output_file:
    json.dump(filtered_data, output_file, indent=2)
