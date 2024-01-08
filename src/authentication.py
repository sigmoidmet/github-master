import json
import os.path


class AuthenticationService:
    __credentials_file = "~/.github-master/.credentials.json"
    __default_profile = "default"
    __token_field = "token"
    __expire_at_field = "expireAt"

    def __init__(self, profile=__default_profile):
        self.profile = profile

    def get_auth_token_if_exists(self) -> str:
        token = self.get_credentials().get(self.profile, {})

        return token.get(self.__token_field)

    def put_auth_token(self, token: str, expire_at=None, profile=__default_profile):
        creds = self.get_credentials()

        creds[profile] = {
            self.__token_field: token,
            self.__expire_at_field: expire_at
        }

        with open(self.__credentials_file, "w+") as f:
            f.write(json.dumps(creds))

    def get_credentials(self) -> dict:
        os.makedirs(os.path.dirname(self.__credentials_file), exist_ok=True)
        if not os.path.exists(self.__credentials_file):
            return {}
        with open(self.__credentials_file, "r") as f:
            return json.loads(f.read())


class AuthenticationProvider:
    def get_auth_token_if_exists(self):
        pass

    def auth(self) -> str:
        pass
