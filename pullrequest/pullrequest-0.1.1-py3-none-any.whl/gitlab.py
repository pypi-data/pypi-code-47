from gitlab import Gitlab


def create(key, repository, title, description, head, base='master', close_source_branch=False, reviewer=None,
           label=None, url='https://gitlab.com/', *_):
    if not reviewer:
        reviewer = []
    gl = Gitlab(url=url, private_token=key)
    assignee_ids = [
        gl_id(r, gl.users, 'username')
        for r
        in reviewer
    ]
    project_id = gl_id(repository, gl.projects)
    project = gl.projects.get(project_id)
    project.mergerequests.create({
        'title': title,
        'description': description,
        'source_branch': head,
        'target_branch': base,
        'label': label,
        'assignee_ids': assignee_ids,
        'remove_source_branch': close_source_branch,
    })


def is_integral(var):
    try:
        int(var)
        return True
    except ValueError:
        return False


def gl_id(name, objects, field='name'):
    if is_integral(name):
        return name
    results = objects.list(**{field: name})
    return results[0].id if results else name
