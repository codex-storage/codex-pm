import os
import requests
import json

# Replace with your GitHub username, organization, repository, and personal access token
username = "JessieBroke"
organization = "codex-storage"
repository = "nim-codex"
token = os.getenv("GH_PAT")

# GitHub API endpoint for listing issue events
api_url = f"https://api.github.com/repos/{organization}/{repository}/issues/events"

# Fetch issue events
response = requests.get(api_url, headers={"Authorization": f"Bearer {token}"})
events = response.json()

# Save events to a JSON file
with open("issue_events.json", "w") as file:
    json.dump(events, file)

# Restore labels based on deletion events
for event in events:
    if event["event"] == "label":
        label_name = event["label"]["name"]
        # Restore the label using your preferred method (GitHub API, gh CLI, etc.)
        print(f"Restoring label: {label_name}")
        # Add logic here to restore the label using the GitHub API or other methods
