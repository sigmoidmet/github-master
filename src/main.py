from github import Github
from github import Auth

from authentication import get_auth_token_if_exists, put_auth_token

if __name__ == "__main__":
    token = get_auth_token_if_exists()

    if not token:
        print("No authentication provided. Please, write down GitHub auth token with writes accesses to repos and "
              "workflows.")
        token = input()
        put_auth_token(token)

    auth = Auth.Token(token)
    g = Github(auth=auth)
    user = g.get_user()
    repo_name = "test-repo"
    repo = user.create_repo(repo_name)
    print(f"Repository {repo_name} successfully created.")
