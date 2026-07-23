import requests
import json
def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"User '{username}' not found!")
            return None
        else:
            print(f"Unexpected error: {response.status_code}")
            return None
    except requests.exceptions.ConnectionError:
        print("Check your internet connection!")
        return None
    except requests.exceptions.Timeout:
        print("Request timed out!")
        return None
def display_user(data):
    if data is None:
        return
    print("\n" + "="*40)
    print(f"  GitHub User Profile")
    print("="*40)
    print(f"  Username  : {data['login']}")
    print(f"  Name      : {data.get('name', 'Not provided')}")
    print(f"  Location  : {data.get('location', 'Not provided')}")
    print(f"  Bio       : {data.get('bio', 'Not provided')}")
    print(f"  Followers : {data['followers']}")
    print(f"  Following : {data['following']}")
    print(f"  Repos     : {data['public_repos']}")
    print("="*40)
username = input("Enter GitHub username: ")
user_data = get_github_user(username)
display_user(user_data)