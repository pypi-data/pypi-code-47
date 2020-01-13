from github import Github, Repository


def create(key, repository, title, description, head, base='master', reviewer=None, label=None, *_):
    g = Github(key)
    repo_obj = g.get_repo(repository)  # type: Repository.Repository
    pr = repo_obj.create_pull(
        title=title,
        body=description,
        head=head,
        base=base,
    )
    if label:
        pr.add_to_labels(*label)
    if reviewer:
        pr.add_to_assignees(*reviewer)
        pr.create_review_request(reviewers=reviewer)
