from github import Github

#lets user login
while True:
    username =  "duffyl9"
    password =  "41214121Lol"
    try:
        g = Github(username,password)
        user = g.get_user("duffyl9")
    except:
        print("Error. Please try again")
        continue
    else:
        break

def getRepoCommits():
    commits = []
    repo_commits = []
    for repo in user.get_repos():
        commit_count=0
        for commit in repo.get_commits():
            commit_count+=1
        #print(commit_count)
        repo_commits.append([repo.name, commit_count])
    return repo_commits

print(getRepoCommits())

