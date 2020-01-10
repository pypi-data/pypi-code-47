from octopy import request, model


class Reaction:

    """
    Official GITHUB documentation: https://developer.github.com/v3/reactions/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Reactions.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.squirrel-girl-preview+json"

    def all(self, reactions_for="commit_comment", page=1, **kwargs):
        """
        Returns all reaction for a specific type.

        :kwarg reactions_for: specifies for which type, reactions to be returned.
            It can be `commit_comment`, `issue`, `team_discussion_comment`,
            `team_discussion`, or `pull_request`
        :kwarg content: returns a single reacton type; if not provided, returns all
            reactions
        """
        owner = kwargs.get("owner")
        repo = kwargs.get("repo")

        try:
            del kwargs["owner"]
            del kwargs["repo"]
        except:
            pass

        if reactions_for.lower() == "commit_comment":
            comment_id = kwargs.get("comment_id")
            del kwargs["comment_id"]
            url = f"{self._url}/repos/{owner}/{repo}/comments/{comment_id}/reactions?page={page}"
        elif reactions_for.lower() == "issue":
            issue_number = kwargs.get("issue_number")
            del kwargs["issue_number"]
            url = f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/reactions?page={page}"
        elif reactions_for.lower() == "issue_comment":
            comment_id = kwargs.get("comment_id")
            del kwargs["comment_id"]
            url = f"{self._url}/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions?page={page}"
        elif reactions_for.lower() == "pull_request":
            comment_id = kwargs.get("comment_id")
            del kwargs["comment_id"]
            url = f"{self._url}/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions?page={page}"
        elif reactions_for.lower() == "team_disscusion":
            team_id = kwargs.get("team_id")
            disscusion_number = kwargs.get("disscusion_number")

            del kwargs["team_id"]
            del kwargs["disscusion_number"]
            url = f"{self._url}/teams/{team_id}/discussions/{disscusion_number}/reactions?page={page}"
        elif reactions_for.lower() == "team_disscusion_comment":
            team_id = kwargs.get("team_id")
            disscusion_number = kwargs.get("disscusion_number")
            comment_number = kwargs.get("comment_number")
            del kwargs["team_id"]
            del kwargs["disscusion_number"]
            del kwargs["comment_number"]
            url = f"{self._url}/teams/{team_id}/discussions/{disscusion_number}/comments/{comment_number}/reactions?page={page}"
        else:
            raise TypeError("Invalid choice.")

        items = [
            model.create_class("CommitCommentReaction", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def create(self, reactions_for="commit_comment", **kwargs):
        """
        Creates a reaction.

        :kwarg reactions_for: specifies for which type, reactions to be returned.
            It can be `commit_comment`, `issue`, `team_discussion_comment`,
            `team_discussion`, or `pull_request`
        :kwarg content: [required] reaction type to add to the `reactions_for` type.
        """
        owner = kwargs.get("owner")
        repo = kwargs.get("repo")

        try:
            del kwargs["owner"]
            del kwargs["repo"]
        except:
            pass

        if reactions_for.lower() == "commit_comment":
            comment_id = kwargs.get("comment_id")
            del kwargs["comment_id"]
            url = f"{self._url}/repos/{owner}/{repo}/comments/{comment_id}/reactions"
        elif reactions_for.lower() == "issue":
            issue_number = kwargs.get("issue_number")
            del kwargs["issue_number"]
            url = f"{self._url}/repos/{owner}/{repo}/issues/{issue_number}/reactions"
        elif reactions_for.lower() == "issue_comment":
            comment_id = kwargs.get("comment_id")
            del kwargs["comment_id"]
            url = f"{self._url}/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions"
        elif reactions_for.lower() == "pull_request":
            comment_id = kwargs.get("comment_id")
            del kwargs["comment_id"]
            url = f"{self._url}/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions?page={page}"
        elif reactions_for.lower() == "team_disscustion":
            team_id = kwargs.get("team_id")
            disscusion_number = kwargs.get("disscusion_number")

            del kwargs["team_id"]
            del kwargs["disscusion_number"]
            url = (
                f"{self._url}/teams/{team_id}/discussions/{disscusion_number}/reactions"
            )
        elif reactions_for.lower() == "team_disscusion_comment":
            team_id = kwargs.get("team_id")
            disscusion_number = kwargs.get("disscusion_number")
            comment_number = kwargs.get("comment_number")
            del kwargs["team_id"]
            del kwargs["disscusion_number"]
            del kwargs["comment_number"]
            url = f"{self._url}/teams/{team_id}/discussions/{disscusion_number}/comments/{comment_number}/reactions?page={page}"
        else:
            raise TypeError("Invalid choice.")

        return model.create_class(
            "Reaction", request.post(url, headers=self._headers, params=kwargs)
        )

    def remove(self, reaction_id):
        """
        Deletes a reaction.

        :param reaction_id: reaction's id
        """
        url = f"{self._url}/reactions/{reaction_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
