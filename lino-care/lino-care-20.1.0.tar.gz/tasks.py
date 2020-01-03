from atelier.invlib import setup_from_tasks
ns = setup_from_tasks(
    globals(), "lino_care",
    languages="en de fr et".split(),
    tolerate_sphinx_warnings=False,
    blogref_url='http://luc.lino-framework.org',
    revision_control_system='git',
    locale_dir='lino_care/lib/care/locale',
)
    # cleanable_files=['docs/api/lino_care.*'],

# The following demo databases use the database file of team, so there is no
# need initialize them:
#    - lino_care.projects.public.settings.demo
#    - lino_care.projects.bs3.settings.demo
