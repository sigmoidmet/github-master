import json
import os.path

__credentials_file = "~/.github-master/.credentials.json"
__default_profile = "default"
__token_field = "token"
__expire_at_field = "expireAt"


def get_auth_token_if_exists(profile=__default_profile) -> str:
    return get_credentials().get(profile, {}).get(__token_field)


def put_auth_token(token: str, expire_at=None, profile=__default_profile):
    creds = get_credentials()

    creds[profile] = {
        __token_field: token,
        __expire_at_field: expire_at
    }

    with open(__credentials_file, "w+") as f:
        f.write(json.dumps(creds))


def get_credentials() -> dict:
    os.makedirs(os.path.dirname(__credentials_file), exist_ok=True)
    if not os.path.exists(__credentials_file):
        return {}
    with open(__credentials_file, "r") as f:
        return json.loads(f.read())
