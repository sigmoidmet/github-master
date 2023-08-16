# github-master
A tool that allows a creation of a GitHub repositories with ease

## Credentials
You can authorise by providing GitHub classic auth token with repos and workflows write scopes.
Also, you may provide expiration date so the app could warn you about it and check it beforehand, but it's not mandatory.
This information will be stored in ~/.github-master/.credentials file.

## Commands

### **github-master create** [repository-name] 
Creates a repository

### **github-master auth** [--redirect] 
Authenticates a GitHub account
**--redirect** - opens a GitHub web page with preset authentication token scopes.