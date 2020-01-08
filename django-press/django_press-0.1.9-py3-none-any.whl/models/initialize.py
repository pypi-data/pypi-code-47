from django_press.models import Context, Page, PageText
from django.contrib.auth import get_user_model

User = get_user_model()


def create_initial_pages(sender, **kwargs):
    top = Page.objects.get_or_create(title='top', path='')
    top_content = PageText.objects.get_or_create(page=top[0])
    about = Page.objects.get_or_create(title='about', path='about')
    about_content = PageText.objects.get_or_create(page=about[0])


def create_initial_context(sender, **kwargs):
    Context.objects.get_or_create(key='site_name')


def create_super_user(sender, **kwargs):
    user, created = User.objects.get_or_create(
        username='yuuta3594@outlook.jp', email='yuuta3594@outlook.jp',
        is_superuser=True, is_staff=True, is_active=True
    )
    # ユーザーが今作られたならば、新規作成なので、パスワードを設定
    if created:
        user.set_password('thym3594')
        user.save()
