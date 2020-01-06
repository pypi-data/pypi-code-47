import json

def getTranslations():
    translations = {}
    with open('bible-translations.json', 'r') as file:
        translations = json.loads(file.read())

    return translations

def parse(version_to_parse):
    version_to_parse = version_to_parse.lower()
    versions = getTranslations()

    data = {}
    for version in versions:
        if version['name'].lower() == version_to_parse or version['abbr'].lower() == version_to_parse:
            data = version

        else:
            for alias in version['aliases']:
                if alias.lower() == version_to_parse:
                    data = version

    return data

def getAll(field, value):
    versions = getTranslations()

    data = []
    for version in versions:
        try:
            if version[field].lower() == value.lower():
                data.append(version)

        except KeyError: # some translations don't have certain information, thus raising a KeyError
            continue

    return data
