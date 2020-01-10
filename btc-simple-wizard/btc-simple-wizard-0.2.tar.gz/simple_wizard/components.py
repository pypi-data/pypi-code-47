from django.utils.html import format_html


class BaseButton:
    """
    Generic button class
    """

    html_string = '<%(tag)s class="%(css_classes)s" %(html_params)s>%(title)s</%(tag)s>'
    common_css_classes: list = []
    common_html_params: dict = {}
    tag: str = 'button'

    def __init__(self, title: str, css_classes: list = None, html_params: dict = None) -> None:
        self.title = self.format_title(title) or title
        self.html_params = dict(**self.common_html_params, **(html_params or {}))
        self.css_classes = [*self.common_css_classes, *(css_classes or [])]

    @staticmethod
    def prepare_html_params(html_params: dict) -> str:
        return ' '.join([f'{key}={value}' for key, value in html_params.items()])

    @staticmethod
    def prepare_css_classes(css_classes: list) -> str:
        return ' '.join(css_classes)

    def get_format_kwargs(self, **kwargs) -> dict:
        format_kwargs = dict(
            title=self.title,
            css_classes=self.prepare_css_classes(self.css_classes),
            html_params=self.prepare_html_params(self.html_params),
            tag=self.tag
        )
        format_kwargs.update(kwargs)
        return format_kwargs

    def format_title(self, title: str) -> str:
        pass

    @property
    def raw_string(self) -> str:
        return self.html_string % self.get_format_kwargs()

    def __str__(self) -> str:
        return format_html(self.raw_string)


class BaseWizardButton(BaseButton):
    """
    A base button class for load steps content
    """

    common_html_params = {'type': 'button'}

    def __init__(self,
                 load_step: str,
                 always_fetch: bool = False,
                 management_url: str = '',
                 method: str = 'get',
                 title: str = '',
                 css_classes: list = None,
                 html_params: dict = None):

        self.load_step = load_step
        self.always_fetch = always_fetch
        self.management_url = management_url
        self.method = method
        super().__init__(title, css_classes, html_params)

    def get_format_kwargs(self, **kwargs) -> dict:
        self.html_params.update({
            'data-step-unique-name': self.load_step,
            'data-always-fetch': str(self.always_fetch).lower(),
            'data-management-url': self.management_url,
            'data-method': self.method
        })
        return super().get_format_kwargs()


class LoadWizardStepButton(BaseWizardButton):
    """
    A button class for load steps content
    """

    common_css_classes = ['js-load_wizard']

    def __init__(self,
                 load_step: str,
                 always_fetch: bool = False,
                 management_url: str = '',
                 title: str = '',
                 css_classes: list = None,
                 html_params: dict = None):

        super().__init__(load_step, always_fetch, management_url, 'get', title, css_classes, html_params)


class LoadWizardStepPostButton(BaseWizardButton):
    """
    A button class for load steps content
    """

    common_css_classes = ['js-load_wizard']

    def __init__(self,
                 load_step: str,
                 management_url: str = '',
                 title: str = '',
                 css_classes: list = None,
                 html_params: dict = None):

        super().__init__(load_step, True, management_url, 'post', title, css_classes, html_params)


class CloseWizardModalButton(BaseButton):
    """
    A close button for close wizard modal
    """

    common_css_classes = ['js-close_wizard']
