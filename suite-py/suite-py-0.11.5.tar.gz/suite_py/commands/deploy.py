from __future__ import print_function, unicode_literals
from ..lib.handler.youtrack_handler import YoutrackHandler
from ..lib.handler.github_handler import GithubHandler
from ..lib.handler.slack_handler import SlackHandler
from ..lib.handler import prompt_utils
from ..lib.logger import Logger
from ..lib.config import Config
import sys
import semver

youtrack = YoutrackHandler()
github = GithubHandler()
config = Config().load()
logger = Logger()
slack = SlackHandler()


def entrypoint(args):
    if prompt_utils.ask_confirm("Sono presenti migration?", default=False):
        logger.error(
            "Impossibile continuare con il deploy a causa di migration presenti. Chiedi ai devops di effettuare il deploy.")
        sys.exit(-1)

    repo = github.get_repo(args.project)

    latest_release = get_release(repo)

    versions = bump_versions(latest_release.title)

    new_version = prompt_utils.ask_choices(
        "Seleziona versione:",
        [
            {"name": "Patch {}".format(versions["patch"]), "value": versions["patch"]},
            {"name": "Minor {}".format(versions["minor"]), "value": versions["minor"]},
            {"name": "Major {}".format(versions["major"]), "value": versions["major"]},
        ]
    )

    commits = github.get_commits_since_release(repo, latest_release)
    message = "\n".join(["* " + c.commit.message.splitlines()[0] for c in commits])

    logger.info("\nLista dei commit:\n{}\n".format(message))

    if not prompt_utils.ask_confirm("Vuoi continuare?"):
        sys.exit(-1)

    release_state = config["youtrack"]["release_state"]

    deployed_cards_link = []
    try:
        for issue_id in youtrack.get_issue_ids(commits):
            deployed_cards_link.append(youtrack.get_link(issue_id))
            youtrack.update_state(
                issue_id, release_state
            )
        logger.info("Imposto le card in {}".format(release_state))
    except:
        logger.warning("Si è verificato un errore durante lo spostamento delle card in {}".format(release_state))
    finally:
        create_release(repo, new_version, message, args.project, deployed_cards_link)


def get_release(repo):
    latest_release = github.get_latest_release_if_exists(repo)
    if latest_release:
        logger.info("La release attuale è {}".format(latest_release.title))
        return latest_release
    else:
        tag = repo.get_tags()[0]
        logger.info("L'ultimo tag trovato è {}".format(tag.name))

        return repo.create_git_release(tag.name, tag.name, "New release from tag {}".format(tag.name))


def create_release(repo, new_version, message, project, deployed_cards_link):
    new_release = repo.create_git_release(new_version, new_version, message)
    if new_release:
        logger.info("La release è stata creata! Link: {}".format(new_release.html_url))
        slack.post(
            "#deploy", "ho effettuato il deploy di {}. Nuova release con versione {} {}\n{}".format(project, new_version, new_release.html_url, deployed_cards_to_string(deployed_cards_link)))


def bump_versions(current):
    return {
        "patch": semver.bump_patch(current),
        "minor": semver.bump_minor(current),
        "major": semver.bump_major(current)
    }


def deployed_cards_to_string(cards):
    if len(cards) == 0:
        return ""
    else:
        return "\n".join(cards)
