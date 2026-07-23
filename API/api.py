import requests

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    # Check if request succeeded
    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data.get('name', 'Not provided')}")
        print(f"Location: {data.get('location', 'Not provided')}")
        print(f"Public Repos: {data['public_repos']}")
        print(f"Followers: {data['followers']}")
    elif response.status_code == 404:
        print(f"User '{username}' not found!")
    else:
        print(f"Something went wrong. Status: {response.status_code}")

# Try it with different usernames
username = input("Enter a GitHub username: ")
get_github_user(username)