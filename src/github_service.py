from github import Github, BadCredentialsException
from github import Auth

from authentication import AuthenticationProvider


class GithubService:
    def __init__(self, authentication_provider: AuthenticationProvider, max_login_attempts=3):
        self.__max_login_attempts = max_login_attempts
        self.__github = None
        self.__authenticationProvider = authentication_provider
        token = authentication_provider.get_auth_token_if_exists()

        if token is None:
            token = authentication_provider.auth()

        self.activate_github(token)

    def create_repository(self, name):
        user = self.__github.get_user()
        self.__do_action(lambda: user.create_repo(name))

    def __do_action(self, action, attempts=0):
        try:
            action()
        except BadCredentialsException as e:
            if attempts > self.__max_login_attempts:
                raise e
            token = self.__authenticationProvider.auth()
            self.activate_github(token)
            self.__do_action(action, attempts + 1)

    def activate_github(self, token):
        auth = Auth.Token(token)
        self.__github = Github(auth=auth)

