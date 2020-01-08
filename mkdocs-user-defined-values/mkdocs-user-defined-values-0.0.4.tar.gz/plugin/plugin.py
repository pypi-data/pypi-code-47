from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

class UserDefinedValues(BasePlugin):

    config_scheme = (
        ('keywords', config_options.Type(dict)),
        ('input-placeholder', config_options.Type(mkdocs_utils.string_types, default='{{{user-defined-values}}}'))
    )

    def on_config(self, config, **kwards):
        self.data_tag = 'data-bind-user-defined-values'
        self.keywords = {}

        # Sanatise all keywords to be Dictionary. By default MkDocs assigns None as a value for Keys if they are empty
        for key, value in self.config['keywords'].items():
            self.keywords[key] = value if isinstance(value, dict) else {}

        return config

    def on_post_page(self, output_content, page, config):
        # Wrap keyword with span and data tag
        for keyword in self.keywords:
            output_content = output_content.replace(keyword, f'<span {self.data_tag}="{keyword}">{keyword}</span>')

        # Embed binding javascript
        input_boxes = '''
            <style>
                label.user-defined-values {
                    width: 30%
                }

                input.user-defined-values[type=text] {
                    width: 100%;
                    padding: 12px 20px;
                    margin: 8px 0;
                    box-sizing: border-box;
                    border: 1px solid black;
                    display: inline-block;
                }
            </style>

            <script>
                function createEventListener(userDefinedKey, dataTag) {
                    const domElement = document.getElementById(userDefinedKey);
                    domElement.value = window.localStorage.getItem(userDefinedKey);

                    domElement.addEventListener("input", event => {
                        const value = event.target.value;
                        window.localStorage.setItem(userDefinedKey, value);
                        document.querySelectorAll('[' + dataTag + '=' + userDefinedKey + ']').forEach((element, _) => {
                            if (value == '') {
                                element.innerHTML = userDefinedKey;
                            } else {
                                element.innerHTML = value;
                            }
                        });
                    });

                    document.addEventListener("DOMContentLoaded", () => {
                        domElement.dispatchEvent(new Event("input"));
                    });
                }
            </script>
        '''

        for keyword, values in self.keywords.items():
            label = keyword
            placeholder = ''

            if values:
                label = values.get('label', label)
                placeholder = values.get('placeholder', placeholder)

            input_boxes += f'''
                <label class="user-defined-values" for="{keyword}">{label}</label>
                <input class="user-defined-values" type="text" placeholder="{placeholder}" id="{keyword}" />
                <script>
                    createEventListener("{keyword}", "{self.data_tag}");
                </script>
            '''

        output_content = output_content.replace(self.config['input-placeholder'], input_boxes)

        return output_content