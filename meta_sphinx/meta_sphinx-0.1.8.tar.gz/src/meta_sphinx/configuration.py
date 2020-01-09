import re
from pathlib import Path
from typing import Dict, List

import sphinx
import sphinx.application
import yaml

from slugify import slugify

from .get_metadata import get_package_metadata


def load_conf(directive_or_app: sphinx.application.Sphinx, *files):

    if not hasattr(directive_or_app.env, "meta_sphinx_configs"):
        directive_or_app.env.meta_sphinx_configs = {}

    for file in files:
        if file not in directive_or_app.env.meta_sphinx_configs:
            directive_or_app.env.meta_sphinx_configs[
                file
            ] = read_configuration_file(
                file,
                download_meta=True,
                project_type=directive_or_app.config.meta_sphinx_project_type,
            )

    return sum(directive_or_app.env.meta_sphinx_configs.values(), [])


def read_configuration_file(
    filepath: Path, download_meta: bool, project_type="Libraries"
):

    filepath = Path(filepath)

    with filepath.open() as f:
        conf = yaml.safe_load(f)

    for item in conf:
        if item["name"] in (
            "index",
            project_type.lower().replace(" ", "-"),
            "search",
        ):
            raise ValueError(
                f"{item['name']} is not a valid name as it clashes "
                + "with page names locally."
            )
        if download_meta:
            metadata = get_package_metadata(item["name"])
            item["package_metadata"] = metadata
            item.setdefault(
                "description", metadata.get("summary", "no summary available")
            )
            item.setdefault(
                "version", metadata.get("version", "no version available")
            )

        item.setdefault(
            "is_url", re.match(r"^http(s{0,1})://.*", item["path"]) is not None
        )

    return conf


def parse_languages(conf: List[Dict]) -> List[Dict]:
    outp = []
    for item in conf:
        item.setdefault("languages", [])
        if "language" in item and item["language"] not in item["languages"]:
            item["languages"].append(item["language"])
        item["language_slugs"] = [slugify(lang) for lang in item["languages"]]
        outp.append(item)
    return outp
