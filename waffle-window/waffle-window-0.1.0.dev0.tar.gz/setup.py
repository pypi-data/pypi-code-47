# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['waffle_window',
 'waffle_window.management',
 'waffle_window.management.commands',
 'waffle_window.migrations']

package_data = \
{'': ['*']}

install_requires = \
['django-waffle>=0.19.0,<0.20.0', 'django>=2.2,<4.0']

setup_kwargs = {
    'name': 'waffle-window',
    'version': '0.1.0.dev0',
    'description': 'Django app for managing user groups and django-waffle flags.',
    'long_description': '# django-waffle-window\n\nDjango app for managing time-bound django-waffle user-flag membership.\n\n## Background\n\nIf you have used `django-waffle` for managing feature flags, you will probably have come across the\nchallenge of managing which users have access to which flags at what point in time. The underlying\nmodel allows you to assign individual users or groups to a flag, leaving you to manage how and when\nto add users to a flag, or remove users from a flag. Take the following use case:\n\n    Give access to user A to feature B for 30 days, starting Monday.\n\nThis use case can be challenging to manage at scale. Someone has to remember to turn the flag, and\nthen again to turn it off (which means, in practice, removing the user from the flag, or the\nflag-enabled group).\n\nThis app attempts to tackle this problem by adding a `FlagMember` model that enables you to set a\ndate window within which a user will be added to a flag, and outside of which they will be removed.\nThe add / remove process is managed via management command.\n\n```\n$ python manage.py update_flag_membership\n```\n\n### Implementation\n\nThe flag membership is managed using Django Groups. For each flag, a related group called\n`WAFFLE_<flag_name>` is created, and assigned to the flag. The management command then runs through\neach flag, checks the `FlagMember` table for users who are assigned to the flag _on that date_, and\nassigns them to the relevant group. The user membership window is defined through\n`FlagMember.start_date` and `FlagMember.end_date`.\n\n```python\nclass FlagMemberQuerySet(QuerySet):\n\n    def active(flag_name: str) -> FlagMemberQuerySet:\n        """Return all users assigned to the flag today."""\n        on_date = datetime.date.today()\n        return self.filter(\n            name=flag_name,\n            start_date__gte=on_date,\n            end_date__lte=on_date\n        )\n```\n\nEach `FlagMember` object can sync its own membership:\n\n```python\n>>> member = FlagMember(user, flag_name, start_date, end_date)\n>>> member.save()  # save object, but do not add to group\n>>> member.sync()  # add to / remove from group as appropriate\n```\n\nThe scheduler clears the entire group and re-adds those members who are active.\n\n```python\ndef _get_or_create_flag_group(flag_name: str) -> Group:\n    flag = Flag.objects.get(name=flag_name)\n    group = Group.objects.get_or_create(name=f"WAFFLE_{flag_name}")\n    flag.group_set.add(group)\n    return group\n\ndef sync_flag_membership(flag_name: str) -> None:\n    """Update the flag group with all members of the queryset."""\n    active_members = FlagMember.objects.active(flag_name)\n    group = _get_or_create_flag_group(flag_name)\n    group.user_set.clear()\n    group.add(*active_members)  # this won\'t scale for large querysets\n```\n\nThe management command updates all Flags:\n\n```python\nclass Command(BaseCommand):\n\n    def handle(self, *args, **options):\n        for flag in Flag.objects.all():\n            sync_flag_membership(flag.name)\n\n```\n',
    'author': 'YunoJuno',
    'author_email': 'code@yunojuno.com',
    'maintainer': 'YunoJuno',
    'maintainer_email': 'code@yunojuno.com',
    'url': 'https://github.com/yunojuno/django-waffle-window',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
