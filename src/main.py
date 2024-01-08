import webbrowser
from datetime import datetime

from arguments_parser import get_parser
from authentication import AuthenticationService, AuthenticationProvider
from github_service import GithubService


class CommandLineAuthenticationProvider(AuthenticationProvider):

    def __init__(self, authentication_service_arg: AuthenticationService, redirect: bool):
        self.__authentication_service = authentication_service_arg
        self.redirect = redirect

    def get_auth_token_if_exists(self):
        return self.__authentication_service.get_auth_token_if_exists()

    def on_bad_credentials(self) -> str:
        if self.redirect:
            self.send_to_auth_page()

        token = input()

        self.__authentication_service.put_auth_token(token)

        return token

    def send_to_auth_page(self):
        current_month = datetime.now().month
        current_year = datetime.now().year
        __url = f"https://github.com/settings/tokens/new?description=github-master-creds-{current_year}-{current_month}&scopes=repo%2Cworkflow"
        webbrowser.open(__url)


if __name__ == "__main__":
    parser = get_parser()

    args = parser.parse_args()

    if args.command == 'create' and args.repositoryName is None:
        parser.error("You need to provide repositoryName argument to create it")

    authentication_service = AuthenticationService()
    githubService = GithubService(CommandLineAuthenticationProvider(authentication_service, not args.noRedirect))

    if args.command == 'create':
        githubService.create_repository(args.repositoryName)
        print(f"Repository {args.repositoryName} successfully created.")
    else:
        print("Sorry, we don't support this yet")
