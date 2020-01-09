# Code is generated: DO NOT EDIT

# Copyright 2019 Machine Zone, Inc. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from kubespec import context
from kubespec import types
from kubespec.k8s import base
from kubespec.k8s import v1 as k8sv1
from typeguard import check_type, typechecked
from typing import Any, Dict, List, Optional


# BuildRunPolicy defines the behaviour of how the new builds are executed
# from the existing build configuration.
BuildRunPolicy = base.Enum(
    "BuildRunPolicy",
    {
        # Label represents the start policy used to to start the build.
        "Label": "openshift.io/build.start-policy",
        # Parallel schedules new builds immediately after they are
        # created. Builds will be executed in parallel.
        "Parallel": "Parallel",
        # Serial schedules new builds to execute in a sequence as
        # they are created. Every build gets queued up and will execute when the
        # previous build completes. This is the default policy.
        "Serial": "Serial",
        # SerialLatestOnly schedules only the latest build to execute,
        # cancelling all the previously queued build.
        "SerialLatestOnly": "SerialLatestOnly",
    },
)


# BuildSourceType is the type of SCM used.
BuildSourceType = base.Enum(
    "BuildSourceType",
    {
        # Binary indicates the build will accept a Binary file as input.
        "Binary": "Binary",
        # Dockerfile uses a Dockerfile as the start of a build
        "Dockerfile": "Dockerfile",
        # Git instructs a build to use a Git source control repository as the build input.
        "Git": "Git",
        # Image indicates the build will accept an image as input
        "Image": "Image",
        # None indicates the build has no predefined input (only valid for Source and Custom Strategies)
        "None": "None",
    },
)


# BuildStrategyType describes a particular way of performing a build.
BuildStrategyType = base.Enum(
    "BuildStrategyType",
    {
        # Custom performs builds using custom builder container image.
        "Custom": "Custom",
        # Docker performs builds using a Dockerfile.
        "Docker": "Docker",
        # JenkinsPipeline indicates the build will run via Jenkine Pipeline.
        "JenkinsPipeline": "JenkinsPipeline",
        # Source performs builds build using Source To Images with a Git repository
        # and a builder image.
        "Source": "Source",
    },
)


# BuildTriggerType refers to a specific BuildTriggerPolicy implementation.
BuildTriggerType = base.Enum(
    "BuildTriggerType",
    {
        # Bitbucket represents a trigger that launches builds on
        # Bitbucket webhook invocations
        "Bitbucket": "Bitbucket",
        # ConfigChange will trigger a build on an initial build config creation
        # WARNING: In the future the behavior will change to trigger a build on any config change
        "ConfigChange": "ConfigChange",
        # Generic represents a trigger that launches builds on
        # generic webhook invocations
        "Generic": "Generic",
        "GitHub": "github",
        # GitLab represents a trigger that launches builds on
        # GitLab webhook invocations
        "GitLab": "GitLab",
        "ImageChange": "imageChange",
    },
)


# ImageOptimizationPolicy describes what optimizations the builder can perform when building images.
ImageOptimizationPolicy = base.Enum(
    "ImageOptimizationPolicy",
    {
        # None will generate a canonical container image as produced by the
        # `container image build` command.
        "None": "None",
        # SkipLayers is an experimental policy and will avoid creating
        # unique layers for each dockerfile line, resulting in smaller images and saving time
        # during creation. Some Dockerfile syntax is not fully supported - content added to
        # a VOLUME by an earlier layer may have incorrect uid, gid, and filesystem permissions.
        # If an unsupported setting is detected, the build will fail.
        "SkipLayers": "SkipLayers",
        # SkipLayersAndWarn is the same as SkipLayers, but will only
        # warn to the build output instead of failing when unsupported syntax is detected. This
        # policy is experimental.
        "SkipLayersAndWarn": "SkipLayersAndWarn",
    },
)


class BinaryBuildRequestOptions(base.TypedObject, base.NamespacedMetadataObject):
    """
    BinaryBuildRequestOptions are the options required to fully speficy a binary build request
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        asFile: str = None,
        revisionCommit: str = None,
        revisionMessage: str = None,
        revisionAuthorName: str = None,
        revisionAuthorEmail: str = None,
        revisionCommitterName: str = None,
        revisionCommitterEmail: str = None,
    ):
        super().__init__(
            apiVersion="build.openshift.io/v1",
            kind="BinaryBuildRequestOptions",
            **({"namespace": namespace} if namespace is not None else {}),
            **({"name": name} if name is not None else {}),
            **({"labels": labels} if labels is not None else {}),
            **({"annotations": annotations} if annotations is not None else {}),
        )
        self.__asFile = asFile
        self.__revisionCommit = revisionCommit
        self.__revisionMessage = revisionMessage
        self.__revisionAuthorName = revisionAuthorName
        self.__revisionAuthorEmail = revisionAuthorEmail
        self.__revisionCommitterName = revisionCommitterName
        self.__revisionCommitterEmail = revisionCommitterEmail

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        asFile = self.asFile()
        check_type("asFile", asFile, Optional[str])
        if asFile:  # omit empty
            v["asFile"] = asFile
        revisionCommit = self.revisionCommit()
        check_type("revisionCommit", revisionCommit, Optional[str])
        if revisionCommit:  # omit empty
            v["revision.commit"] = revisionCommit
        revisionMessage = self.revisionMessage()
        check_type("revisionMessage", revisionMessage, Optional[str])
        if revisionMessage:  # omit empty
            v["revision.message"] = revisionMessage
        revisionAuthorName = self.revisionAuthorName()
        check_type("revisionAuthorName", revisionAuthorName, Optional[str])
        if revisionAuthorName:  # omit empty
            v["revision.authorName"] = revisionAuthorName
        revisionAuthorEmail = self.revisionAuthorEmail()
        check_type("revisionAuthorEmail", revisionAuthorEmail, Optional[str])
        if revisionAuthorEmail:  # omit empty
            v["revision.authorEmail"] = revisionAuthorEmail
        revisionCommitterName = self.revisionCommitterName()
        check_type("revisionCommitterName", revisionCommitterName, Optional[str])
        if revisionCommitterName:  # omit empty
            v["revision.committerName"] = revisionCommitterName
        revisionCommitterEmail = self.revisionCommitterEmail()
        check_type("revisionCommitterEmail", revisionCommitterEmail, Optional[str])
        if revisionCommitterEmail:  # omit empty
            v["revision.committerEmail"] = revisionCommitterEmail
        return v

    def asFile(self) -> Optional[str]:
        """
        asFile determines if the binary should be created as a file within the source rather than extracted as an archive
        """
        return self.__asFile

    def revisionCommit(self) -> Optional[str]:
        """
        revision.commit is the value identifying a specific commit
        """
        return self.__revisionCommit

    def revisionMessage(self) -> Optional[str]:
        """
        revision.message is the description of a specific commit
        """
        return self.__revisionMessage

    def revisionAuthorName(self) -> Optional[str]:
        """
        revision.authorName of the source control user
        """
        return self.__revisionAuthorName

    def revisionAuthorEmail(self) -> Optional[str]:
        """
        revision.authorEmail of the source control user
        """
        return self.__revisionAuthorEmail

    def revisionCommitterName(self) -> Optional[str]:
        """
        revision.committerName of the source control user
        """
        return self.__revisionCommitterName

    def revisionCommitterEmail(self) -> Optional[str]:
        """
        revision.committerEmail of the source control user
        """
        return self.__revisionCommitterEmail


class BinaryBuildSource(types.Object):
    """
    BinaryBuildSource describes a binary file to be used for the Docker and Source build strategies,
    where the file will be extracted and used as the build source.
    """

    @context.scoped
    @typechecked
    def __init__(self, asFile: str = None):
        super().__init__()
        self.__asFile = asFile

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        asFile = self.asFile()
        check_type("asFile", asFile, Optional[str])
        if asFile:  # omit empty
            v["asFile"] = asFile
        return v

    def asFile(self) -> Optional[str]:
        """
        asFile indicates that the provided binary input should be considered a single file
        within the build input. For example, specifying "webapp.war" would place the provided
        binary as `/webapp.war` for the builder. If left empty, the Docker and Source build
        strategies assume this file is a zip, tar, or tar.gz file and extract it as the source.
        The custom strategy receives this binary as standard input. This filename may not
        contain slashes or be '..' or '.'.
        """
        return self.__asFile


class SourceControlUser(types.Object):
    """
    SourceControlUser defines the identity of a user of source control
    """

    @context.scoped
    @typechecked
    def __init__(self, name: str = None, email: str = None):
        super().__init__()
        self.__name = name
        self.__email = email

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        name = self.name()
        check_type("name", name, Optional[str])
        if name:  # omit empty
            v["name"] = name
        email = self.email()
        check_type("email", email, Optional[str])
        if email:  # omit empty
            v["email"] = email
        return v

    def name(self) -> Optional[str]:
        """
        name of the source control user
        """
        return self.__name

    def email(self) -> Optional[str]:
        """
        email of the source control user
        """
        return self.__email


class GitSourceRevision(types.Object):
    """
    GitSourceRevision is the commit information from a git source for a build
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        commit: str = None,
        author: "SourceControlUser" = None,
        committer: "SourceControlUser" = None,
        message: str = None,
    ):
        super().__init__()
        self.__commit = commit
        self.__author = author if author is not None else SourceControlUser()
        self.__committer = committer if committer is not None else SourceControlUser()
        self.__message = message

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        commit = self.commit()
        check_type("commit", commit, Optional[str])
        if commit:  # omit empty
            v["commit"] = commit
        author = self.author()
        check_type("author", author, Optional["SourceControlUser"])
        v["author"] = author
        committer = self.committer()
        check_type("committer", committer, Optional["SourceControlUser"])
        v["committer"] = committer
        message = self.message()
        check_type("message", message, Optional[str])
        if message:  # omit empty
            v["message"] = message
        return v

    def commit(self) -> Optional[str]:
        """
        commit is the commit hash identifying a specific commit
        """
        return self.__commit

    def author(self) -> Optional["SourceControlUser"]:
        """
        author is the author of a specific commit
        """
        return self.__author

    def committer(self) -> Optional["SourceControlUser"]:
        """
        committer is the committer of a specific commit
        """
        return self.__committer

    def message(self) -> Optional[str]:
        """
        message is the description of a specific commit
        """
        return self.__message


class SourceRevision(types.Object):
    """
    SourceRevision is the revision or commit information from the source for the build
    """

    @context.scoped
    @typechecked
    def __init__(self, type: BuildSourceType = None, git: "GitSourceRevision" = None):
        super().__init__()
        self.__type = type
        self.__git = git

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        type = self.type()
        check_type("type", type, BuildSourceType)
        v["type"] = type
        git = self.git()
        check_type("git", git, Optional["GitSourceRevision"])
        if git is not None:  # omit empty
            v["git"] = git
        return v

    def type(self) -> BuildSourceType:
        """
        type of the build source, may be one of 'Source', 'Dockerfile', 'Binary', or 'Images'
        """
        return self.__type

    def git(self) -> Optional["GitSourceRevision"]:
        """
        Git contains information about git-based build source
        """
        return self.__git


class CommonWebHookCause(types.Object):
    """
    CommonWebHookCause factors out the identical format of these webhook
    causes into struct so we can share it in the specific causes;  it is too late for
    GitHub and Generic but we can leverage this pattern with GitLab and Bitbucket.
    """

    @context.scoped
    @typechecked
    def __init__(self, revision: "SourceRevision" = None, secret: str = None):
        super().__init__()
        self.__revision = revision
        self.__secret = secret

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        revision = self.revision()
        check_type("revision", revision, Optional["SourceRevision"])
        if revision is not None:  # omit empty
            v["revision"] = revision
        secret = self.secret()
        check_type("secret", secret, Optional[str])
        if secret:  # omit empty
            v["secret"] = secret
        return v

    def revision(self) -> Optional["SourceRevision"]:
        """
        Revision is the git source revision information of the trigger.
        """
        return self.__revision

    def secret(self) -> Optional[str]:
        """
        Secret is the obfuscated webhook secret that triggered a build.
        """
        return self.__secret


class BitbucketWebHookCause(types.Object):
    """
    BitbucketWebHookCause has information about a Bitbucket webhook that triggered a
    build.
    """

    @context.scoped
    @typechecked
    def __init__(self, commonWebHookCause: "CommonWebHookCause" = None):
        super().__init__()
        self.__commonWebHookCause = (
            commonWebHookCause
            if commonWebHookCause is not None
            else CommonWebHookCause()
        )

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        commonWebHookCause = self.commonWebHookCause()
        check_type("commonWebHookCause", commonWebHookCause, "CommonWebHookCause")
        v.update(commonWebHookCause._root())  # inline
        return v

    def commonWebHookCause(self) -> "CommonWebHookCause":
        return self.__commonWebHookCause


class GenericWebHookCause(types.Object):
    """
    GenericWebHookCause holds information about a generic WebHook that
    triggered a build.
    """

    @context.scoped
    @typechecked
    def __init__(self, revision: "SourceRevision" = None, secret: str = None):
        super().__init__()
        self.__revision = revision
        self.__secret = secret

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        revision = self.revision()
        check_type("revision", revision, Optional["SourceRevision"])
        if revision is not None:  # omit empty
            v["revision"] = revision
        secret = self.secret()
        check_type("secret", secret, Optional[str])
        if secret:  # omit empty
            v["secret"] = secret
        return v

    def revision(self) -> Optional["SourceRevision"]:
        """
        revision is an optional field that stores the git source revision
        information of the generic webhook trigger when it is available.
        """
        return self.__revision

    def secret(self) -> Optional[str]:
        """
        secret is the obfuscated webhook secret that triggered a build.
        """
        return self.__secret


class GitHubWebHookCause(types.Object):
    """
    GitHubWebHookCause has information about a GitHub webhook that triggered a
    build.
    """

    @context.scoped
    @typechecked
    def __init__(self, revision: "SourceRevision" = None, secret: str = None):
        super().__init__()
        self.__revision = revision
        self.__secret = secret

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        revision = self.revision()
        check_type("revision", revision, Optional["SourceRevision"])
        if revision is not None:  # omit empty
            v["revision"] = revision
        secret = self.secret()
        check_type("secret", secret, Optional[str])
        if secret:  # omit empty
            v["secret"] = secret
        return v

    def revision(self) -> Optional["SourceRevision"]:
        """
        revision is the git revision information of the trigger.
        """
        return self.__revision

    def secret(self) -> Optional[str]:
        """
        secret is the obfuscated webhook secret that triggered a build.
        """
        return self.__secret


class GitLabWebHookCause(types.Object):
    """
    GitLabWebHookCause has information about a GitLab webhook that triggered a
    build.
    """

    @context.scoped
    @typechecked
    def __init__(self, commonWebHookCause: "CommonWebHookCause" = None):
        super().__init__()
        self.__commonWebHookCause = (
            commonWebHookCause
            if commonWebHookCause is not None
            else CommonWebHookCause()
        )

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        commonWebHookCause = self.commonWebHookCause()
        check_type("commonWebHookCause", commonWebHookCause, "CommonWebHookCause")
        v.update(commonWebHookCause._root())  # inline
        return v

    def commonWebHookCause(self) -> "CommonWebHookCause":
        return self.__commonWebHookCause


class ImageChangeCause(types.Object):
    """
    ImageChangeCause contains information about the image that triggered a
    build
    """

    @context.scoped
    @typechecked
    def __init__(self, imageID: str = None, fromRef: "k8sv1.ObjectReference" = None):
        super().__init__()
        self.__imageID = imageID
        self.__fromRef = fromRef

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        imageID = self.imageID()
        check_type("imageID", imageID, Optional[str])
        if imageID:  # omit empty
            v["imageID"] = imageID
        fromRef = self.fromRef()
        check_type("fromRef", fromRef, Optional["k8sv1.ObjectReference"])
        if fromRef is not None:  # omit empty
            v["fromRef"] = fromRef
        return v

    def imageID(self) -> Optional[str]:
        """
        imageID is the ID of the image that triggered a a new build.
        """
        return self.__imageID

    def fromRef(self) -> Optional["k8sv1.ObjectReference"]:
        """
        fromRef contains detailed information about an image that triggered a
        build.
        """
        return self.__fromRef


class BuildTriggerCause(types.Object):
    """
    BuildTriggerCause holds information about a triggered build. It is used for
    displaying build trigger data for each build and build configuration in oc
    describe. It is also used to describe which triggers led to the most recent
    update in the build configuration.
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        message: str = None,
        genericWebHook: "GenericWebHookCause" = None,
        githubWebHook: "GitHubWebHookCause" = None,
        imageChangeBuild: "ImageChangeCause" = None,
        gitlabWebHook: "GitLabWebHookCause" = None,
        bitbucketWebHook: "BitbucketWebHookCause" = None,
    ):
        super().__init__()
        self.__message = message
        self.__genericWebHook = genericWebHook
        self.__githubWebHook = githubWebHook
        self.__imageChangeBuild = imageChangeBuild
        self.__gitlabWebHook = gitlabWebHook
        self.__bitbucketWebHook = bitbucketWebHook

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        message = self.message()
        check_type("message", message, Optional[str])
        if message:  # omit empty
            v["message"] = message
        genericWebHook = self.genericWebHook()
        check_type("genericWebHook", genericWebHook, Optional["GenericWebHookCause"])
        if genericWebHook is not None:  # omit empty
            v["genericWebHook"] = genericWebHook
        githubWebHook = self.githubWebHook()
        check_type("githubWebHook", githubWebHook, Optional["GitHubWebHookCause"])
        if githubWebHook is not None:  # omit empty
            v["githubWebHook"] = githubWebHook
        imageChangeBuild = self.imageChangeBuild()
        check_type("imageChangeBuild", imageChangeBuild, Optional["ImageChangeCause"])
        if imageChangeBuild is not None:  # omit empty
            v["imageChangeBuild"] = imageChangeBuild
        gitlabWebHook = self.gitlabWebHook()
        check_type("gitlabWebHook", gitlabWebHook, Optional["GitLabWebHookCause"])
        if gitlabWebHook is not None:  # omit empty
            v["gitlabWebHook"] = gitlabWebHook
        bitbucketWebHook = self.bitbucketWebHook()
        check_type(
            "bitbucketWebHook", bitbucketWebHook, Optional["BitbucketWebHookCause"]
        )
        if bitbucketWebHook is not None:  # omit empty
            v["bitbucketWebHook"] = bitbucketWebHook
        return v

    def message(self) -> Optional[str]:
        """
        message is used to store a human readable message for why the build was
        triggered. E.g.: "Manually triggered by user", "Configuration change",etc.
        """
        return self.__message

    def genericWebHook(self) -> Optional["GenericWebHookCause"]:
        """
        genericWebHook holds data about a builds generic webhook trigger.
        """
        return self.__genericWebHook

    def githubWebHook(self) -> Optional["GitHubWebHookCause"]:
        """
        gitHubWebHook represents data for a GitHub webhook that fired a
        specific build.
        """
        return self.__githubWebHook

    def imageChangeBuild(self) -> Optional["ImageChangeCause"]:
        """
        imageChangeBuild stores information about an imagechange event
        that triggered a new build.
        """
        return self.__imageChangeBuild

    def gitlabWebHook(self) -> Optional["GitLabWebHookCause"]:
        """
        GitLabWebHook represents data for a GitLab webhook that fired a specific
        build.
        """
        return self.__gitlabWebHook

    def bitbucketWebHook(self) -> Optional["BitbucketWebHookCause"]:
        """
        BitbucketWebHook represents data for a Bitbucket webhook that fired a
        specific build.
        """
        return self.__bitbucketWebHook


class ImageLabel(types.Object):
    """
    ImageLabel represents a label applied to the resulting image.
    """

    @context.scoped
    @typechecked
    def __init__(self, name: str = "", value: str = None):
        super().__init__()
        self.__name = name
        self.__value = value

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        name = self.name()
        check_type("name", name, str)
        v["name"] = name
        value = self.value()
        check_type("value", value, Optional[str])
        if value:  # omit empty
            v["value"] = value
        return v

    def name(self) -> str:
        """
        name defines the name of the label. It must have non-zero length.
        """
        return self.__name

    def value(self) -> Optional[str]:
        """
        value defines the literal value of the label.
        """
        return self.__value


class BuildOutput(types.Object):
    """
    BuildOutput is input to a build strategy and describes the container image that the strategy
    should produce.
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        to: "k8sv1.ObjectReference" = None,
        pushSecret: "k8sv1.LocalObjectReference" = None,
        imageLabels: List["ImageLabel"] = None,
    ):
        super().__init__()
        self.__to = to
        self.__pushSecret = pushSecret
        self.__imageLabels = imageLabels if imageLabels is not None else []

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        to = self.to()
        check_type("to", to, Optional["k8sv1.ObjectReference"])
        if to is not None:  # omit empty
            v["to"] = to
        pushSecret = self.pushSecret()
        check_type("pushSecret", pushSecret, Optional["k8sv1.LocalObjectReference"])
        if pushSecret is not None:  # omit empty
            v["pushSecret"] = pushSecret
        imageLabels = self.imageLabels()
        check_type("imageLabels", imageLabels, Optional[List["ImageLabel"]])
        if imageLabels:  # omit empty
            v["imageLabels"] = imageLabels
        return v

    def to(self) -> Optional["k8sv1.ObjectReference"]:
        """
        to defines an optional location to push the output of this build to.
        Kind must be one of 'ImageStreamTag' or 'DockerImage'.
        This value will be used to look up a container image repository to push to.
        In the case of an ImageStreamTag, the ImageStreamTag will be looked for in the namespace of
        the build unless Namespace is specified.
        """
        return self.__to

    def pushSecret(self) -> Optional["k8sv1.LocalObjectReference"]:
        """
        PushSecret is the name of a Secret that would be used for setting
        up the authentication for executing the Docker push to authentication
        enabled Docker Registry (or Docker Hub).
        """
        return self.__pushSecret

    def imageLabels(self) -> Optional[List["ImageLabel"]]:
        """
        imageLabels define a list of labels that are applied to the resulting image. If there
        are multiple labels with the same name then the last one in the list is used.
        """
        return self.__imageLabels


class BuildPostCommitSpec(types.Object):
    """
    A BuildPostCommitSpec holds a build post commit hook specification. The hook
    executes a command in a temporary container running the build output image,
    immediately after the last layer of the image is committed and before the
    image is pushed to a registry. The command is executed with the current
    working directory ($PWD) set to the image's WORKDIR.
    
    The build will be marked as failed if the hook execution fails. It will fail
    if the script or command return a non-zero exit code, or if there is any
    other error related to starting the temporary container.
    
    There are five different ways to configure the hook. As an example, all forms
    below are equivalent and will execute `rake test --verbose`.
    
    1. Shell script:
    
           "postCommit": {
             "script": "rake test --verbose",
           }
    
        The above is a convenient form which is equivalent to:
    
           "postCommit": {
             "command": ["/bin/sh", "-ic"],
             "args":    ["rake test --verbose"]
           }
    
    2. A command as the image entrypoint:
    
           "postCommit": {
             "commit": ["rake", "test", "--verbose"]
           }
    
        Command overrides the image entrypoint in the exec form, as documented in
        Docker: https://docs.docker.com/engine/reference/builder/#entrypoint.
    
    3. Pass arguments to the default entrypoint:
    
           "postCommit": {
    		      "args": ["rake", "test", "--verbose"]
    	      }
    
        This form is only useful if the image entrypoint can handle arguments.
    
    4. Shell script with arguments:
    
           "postCommit": {
             "script": "rake test $1",
             "args":   ["--verbose"]
           }
    
        This form is useful if you need to pass arguments that would otherwise be
        hard to quote properly in the shell script. In the script, $0 will be
        "/bin/sh" and $1, $2, etc, are the positional arguments from Args.
    
    5. Command with arguments:
    
           "postCommit": {
             "command": ["rake", "test"],
             "args":    ["--verbose"]
           }
    
        This form is equivalent to appending the arguments to the Command slice.
    
    It is invalid to provide both Script and Command simultaneously. If none of
    the fields are specified, the hook is not executed.
    """

    @context.scoped
    @typechecked
    def __init__(
        self, command: List[str] = None, args: List[str] = None, script: str = None
    ):
        super().__init__()
        self.__command = command if command is not None else []
        self.__args = args if args is not None else []
        self.__script = script

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        command = self.command()
        check_type("command", command, Optional[List[str]])
        if command:  # omit empty
            v["command"] = command
        args = self.args()
        check_type("args", args, Optional[List[str]])
        if args:  # omit empty
            v["args"] = args
        script = self.script()
        check_type("script", script, Optional[str])
        if script:  # omit empty
            v["script"] = script
        return v

    def command(self) -> Optional[List[str]]:
        """
        command is the command to run. It may not be specified with Script.
        This might be needed if the image doesn't have `/bin/sh`, or if you
        do not want to use a shell. In all other cases, using Script might be
        more convenient.
        """
        return self.__command

    def args(self) -> Optional[List[str]]:
        """
        args is a list of arguments that are provided to either Command,
        Script or the container image's default entrypoint. The arguments are
        placed immediately after the command to be run.
        """
        return self.__args

    def script(self) -> Optional[str]:
        """
        script is a shell script to be run with `/bin/sh -ic`. It may not be
        specified with Command. Use Script when a shell script is appropriate
        to execute the post build hook, for example for running unit tests
        with `rake test`. If you need control over the image entrypoint, or
        if the image does not have `/bin/sh`, use Command and/or Args.
        The `-i` flag is needed to support CentOS and RHEL images that use
        Software Collections (SCL), in order to have the appropriate
        collections enabled in the shell. E.g., in the Ruby image, this is
        necessary to make `ruby`, `bundle` and other binaries available in
        the PATH.
        """
        return self.__script


class ConfigMapBuildSource(types.Object):
    """
    ConfigMapBuildSource describes a configmap and its destination directory that will be
    used only at the build time. The content of the configmap referenced here will
    be copied into the destination directory instead of mounting.
    """

    @context.scoped
    @typechecked
    def __init__(
        self, configMap: "k8sv1.LocalObjectReference" = None, destinationDir: str = None
    ):
        super().__init__()
        self.__configMap = (
            configMap if configMap is not None else k8sv1.LocalObjectReference()
        )
        self.__destinationDir = destinationDir

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        configMap = self.configMap()
        check_type("configMap", configMap, "k8sv1.LocalObjectReference")
        v["configMap"] = configMap
        destinationDir = self.destinationDir()
        check_type("destinationDir", destinationDir, Optional[str])
        if destinationDir:  # omit empty
            v["destinationDir"] = destinationDir
        return v

    def configMap(self) -> "k8sv1.LocalObjectReference":
        """
        configMap is a reference to an existing configmap that you want to use in your
        build.
        """
        return self.__configMap

    def destinationDir(self) -> Optional[str]:
        """
        destinationDir is the directory where the files from the configmap should be
        available for the build time.
        For the Source build strategy, these will be injected into a container
        where the assemble script runs.
        For the container image build strategy, these will be copied into the build
        directory, where the Dockerfile is located, so users can ADD or COPY them
        during container image build.
        """
        return self.__destinationDir


class ProxyConfig(types.Object):
    """
    ProxyConfig defines what proxies to use for an operation
    """

    @context.scoped
    @typechecked
    def __init__(
        self, httpProxy: str = None, httpsProxy: str = None, noProxy: str = None
    ):
        super().__init__()
        self.__httpProxy = httpProxy
        self.__httpsProxy = httpsProxy
        self.__noProxy = noProxy

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        httpProxy = self.httpProxy()
        check_type("httpProxy", httpProxy, Optional[str])
        if httpProxy is not None:  # omit empty
            v["httpProxy"] = httpProxy
        httpsProxy = self.httpsProxy()
        check_type("httpsProxy", httpsProxy, Optional[str])
        if httpsProxy is not None:  # omit empty
            v["httpsProxy"] = httpsProxy
        noProxy = self.noProxy()
        check_type("noProxy", noProxy, Optional[str])
        if noProxy is not None:  # omit empty
            v["noProxy"] = noProxy
        return v

    def httpProxy(self) -> Optional[str]:
        """
        httpProxy is a proxy used to reach the git repository over http
        """
        return self.__httpProxy

    def httpsProxy(self) -> Optional[str]:
        """
        httpsProxy is a proxy used to reach the git repository over https
        """
        return self.__httpsProxy

    def noProxy(self) -> Optional[str]:
        """
        noProxy is the list of domains for which the proxy should not be used
        """
        return self.__noProxy


class GitBuildSource(types.Object):
    """
    GitBuildSource defines the parameters of a Git SCM
    """

    @context.scoped
    @typechecked
    def __init__(
        self, uri: str = "", ref: str = None, proxyConfig: "ProxyConfig" = None
    ):
        super().__init__()
        self.__uri = uri
        self.__ref = ref
        self.__proxyConfig = proxyConfig if proxyConfig is not None else ProxyConfig()

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        uri = self.uri()
        check_type("uri", uri, str)
        v["uri"] = uri
        ref = self.ref()
        check_type("ref", ref, Optional[str])
        if ref:  # omit empty
            v["ref"] = ref
        proxyConfig = self.proxyConfig()
        check_type("proxyConfig", proxyConfig, "ProxyConfig")
        v.update(proxyConfig._root())  # inline
        return v

    def uri(self) -> str:
        """
        uri points to the source that will be built. The structure of the source
        will depend on the type of build to run
        """
        return self.__uri

    def ref(self) -> Optional[str]:
        """
        ref is the branch/tag/ref to build.
        """
        return self.__ref

    def proxyConfig(self) -> "ProxyConfig":
        """
        proxyConfig defines the proxies to use for the git clone operation. Values
        not set here are inherited from cluster-wide build git proxy settings.
        """
        return self.__proxyConfig


class ImageSourcePath(types.Object):
    """
    ImageSourcePath describes a path to be copied from a source image and its destination within the build directory.
    """

    @context.scoped
    @typechecked
    def __init__(self, sourcePath: str = "", destinationDir: str = ""):
        super().__init__()
        self.__sourcePath = sourcePath
        self.__destinationDir = destinationDir

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        sourcePath = self.sourcePath()
        check_type("sourcePath", sourcePath, str)
        v["sourcePath"] = sourcePath
        destinationDir = self.destinationDir()
        check_type("destinationDir", destinationDir, str)
        v["destinationDir"] = destinationDir
        return v

    def sourcePath(self) -> str:
        """
        sourcePath is the absolute path of the file or directory inside the image to
        copy to the build directory.  If the source path ends in /. then the content of
        the directory will be copied, but the directory itself will not be created at the
        destination.
        """
        return self.__sourcePath

    def destinationDir(self) -> str:
        """
        destinationDir is the relative directory within the build directory
        where files copied from the image are placed.
        """
        return self.__destinationDir


class ImageSource(types.Object):
    """
    ImageSource is used to describe build source that will be extracted from an image or used during a
    multi stage build. A reference of type ImageStreamTag, ImageStreamImage or DockerImage may be used.
    A pull secret can be specified to pull the image from an external registry or override the default
    service account secret if pulling from the internal registry. Image sources can either be used to
    extract content from an image and place it into the build context along with the repository source,
    or used directly during a multi-stage container image build to allow content to be copied without overwriting
    the contents of the repository source (see the 'paths' and 'as' fields).
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        from_: "k8sv1.ObjectReference" = None,
        as_: List[str] = None,
        paths: List["ImageSourcePath"] = None,
        pullSecret: "k8sv1.LocalObjectReference" = None,
    ):
        super().__init__()
        self.__from_ = from_ if from_ is not None else k8sv1.ObjectReference()
        self.__as_ = as_ if as_ is not None else []
        self.__paths = paths if paths is not None else []
        self.__pullSecret = pullSecret

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        from_ = self.from_()
        check_type("from_", from_, "k8sv1.ObjectReference")
        v["from"] = from_
        as_ = self.as_()
        check_type("as_", as_, List[str])
        v["as"] = as_
        paths = self.paths()
        check_type("paths", paths, List["ImageSourcePath"])
        v["paths"] = paths
        pullSecret = self.pullSecret()
        check_type("pullSecret", pullSecret, Optional["k8sv1.LocalObjectReference"])
        if pullSecret is not None:  # omit empty
            v["pullSecret"] = pullSecret
        return v

    def from_(self) -> "k8sv1.ObjectReference":
        """
        from is a reference to an ImageStreamTag, ImageStreamImage, or DockerImage to
        copy source from.
        """
        return self.__from_

    def as_(self) -> List[str]:
        """
        A list of image names that this source will be used in place of during a multi-stage container image
        build. For instance, a Dockerfile that uses "COPY --from=nginx:latest" will first check for an image
        source that has "nginx:latest" in this field before attempting to pull directly. If the Dockerfile
        does not reference an image source it is ignored. This field and paths may both be set, in which case
        the contents will be used twice.
        """
        return self.__as_

    def paths(self) -> List["ImageSourcePath"]:
        """
        paths is a list of source and destination paths to copy from the image. This content will be copied
        into the build context prior to starting the build. If no paths are set, the build context will
        not be altered.
        """
        return self.__paths

    def pullSecret(self) -> Optional["k8sv1.LocalObjectReference"]:
        """
        pullSecret is a reference to a secret to be used to pull the image from a registry
        If the image is pulled from the OpenShift registry, this field does not need to be set.
        """
        return self.__pullSecret


class SecretBuildSource(types.Object):
    """
    SecretBuildSource describes a secret and its destination directory that will be
    used only at the build time. The content of the secret referenced here will
    be copied into the destination directory instead of mounting.
    """

    @context.scoped
    @typechecked
    def __init__(
        self, secret: "k8sv1.LocalObjectReference" = None, destinationDir: str = None
    ):
        super().__init__()
        self.__secret = secret if secret is not None else k8sv1.LocalObjectReference()
        self.__destinationDir = destinationDir

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        secret = self.secret()
        check_type("secret", secret, "k8sv1.LocalObjectReference")
        v["secret"] = secret
        destinationDir = self.destinationDir()
        check_type("destinationDir", destinationDir, Optional[str])
        if destinationDir:  # omit empty
            v["destinationDir"] = destinationDir
        return v

    def secret(self) -> "k8sv1.LocalObjectReference":
        """
        secret is a reference to an existing secret that you want to use in your
        build.
        """
        return self.__secret

    def destinationDir(self) -> Optional[str]:
        """
        destinationDir is the directory where the files from the secret should be
        available for the build time.
        For the Source build strategy, these will be injected into a container
        where the assemble script runs. Later, when the script finishes, all files
        injected will be truncated to zero length.
        For the container image build strategy, these will be copied into the build
        directory, where the Dockerfile is located, so users can ADD or COPY them
        during container image build.
        """
        return self.__destinationDir


class BuildSource(types.Object):
    """
    BuildSource is the SCM used for the build.
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        type: BuildSourceType = None,
        binary: "BinaryBuildSource" = None,
        dockerfile: str = None,
        git: "GitBuildSource" = None,
        images: List["ImageSource"] = None,
        contextDir: str = None,
        sourceSecret: "k8sv1.LocalObjectReference" = None,
        secrets: List["SecretBuildSource"] = None,
        configMaps: List["ConfigMapBuildSource"] = None,
    ):
        super().__init__()
        self.__type = type
        self.__binary = binary
        self.__dockerfile = dockerfile
        self.__git = git
        self.__images = images if images is not None else []
        self.__contextDir = contextDir
        self.__sourceSecret = sourceSecret
        self.__secrets = secrets if secrets is not None else []
        self.__configMaps = configMaps if configMaps is not None else []

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        type = self.type()
        check_type("type", type, BuildSourceType)
        v["type"] = type
        binary = self.binary()
        check_type("binary", binary, Optional["BinaryBuildSource"])
        if binary is not None:  # omit empty
            v["binary"] = binary
        dockerfile = self.dockerfile()
        check_type("dockerfile", dockerfile, Optional[str])
        if dockerfile is not None:  # omit empty
            v["dockerfile"] = dockerfile
        git = self.git()
        check_type("git", git, Optional["GitBuildSource"])
        if git is not None:  # omit empty
            v["git"] = git
        images = self.images()
        check_type("images", images, Optional[List["ImageSource"]])
        if images:  # omit empty
            v["images"] = images
        contextDir = self.contextDir()
        check_type("contextDir", contextDir, Optional[str])
        if contextDir:  # omit empty
            v["contextDir"] = contextDir
        sourceSecret = self.sourceSecret()
        check_type("sourceSecret", sourceSecret, Optional["k8sv1.LocalObjectReference"])
        if sourceSecret is not None:  # omit empty
            v["sourceSecret"] = sourceSecret
        secrets = self.secrets()
        check_type("secrets", secrets, Optional[List["SecretBuildSource"]])
        if secrets:  # omit empty
            v["secrets"] = secrets
        configMaps = self.configMaps()
        check_type("configMaps", configMaps, Optional[List["ConfigMapBuildSource"]])
        if configMaps:  # omit empty
            v["configMaps"] = configMaps
        return v

    def type(self) -> BuildSourceType:
        """
        type of build input to accept
        """
        return self.__type

    def binary(self) -> Optional["BinaryBuildSource"]:
        """
        binary builds accept a binary as their input. The binary is generally assumed to be a tar,
        gzipped tar, or zip file depending on the strategy. For container image builds, this is the build
        context and an optional Dockerfile may be specified to override any Dockerfile in the
        build context. For Source builds, this is assumed to be an archive as described above. For
        Source and container image builds, if binary.asFile is set the build will receive a directory with
        a single file. contextDir may be used when an archive is provided. Custom builds will
        receive this binary as input on STDIN.
        """
        return self.__binary

    def dockerfile(self) -> Optional[str]:
        """
        dockerfile is the raw contents of a Dockerfile which should be built. When this option is
        specified, the FROM may be modified based on your strategy base image and additional ENV
        stanzas from your strategy environment will be added after the FROM, but before the rest
        of your Dockerfile stanzas. The Dockerfile source type may be used with other options like
        git - in those cases the Git repo will have any innate Dockerfile replaced in the context
        dir.
        """
        return self.__dockerfile

    def git(self) -> Optional["GitBuildSource"]:
        """
        git contains optional information about git build source
        """
        return self.__git

    def images(self) -> Optional[List["ImageSource"]]:
        """
        images describes a set of images to be used to provide source for the build
        """
        return self.__images

    def contextDir(self) -> Optional[str]:
        """
        contextDir specifies the sub-directory where the source code for the application exists.
        This allows to have buildable sources in directory other than root of
        repository.
        """
        return self.__contextDir

    def sourceSecret(self) -> Optional["k8sv1.LocalObjectReference"]:
        """
        sourceSecret is the name of a Secret that would be used for setting
        up the authentication for cloning private repository.
        The secret contains valid credentials for remote repository, where the
        data's key represent the authentication method to be used and value is
        the base64 encoded credentials. Supported auth methods are: ssh-privatekey.
        """
        return self.__sourceSecret

    def secrets(self) -> Optional[List["SecretBuildSource"]]:
        """
        secrets represents a list of secrets and their destinations that will
        be used only for the build.
        """
        return self.__secrets

    def configMaps(self) -> Optional[List["ConfigMapBuildSource"]]:
        """
        configMaps represents a list of configMaps and their destinations that will
        be used for the build.
        """
        return self.__configMaps


class SecretSpec(types.Object):
    """
    SecretSpec specifies a secret to be included in a build pod and its corresponding mount point
    """

    @context.scoped
    @typechecked
    def __init__(
        self, secretSource: "k8sv1.LocalObjectReference" = None, mountPath: str = ""
    ):
        super().__init__()
        self.__secretSource = (
            secretSource if secretSource is not None else k8sv1.LocalObjectReference()
        )
        self.__mountPath = mountPath

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        secretSource = self.secretSource()
        check_type("secretSource", secretSource, "k8sv1.LocalObjectReference")
        v["secretSource"] = secretSource
        mountPath = self.mountPath()
        check_type("mountPath", mountPath, str)
        v["mountPath"] = mountPath
        return v

    def secretSource(self) -> "k8sv1.LocalObjectReference":
        """
        secretSource is a reference to the secret
        """
        return self.__secretSource

    def mountPath(self) -> str:
        """
        mountPath is the path at which to mount the secret
        """
        return self.__mountPath


class CustomBuildStrategy(types.Object):
    """
    CustomBuildStrategy defines input parameters specific to Custom build.
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        from_: "k8sv1.ObjectReference" = None,
        pullSecret: "k8sv1.LocalObjectReference" = None,
        env: List["k8sv1.EnvVar"] = None,
        exposeDockerSocket: bool = None,
        forcePull: bool = None,
        secrets: List["SecretSpec"] = None,
        buildAPIVersion: str = None,
    ):
        super().__init__()
        self.__from_ = from_ if from_ is not None else k8sv1.ObjectReference()
        self.__pullSecret = pullSecret
        self.__env = env if env is not None else []
        self.__exposeDockerSocket = exposeDockerSocket
        self.__forcePull = forcePull
        self.__secrets = secrets if secrets is not None else []
        self.__buildAPIVersion = buildAPIVersion

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        from_ = self.from_()
        check_type("from_", from_, "k8sv1.ObjectReference")
        v["from"] = from_
        pullSecret = self.pullSecret()
        check_type("pullSecret", pullSecret, Optional["k8sv1.LocalObjectReference"])
        if pullSecret is not None:  # omit empty
            v["pullSecret"] = pullSecret
        env = self.env()
        check_type("env", env, Optional[List["k8sv1.EnvVar"]])
        if env:  # omit empty
            v["env"] = env
        exposeDockerSocket = self.exposeDockerSocket()
        check_type("exposeDockerSocket", exposeDockerSocket, Optional[bool])
        if exposeDockerSocket:  # omit empty
            v["exposeDockerSocket"] = exposeDockerSocket
        forcePull = self.forcePull()
        check_type("forcePull", forcePull, Optional[bool])
        if forcePull:  # omit empty
            v["forcePull"] = forcePull
        secrets = self.secrets()
        check_type("secrets", secrets, Optional[List["SecretSpec"]])
        if secrets:  # omit empty
            v["secrets"] = secrets
        buildAPIVersion = self.buildAPIVersion()
        check_type("buildAPIVersion", buildAPIVersion, Optional[str])
        if buildAPIVersion:  # omit empty
            v["buildAPIVersion"] = buildAPIVersion
        return v

    def from_(self) -> "k8sv1.ObjectReference":
        """
        from is reference to an DockerImage, ImageStreamTag, or ImageStreamImage from which
        the container image should be pulled
        """
        return self.__from_

    def pullSecret(self) -> Optional["k8sv1.LocalObjectReference"]:
        """
        pullSecret is the name of a Secret that would be used for setting up
        the authentication for pulling the container images from the private Docker
        registries
        """
        return self.__pullSecret

    def env(self) -> Optional[List["k8sv1.EnvVar"]]:
        """
        env contains additional environment variables you want to pass into a builder container.
        """
        return self.__env

    def exposeDockerSocket(self) -> Optional[bool]:
        """
        exposeDockerSocket will allow running Docker commands (and build container images) from
        inside the container.
        TODO: Allow admins to enforce 'false' for this option
        """
        return self.__exposeDockerSocket

    def forcePull(self) -> Optional[bool]:
        """
        forcePull describes if the controller should configure the build pod to always pull the images
        for the builder or only pull if it is not present locally
        """
        return self.__forcePull

    def secrets(self) -> Optional[List["SecretSpec"]]:
        """
        secrets is a list of additional secrets that will be included in the build pod
        """
        return self.__secrets

    def buildAPIVersion(self) -> Optional[str]:
        """
        buildAPIVersion is the requested API version for the Build object serialized and passed to the custom builder
        """
        return self.__buildAPIVersion


class DockerBuildStrategy(types.Object):
    """
    DockerBuildStrategy defines input parameters specific to container image build.
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        from_: "k8sv1.ObjectReference" = None,
        pullSecret: "k8sv1.LocalObjectReference" = None,
        noCache: bool = None,
        env: List["k8sv1.EnvVar"] = None,
        forcePull: bool = None,
        dockerfilePath: str = None,
        buildArgs: List["k8sv1.EnvVar"] = None,
        imageOptimizationPolicy: ImageOptimizationPolicy = None,
    ):
        super().__init__()
        self.__from_ = from_
        self.__pullSecret = pullSecret
        self.__noCache = noCache
        self.__env = env if env is not None else []
        self.__forcePull = forcePull
        self.__dockerfilePath = dockerfilePath
        self.__buildArgs = buildArgs if buildArgs is not None else []
        self.__imageOptimizationPolicy = imageOptimizationPolicy

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        from_ = self.from_()
        check_type("from_", from_, Optional["k8sv1.ObjectReference"])
        if from_ is not None:  # omit empty
            v["from"] = from_
        pullSecret = self.pullSecret()
        check_type("pullSecret", pullSecret, Optional["k8sv1.LocalObjectReference"])
        if pullSecret is not None:  # omit empty
            v["pullSecret"] = pullSecret
        noCache = self.noCache()
        check_type("noCache", noCache, Optional[bool])
        if noCache:  # omit empty
            v["noCache"] = noCache
        env = self.env()
        check_type("env", env, Optional[List["k8sv1.EnvVar"]])
        if env:  # omit empty
            v["env"] = env
        forcePull = self.forcePull()
        check_type("forcePull", forcePull, Optional[bool])
        if forcePull:  # omit empty
            v["forcePull"] = forcePull
        dockerfilePath = self.dockerfilePath()
        check_type("dockerfilePath", dockerfilePath, Optional[str])
        if dockerfilePath:  # omit empty
            v["dockerfilePath"] = dockerfilePath
        buildArgs = self.buildArgs()
        check_type("buildArgs", buildArgs, Optional[List["k8sv1.EnvVar"]])
        if buildArgs:  # omit empty
            v["buildArgs"] = buildArgs
        imageOptimizationPolicy = self.imageOptimizationPolicy()
        check_type(
            "imageOptimizationPolicy",
            imageOptimizationPolicy,
            Optional[ImageOptimizationPolicy],
        )
        if imageOptimizationPolicy is not None:  # omit empty
            v["imageOptimizationPolicy"] = imageOptimizationPolicy
        return v

    def from_(self) -> Optional["k8sv1.ObjectReference"]:
        """
        from is reference to an DockerImage, ImageStreamTag, or ImageStreamImage from which
        the container image should be pulled
        the resulting image will be used in the FROM line of the Dockerfile for this build.
        """
        return self.__from_

    def pullSecret(self) -> Optional["k8sv1.LocalObjectReference"]:
        """
        pullSecret is the name of a Secret that would be used for setting up
        the authentication for pulling the container images from the private Docker
        registries
        """
        return self.__pullSecret

    def noCache(self) -> Optional[bool]:
        """
        noCache if set to true indicates that the container image build must be executed with the
        --no-cache=true flag
        """
        return self.__noCache

    def env(self) -> Optional[List["k8sv1.EnvVar"]]:
        """
        env contains additional environment variables you want to pass into a builder container.
        """
        return self.__env

    def forcePull(self) -> Optional[bool]:
        """
        forcePull describes if the builder should pull the images from registry prior to building.
        """
        return self.__forcePull

    def dockerfilePath(self) -> Optional[str]:
        """
        dockerfilePath is the path of the Dockerfile that will be used to build the container image,
        relative to the root of the context (contextDir).
        """
        return self.__dockerfilePath

    def buildArgs(self) -> Optional[List["k8sv1.EnvVar"]]:
        """
        buildArgs contains build arguments that will be resolved in the Dockerfile.  See
        https://docs.docker.com/engine/reference/builder/#/arg for more details.
        """
        return self.__buildArgs

    def imageOptimizationPolicy(self) -> Optional[ImageOptimizationPolicy]:
        """
        imageOptimizationPolicy describes what optimizations the system can use when building images
        to reduce the final size or time spent building the image. The default policy is 'None' which
        means the final build image will be equivalent to an image created by the container image build API.
        The experimental policy 'SkipLayers' will avoid commiting new layers in between each
        image step, and will fail if the Dockerfile cannot provide compatibility with the 'None'
        policy. An additional experimental policy 'SkipLayersAndWarn' is the same as
        'SkipLayers' but simply warns if compatibility cannot be preserved.
        """
        return self.__imageOptimizationPolicy


class JenkinsPipelineBuildStrategy(types.Object):
    """
    JenkinsPipelineBuildStrategy holds parameters specific to a Jenkins Pipeline build.
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        jenkinsfilePath: str = None,
        jenkinsfile: str = None,
        env: List["k8sv1.EnvVar"] = None,
    ):
        super().__init__()
        self.__jenkinsfilePath = jenkinsfilePath
        self.__jenkinsfile = jenkinsfile
        self.__env = env if env is not None else []

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        jenkinsfilePath = self.jenkinsfilePath()
        check_type("jenkinsfilePath", jenkinsfilePath, Optional[str])
        if jenkinsfilePath:  # omit empty
            v["jenkinsfilePath"] = jenkinsfilePath
        jenkinsfile = self.jenkinsfile()
        check_type("jenkinsfile", jenkinsfile, Optional[str])
        if jenkinsfile:  # omit empty
            v["jenkinsfile"] = jenkinsfile
        env = self.env()
        check_type("env", env, Optional[List["k8sv1.EnvVar"]])
        if env:  # omit empty
            v["env"] = env
        return v

    def jenkinsfilePath(self) -> Optional[str]:
        """
        JenkinsfilePath is the optional path of the Jenkinsfile that will be used to configure the pipeline
        relative to the root of the context (contextDir). If both JenkinsfilePath & Jenkinsfile are
        both not specified, this defaults to Jenkinsfile in the root of the specified contextDir.
        """
        return self.__jenkinsfilePath

    def jenkinsfile(self) -> Optional[str]:
        """
        Jenkinsfile defines the optional raw contents of a Jenkinsfile which defines a Jenkins pipeline build.
        """
        return self.__jenkinsfile

    def env(self) -> Optional[List["k8sv1.EnvVar"]]:
        """
        env contains additional environment variables you want to pass into a build pipeline.
        """
        return self.__env


class SourceBuildStrategy(types.Object):
    """
    SourceBuildStrategy defines input parameters specific to an Source build.
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        from_: "k8sv1.ObjectReference" = None,
        pullSecret: "k8sv1.LocalObjectReference" = None,
        env: List["k8sv1.EnvVar"] = None,
        scripts: str = None,
        incremental: bool = None,
        forcePull: bool = None,
    ):
        super().__init__()
        self.__from_ = from_ if from_ is not None else k8sv1.ObjectReference()
        self.__pullSecret = pullSecret
        self.__env = env if env is not None else []
        self.__scripts = scripts
        self.__incremental = incremental
        self.__forcePull = forcePull

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        from_ = self.from_()
        check_type("from_", from_, "k8sv1.ObjectReference")
        v["from"] = from_
        pullSecret = self.pullSecret()
        check_type("pullSecret", pullSecret, Optional["k8sv1.LocalObjectReference"])
        if pullSecret is not None:  # omit empty
            v["pullSecret"] = pullSecret
        env = self.env()
        check_type("env", env, Optional[List["k8sv1.EnvVar"]])
        if env:  # omit empty
            v["env"] = env
        scripts = self.scripts()
        check_type("scripts", scripts, Optional[str])
        if scripts:  # omit empty
            v["scripts"] = scripts
        incremental = self.incremental()
        check_type("incremental", incremental, Optional[bool])
        if incremental is not None:  # omit empty
            v["incremental"] = incremental
        forcePull = self.forcePull()
        check_type("forcePull", forcePull, Optional[bool])
        if forcePull:  # omit empty
            v["forcePull"] = forcePull
        return v

    def from_(self) -> "k8sv1.ObjectReference":
        """
        from is reference to an DockerImage, ImageStreamTag, or ImageStreamImage from which
        the container image should be pulled
        """
        return self.__from_

    def pullSecret(self) -> Optional["k8sv1.LocalObjectReference"]:
        """
        pullSecret is the name of a Secret that would be used for setting up
        the authentication for pulling the container images from the private Docker
        registries
        """
        return self.__pullSecret

    def env(self) -> Optional[List["k8sv1.EnvVar"]]:
        """
        env contains additional environment variables you want to pass into a builder container.
        """
        return self.__env

    def scripts(self) -> Optional[str]:
        """
        scripts is the location of Source scripts
        """
        return self.__scripts

    def incremental(self) -> Optional[bool]:
        """
        incremental flag forces the Source build to do incremental builds if true.
        """
        return self.__incremental

    def forcePull(self) -> Optional[bool]:
        """
        forcePull describes if the builder should pull the images from registry prior to building.
        """
        return self.__forcePull


class BuildStrategy(types.Object):
    """
    BuildStrategy contains the details of how to perform a build.
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        type: BuildStrategyType = None,
        dockerStrategy: "DockerBuildStrategy" = None,
        sourceStrategy: "SourceBuildStrategy" = None,
        customStrategy: "CustomBuildStrategy" = None,
        jenkinsPipelineStrategy: "JenkinsPipelineBuildStrategy" = None,
    ):
        super().__init__()
        self.__type = type
        self.__dockerStrategy = dockerStrategy
        self.__sourceStrategy = sourceStrategy
        self.__customStrategy = customStrategy
        self.__jenkinsPipelineStrategy = jenkinsPipelineStrategy

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        type = self.type()
        check_type("type", type, BuildStrategyType)
        v["type"] = type
        dockerStrategy = self.dockerStrategy()
        check_type("dockerStrategy", dockerStrategy, Optional["DockerBuildStrategy"])
        if dockerStrategy is not None:  # omit empty
            v["dockerStrategy"] = dockerStrategy
        sourceStrategy = self.sourceStrategy()
        check_type("sourceStrategy", sourceStrategy, Optional["SourceBuildStrategy"])
        if sourceStrategy is not None:  # omit empty
            v["sourceStrategy"] = sourceStrategy
        customStrategy = self.customStrategy()
        check_type("customStrategy", customStrategy, Optional["CustomBuildStrategy"])
        if customStrategy is not None:  # omit empty
            v["customStrategy"] = customStrategy
        jenkinsPipelineStrategy = self.jenkinsPipelineStrategy()
        check_type(
            "jenkinsPipelineStrategy",
            jenkinsPipelineStrategy,
            Optional["JenkinsPipelineBuildStrategy"],
        )
        if jenkinsPipelineStrategy is not None:  # omit empty
            v["jenkinsPipelineStrategy"] = jenkinsPipelineStrategy
        return v

    def type(self) -> BuildStrategyType:
        """
        type is the kind of build strategy.
        """
        return self.__type

    def dockerStrategy(self) -> Optional["DockerBuildStrategy"]:
        """
        dockerStrategy holds the parameters to the container image build strategy.
        """
        return self.__dockerStrategy

    def sourceStrategy(self) -> Optional["SourceBuildStrategy"]:
        """
        sourceStrategy holds the parameters to the Source build strategy.
        """
        return self.__sourceStrategy

    def customStrategy(self) -> Optional["CustomBuildStrategy"]:
        """
        customStrategy holds the parameters to the Custom build strategy
        """
        return self.__customStrategy

    def jenkinsPipelineStrategy(self) -> Optional["JenkinsPipelineBuildStrategy"]:
        """
        JenkinsPipelineStrategy holds the parameters to the Jenkins Pipeline build strategy.
        """
        return self.__jenkinsPipelineStrategy


class CommonSpec(types.Object):
    """
    CommonSpec encapsulates all the inputs necessary to represent a build.
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        serviceAccount: str = None,
        source: "BuildSource" = None,
        revision: "SourceRevision" = None,
        strategy: "BuildStrategy" = None,
        output: "BuildOutput" = None,
        resources: "k8sv1.ResourceRequirements" = None,
        postCommit: "BuildPostCommitSpec" = None,
        completionDeadlineSeconds: int = None,
        nodeSelector: Dict[str, str] = None,
    ):
        super().__init__()
        self.__serviceAccount = serviceAccount
        self.__source = source if source is not None else BuildSource()
        self.__revision = revision
        self.__strategy = strategy if strategy is not None else BuildStrategy()
        self.__output = output if output is not None else BuildOutput()
        self.__resources = (
            resources if resources is not None else k8sv1.ResourceRequirements()
        )
        self.__postCommit = (
            postCommit if postCommit is not None else BuildPostCommitSpec()
        )
        self.__completionDeadlineSeconds = completionDeadlineSeconds
        self.__nodeSelector = nodeSelector if nodeSelector is not None else {}

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        serviceAccount = self.serviceAccount()
        check_type("serviceAccount", serviceAccount, Optional[str])
        if serviceAccount:  # omit empty
            v["serviceAccount"] = serviceAccount
        source = self.source()
        check_type("source", source, Optional["BuildSource"])
        v["source"] = source
        revision = self.revision()
        check_type("revision", revision, Optional["SourceRevision"])
        if revision is not None:  # omit empty
            v["revision"] = revision
        strategy = self.strategy()
        check_type("strategy", strategy, "BuildStrategy")
        v["strategy"] = strategy
        output = self.output()
        check_type("output", output, Optional["BuildOutput"])
        v["output"] = output
        resources = self.resources()
        check_type("resources", resources, Optional["k8sv1.ResourceRequirements"])
        v["resources"] = resources
        postCommit = self.postCommit()
        check_type("postCommit", postCommit, Optional["BuildPostCommitSpec"])
        v["postCommit"] = postCommit
        completionDeadlineSeconds = self.completionDeadlineSeconds()
        check_type(
            "completionDeadlineSeconds", completionDeadlineSeconds, Optional[int]
        )
        if completionDeadlineSeconds is not None:  # omit empty
            v["completionDeadlineSeconds"] = completionDeadlineSeconds
        nodeSelector = self.nodeSelector()
        check_type("nodeSelector", nodeSelector, Dict[str, str])
        v["nodeSelector"] = nodeSelector
        return v

    def serviceAccount(self) -> Optional[str]:
        """
        serviceAccount is the name of the ServiceAccount to use to run the pod
        created by this build.
        The pod will be allowed to use secrets referenced by the ServiceAccount
        """
        return self.__serviceAccount

    def source(self) -> Optional["BuildSource"]:
        """
        source describes the SCM in use.
        """
        return self.__source

    def revision(self) -> Optional["SourceRevision"]:
        """
        revision is the information from the source for a specific repo snapshot.
        This is optional.
        """
        return self.__revision

    def strategy(self) -> "BuildStrategy":
        """
        strategy defines how to perform a build.
        """
        return self.__strategy

    def output(self) -> Optional["BuildOutput"]:
        """
        output describes the container image the Strategy should produce.
        """
        return self.__output

    def resources(self) -> Optional["k8sv1.ResourceRequirements"]:
        """
        resources computes resource requirements to execute the build.
        """
        return self.__resources

    def postCommit(self) -> Optional["BuildPostCommitSpec"]:
        """
        postCommit is a build hook executed after the build output image is
        committed, before it is pushed to a registry.
        """
        return self.__postCommit

    def completionDeadlineSeconds(self) -> Optional[int]:
        """
        completionDeadlineSeconds is an optional duration in seconds, counted from
        the time when a build pod gets scheduled in the system, that the build may
        be active on a node before the system actively tries to terminate the
        build; value must be positive integer
        """
        return self.__completionDeadlineSeconds

    def nodeSelector(self) -> Dict[str, str]:
        """
        nodeSelector is a selector which must be true for the build pod to fit on a node
        If nil, it can be overridden by default build nodeselector values for the cluster.
        If set to an empty map or a map with any values, default build nodeselector values
        are ignored.
        """
        return self.__nodeSelector


class BuildSpec(types.Object):
    """
    BuildSpec has the information to represent a build and also additional
    information about a build
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        commonSpec: "CommonSpec" = None,
        triggeredBy: List["BuildTriggerCause"] = None,
    ):
        super().__init__()
        self.__commonSpec = commonSpec if commonSpec is not None else CommonSpec()
        self.__triggeredBy = triggeredBy if triggeredBy is not None else []

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        commonSpec = self.commonSpec()
        check_type("commonSpec", commonSpec, "CommonSpec")
        v.update(commonSpec._root())  # inline
        triggeredBy = self.triggeredBy()
        check_type("triggeredBy", triggeredBy, List["BuildTriggerCause"])
        v["triggeredBy"] = triggeredBy
        return v

    def commonSpec(self) -> "CommonSpec":
        """
        CommonSpec is the information that represents a build
        """
        return self.__commonSpec

    def triggeredBy(self) -> List["BuildTriggerCause"]:
        """
        triggeredBy describes which triggers started the most recent update to the
        build configuration and contains information about those triggers.
        """
        return self.__triggeredBy


class Build(base.TypedObject, base.NamespacedMetadataObject):
    """
    Build encapsulates the inputs needed to produce a new deployable image, as well as
    the status of the execution and a reference to the Pod which executed the build.
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        spec: "BuildSpec" = None,
    ):
        super().__init__(
            apiVersion="build.openshift.io/v1",
            kind="Build",
            **({"namespace": namespace} if namespace is not None else {}),
            **({"name": name} if name is not None else {}),
            **({"labels": labels} if labels is not None else {}),
            **({"annotations": annotations} if annotations is not None else {}),
        )
        self.__spec = spec if spec is not None else BuildSpec()

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        spec = self.spec()
        check_type("spec", spec, Optional["BuildSpec"])
        v["spec"] = spec
        return v

    def spec(self) -> Optional["BuildSpec"]:
        """
        spec is all the inputs used to execute the build.
        """
        return self.__spec


class ImageChangeTrigger(types.Object):
    """
    ImageChangeTrigger allows builds to be triggered when an ImageStream changes
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        lastTriggeredImageID: str = None,
        from_: "k8sv1.ObjectReference" = None,
        paused: bool = None,
    ):
        super().__init__()
        self.__lastTriggeredImageID = lastTriggeredImageID
        self.__from_ = from_
        self.__paused = paused

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        lastTriggeredImageID = self.lastTriggeredImageID()
        check_type("lastTriggeredImageID", lastTriggeredImageID, Optional[str])
        if lastTriggeredImageID:  # omit empty
            v["lastTriggeredImageID"] = lastTriggeredImageID
        from_ = self.from_()
        check_type("from_", from_, Optional["k8sv1.ObjectReference"])
        if from_ is not None:  # omit empty
            v["from"] = from_
        paused = self.paused()
        check_type("paused", paused, Optional[bool])
        if paused:  # omit empty
            v["paused"] = paused
        return v

    def lastTriggeredImageID(self) -> Optional[str]:
        """
        lastTriggeredImageID is used internally by the ImageChangeController to save last
        used image ID for build
        """
        return self.__lastTriggeredImageID

    def from_(self) -> Optional["k8sv1.ObjectReference"]:
        """
        from is a reference to an ImageStreamTag that will trigger a build when updated
        It is optional. If no From is specified, the From image from the build strategy
        will be used. Only one ImageChangeTrigger with an empty From reference is allowed in
        a build configuration.
        """
        return self.__from_

    def paused(self) -> Optional[bool]:
        """
        paused is true if this trigger is temporarily disabled. Optional.
        """
        return self.__paused


class SecretLocalReference(types.Object):
    """
    SecretLocalReference contains information that points to the local secret being used
    """

    @context.scoped
    @typechecked
    def __init__(self, name: str = ""):
        super().__init__()
        self.__name = name

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        name = self.name()
        check_type("name", name, str)
        v["name"] = name
        return v

    def name(self) -> str:
        """
        Name is the name of the resource in the same namespace being referenced
        """
        return self.__name


class WebHookTrigger(types.Object):
    """
    WebHookTrigger is a trigger that gets invoked using a webhook type of post
    """

    @context.scoped
    @typechecked
    def __init__(
        self, allowEnv: bool = None, secretReference: "SecretLocalReference" = None
    ):
        super().__init__()
        self.__allowEnv = allowEnv
        self.__secretReference = secretReference

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        allowEnv = self.allowEnv()
        check_type("allowEnv", allowEnv, Optional[bool])
        if allowEnv:  # omit empty
            v["allowEnv"] = allowEnv
        secretReference = self.secretReference()
        check_type("secretReference", secretReference, Optional["SecretLocalReference"])
        if secretReference is not None:  # omit empty
            v["secretReference"] = secretReference
        return v

    def allowEnv(self) -> Optional[bool]:
        """
        allowEnv determines whether the webhook can set environment variables; can only
        be set to true for GenericWebHook.
        """
        return self.__allowEnv

    def secretReference(self) -> Optional["SecretLocalReference"]:
        """
        secretReference is a reference to a secret in the same namespace,
        containing the value to be validated when the webhook is invoked.
        The secret being referenced must contain a key named "WebHookSecretKey", the value
        of which will be checked against the value supplied in the webhook invocation.
        """
        return self.__secretReference


class BuildTriggerPolicy(types.Object):
    """
    BuildTriggerPolicy describes a policy for a single trigger that results in a new Build.
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        type: BuildTriggerType = None,
        github: "WebHookTrigger" = None,
        generic: "WebHookTrigger" = None,
        imageChange: "ImageChangeTrigger" = None,
        gitlab: "WebHookTrigger" = None,
        bitbucket: "WebHookTrigger" = None,
    ):
        super().__init__()
        self.__type = type
        self.__github = github
        self.__generic = generic
        self.__imageChange = imageChange
        self.__gitlab = gitlab
        self.__bitbucket = bitbucket

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        type = self.type()
        check_type("type", type, BuildTriggerType)
        v["type"] = type
        github = self.github()
        check_type("github", github, Optional["WebHookTrigger"])
        if github is not None:  # omit empty
            v["github"] = github
        generic = self.generic()
        check_type("generic", generic, Optional["WebHookTrigger"])
        if generic is not None:  # omit empty
            v["generic"] = generic
        imageChange = self.imageChange()
        check_type("imageChange", imageChange, Optional["ImageChangeTrigger"])
        if imageChange is not None:  # omit empty
            v["imageChange"] = imageChange
        gitlab = self.gitlab()
        check_type("gitlab", gitlab, Optional["WebHookTrigger"])
        if gitlab is not None:  # omit empty
            v["gitlab"] = gitlab
        bitbucket = self.bitbucket()
        check_type("bitbucket", bitbucket, Optional["WebHookTrigger"])
        if bitbucket is not None:  # omit empty
            v["bitbucket"] = bitbucket
        return v

    def type(self) -> BuildTriggerType:
        """
        type is the type of build trigger
        """
        return self.__type

    def github(self) -> Optional["WebHookTrigger"]:
        """
        github contains the parameters for a GitHub webhook type of trigger
        """
        return self.__github

    def generic(self) -> Optional["WebHookTrigger"]:
        """
        generic contains the parameters for a Generic webhook type of trigger
        """
        return self.__generic

    def imageChange(self) -> Optional["ImageChangeTrigger"]:
        """
        imageChange contains parameters for an ImageChange type of trigger
        """
        return self.__imageChange

    def gitlab(self) -> Optional["WebHookTrigger"]:
        """
        GitLabWebHook contains the parameters for a GitLab webhook type of trigger
        """
        return self.__gitlab

    def bitbucket(self) -> Optional["WebHookTrigger"]:
        """
        BitbucketWebHook contains the parameters for a Bitbucket webhook type of
        trigger
        """
        return self.__bitbucket


class BuildConfigSpec(types.Object):
    """
    BuildConfigSpec describes when and how builds are created
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        triggers: List["BuildTriggerPolicy"] = None,
        runPolicy: BuildRunPolicy = BuildRunPolicy["Serial"],
        commonSpec: "CommonSpec" = None,
        successfulBuildsHistoryLimit: int = None,
        failedBuildsHistoryLimit: int = None,
    ):
        super().__init__()
        self.__triggers = triggers if triggers is not None else []
        self.__runPolicy = runPolicy
        self.__commonSpec = commonSpec if commonSpec is not None else CommonSpec()
        self.__successfulBuildsHistoryLimit = successfulBuildsHistoryLimit
        self.__failedBuildsHistoryLimit = failedBuildsHistoryLimit

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        triggers = self.triggers()
        check_type("triggers", triggers, List["BuildTriggerPolicy"])
        v["triggers"] = triggers
        runPolicy = self.runPolicy()
        check_type("runPolicy", runPolicy, Optional[BuildRunPolicy])
        if runPolicy:  # omit empty
            v["runPolicy"] = runPolicy
        commonSpec = self.commonSpec()
        check_type("commonSpec", commonSpec, "CommonSpec")
        v.update(commonSpec._root())  # inline
        successfulBuildsHistoryLimit = self.successfulBuildsHistoryLimit()
        check_type(
            "successfulBuildsHistoryLimit", successfulBuildsHistoryLimit, Optional[int]
        )
        if successfulBuildsHistoryLimit is not None:  # omit empty
            v["successfulBuildsHistoryLimit"] = successfulBuildsHistoryLimit
        failedBuildsHistoryLimit = self.failedBuildsHistoryLimit()
        check_type("failedBuildsHistoryLimit", failedBuildsHistoryLimit, Optional[int])
        if failedBuildsHistoryLimit is not None:  # omit empty
            v["failedBuildsHistoryLimit"] = failedBuildsHistoryLimit
        return v

    def triggers(self) -> List["BuildTriggerPolicy"]:
        """
        triggers determine how new Builds can be launched from a BuildConfig. If
        no triggers are defined, a new build can only occur as a result of an
        explicit client build creation.
        """
        return self.__triggers

    def runPolicy(self) -> Optional[BuildRunPolicy]:
        """
        RunPolicy describes how the new build created from this build
        configuration will be scheduled for execution.
        This is optional, if not specified we default to "Serial".
        """
        return self.__runPolicy

    def commonSpec(self) -> "CommonSpec":
        """
        CommonSpec is the desired build specification
        """
        return self.__commonSpec

    def successfulBuildsHistoryLimit(self) -> Optional[int]:
        """
        successfulBuildsHistoryLimit is the number of old successful builds to retain.
        When a BuildConfig is created, the 5 most recent successful builds are retained unless this value is set.
        If removed after the BuildConfig has been created, all successful builds are retained.
        """
        return self.__successfulBuildsHistoryLimit

    def failedBuildsHistoryLimit(self) -> Optional[int]:
        """
        failedBuildsHistoryLimit is the number of old failed builds to retain.
        When a BuildConfig is created, the 5 most recent failed builds are retained unless this value is set.
        If removed after the BuildConfig has been created, all failed builds are retained.
        """
        return self.__failedBuildsHistoryLimit


class BuildConfig(base.TypedObject, base.NamespacedMetadataObject):
    """
    Build configurations define a build process for new container images. There are three types of builds possible - a container image build using a Dockerfile, a Source-to-Image build that uses a specially prepared base image that accepts source code that it can make runnable, and a custom build that can run // arbitrary container images as a base and accept the build parameters. Builds run on the cluster and on completion are pushed to the container image registry specified in the "output" section. A build can be triggered via a webhook, when the base image changes, or when a user manually requests a new build be // created.
    
    Each build created by a build configuration is numbered and refers back to its parent configuration. Multiple builds can be triggered at once. Builds that do not have "output" set can be used to test code or run a verification build.
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        spec: "BuildConfigSpec" = None,
    ):
        super().__init__(
            apiVersion="build.openshift.io/v1",
            kind="BuildConfig",
            **({"namespace": namespace} if namespace is not None else {}),
            **({"name": name} if name is not None else {}),
            **({"labels": labels} if labels is not None else {}),
            **({"annotations": annotations} if annotations is not None else {}),
        )
        self.__spec = spec if spec is not None else BuildConfigSpec()

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        spec = self.spec()
        check_type("spec", spec, "BuildConfigSpec")
        v["spec"] = spec
        return v

    def spec(self) -> "BuildConfigSpec":
        """
        spec holds all the input necessary to produce a new build, and the conditions when
        to trigger them.
        """
        return self.__spec


class BuildLog(base.TypedObject):
    """
    BuildLog is the (unused) resource associated with the build log redirector
    """

    @context.scoped
    @typechecked
    def __init__(self):
        super().__init__(apiVersion="build.openshift.io/v1", kind="BuildLog")

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        return v


class BuildLogOptions(base.TypedObject):
    """
    BuildLogOptions is the REST options for a build log
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        container: str = None,
        follow: bool = None,
        previous: bool = None,
        sinceSeconds: int = None,
        sinceTime: "base.Time" = None,
        timestamps: bool = None,
        tailLines: int = None,
        limitBytes: int = None,
        nowait: bool = None,
        version: int = None,
    ):
        super().__init__(apiVersion="build.openshift.io/v1", kind="BuildLogOptions")
        self.__container = container
        self.__follow = follow
        self.__previous = previous
        self.__sinceSeconds = sinceSeconds
        self.__sinceTime = sinceTime
        self.__timestamps = timestamps
        self.__tailLines = tailLines
        self.__limitBytes = limitBytes
        self.__nowait = nowait
        self.__version = version

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        container = self.container()
        check_type("container", container, Optional[str])
        if container:  # omit empty
            v["container"] = container
        follow = self.follow()
        check_type("follow", follow, Optional[bool])
        if follow:  # omit empty
            v["follow"] = follow
        previous = self.previous()
        check_type("previous", previous, Optional[bool])
        if previous:  # omit empty
            v["previous"] = previous
        sinceSeconds = self.sinceSeconds()
        check_type("sinceSeconds", sinceSeconds, Optional[int])
        if sinceSeconds is not None:  # omit empty
            v["sinceSeconds"] = sinceSeconds
        sinceTime = self.sinceTime()
        check_type("sinceTime", sinceTime, Optional["base.Time"])
        if sinceTime is not None:  # omit empty
            v["sinceTime"] = sinceTime
        timestamps = self.timestamps()
        check_type("timestamps", timestamps, Optional[bool])
        if timestamps:  # omit empty
            v["timestamps"] = timestamps
        tailLines = self.tailLines()
        check_type("tailLines", tailLines, Optional[int])
        if tailLines is not None:  # omit empty
            v["tailLines"] = tailLines
        limitBytes = self.limitBytes()
        check_type("limitBytes", limitBytes, Optional[int])
        if limitBytes is not None:  # omit empty
            v["limitBytes"] = limitBytes
        nowait = self.nowait()
        check_type("nowait", nowait, Optional[bool])
        if nowait:  # omit empty
            v["nowait"] = nowait
        version = self.version()
        check_type("version", version, Optional[int])
        if version is not None:  # omit empty
            v["version"] = version
        return v

    def container(self) -> Optional[str]:
        """
        cointainer for which to stream logs. Defaults to only container if there is one container in the pod.
        """
        return self.__container

    def follow(self) -> Optional[bool]:
        """
        follow if true indicates that the build log should be streamed until
        the build terminates.
        """
        return self.__follow

    def previous(self) -> Optional[bool]:
        """
        previous returns previous build logs. Defaults to false.
        """
        return self.__previous

    def sinceSeconds(self) -> Optional[int]:
        """
        sinceSeconds is a relative time in seconds before the current time from which to show logs. If this value
        precedes the time a pod was started, only logs since the pod start will be returned.
        If this value is in the future, no logs will be returned.
        Only one of sinceSeconds or sinceTime may be specified.
        """
        return self.__sinceSeconds

    def sinceTime(self) -> Optional["base.Time"]:
        """
        sinceTime is an RFC3339 timestamp from which to show logs. If this value
        precedes the time a pod was started, only logs since the pod start will be returned.
        If this value is in the future, no logs will be returned.
        Only one of sinceSeconds or sinceTime may be specified.
        """
        return self.__sinceTime

    def timestamps(self) -> Optional[bool]:
        """
        timestamps, If true, add an RFC3339 or RFC3339Nano timestamp at the beginning of every line
        of log output. Defaults to false.
        """
        return self.__timestamps

    def tailLines(self) -> Optional[int]:
        """
        tailLines, If set, is the number of lines from the end of the logs to show. If not specified,
        logs are shown from the creation of the container or sinceSeconds or sinceTime
        """
        return self.__tailLines

    def limitBytes(self) -> Optional[int]:
        """
        limitBytes, If set, is the number of bytes to read from the server before terminating the
        log output. This may not display a complete final line of logging, and may return
        slightly more or slightly less than the specified limit.
        """
        return self.__limitBytes

    def nowait(self) -> Optional[bool]:
        """
        noWait if true causes the call to return immediately even if the build
        is not available yet. Otherwise the server will wait until the build has started.
        TODO: Fix the tag to 'noWait' in v2
        """
        return self.__nowait

    def version(self) -> Optional[int]:
        """
        version of the build for which to view logs.
        """
        return self.__version


class DockerStrategyOptions(types.Object):
    """
    DockerStrategyOptions contains extra strategy options for container image builds
    """

    @context.scoped
    @typechecked
    def __init__(self, buildArgs: List["k8sv1.EnvVar"] = None, noCache: bool = None):
        super().__init__()
        self.__buildArgs = buildArgs if buildArgs is not None else []
        self.__noCache = noCache

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        buildArgs = self.buildArgs()
        check_type("buildArgs", buildArgs, Optional[List["k8sv1.EnvVar"]])
        if buildArgs:  # omit empty
            v["buildArgs"] = buildArgs
        noCache = self.noCache()
        check_type("noCache", noCache, Optional[bool])
        if noCache is not None:  # omit empty
            v["noCache"] = noCache
        return v

    def buildArgs(self) -> Optional[List["k8sv1.EnvVar"]]:
        """
        Args contains any build arguments that are to be passed to Docker.  See
        https://docs.docker.com/engine/reference/builder/#/arg for more details
        """
        return self.__buildArgs

    def noCache(self) -> Optional[bool]:
        """
        noCache overrides the docker-strategy noCache option in the build config
        """
        return self.__noCache


class SourceStrategyOptions(types.Object):
    """
    SourceStrategyOptions contains extra strategy options for Source builds
    """

    @context.scoped
    @typechecked
    def __init__(self, incremental: bool = None):
        super().__init__()
        self.__incremental = incremental

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        incremental = self.incremental()
        check_type("incremental", incremental, Optional[bool])
        if incremental is not None:  # omit empty
            v["incremental"] = incremental
        return v

    def incremental(self) -> Optional[bool]:
        """
        incremental overrides the source-strategy incremental option in the build config
        """
        return self.__incremental


class BuildRequest(base.TypedObject, base.NamespacedMetadataObject):
    """
    BuildRequest is the resource used to pass parameters to build generator
    """

    @context.scoped
    @typechecked
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        revision: "SourceRevision" = None,
        triggeredByImage: "k8sv1.ObjectReference" = None,
        from_: "k8sv1.ObjectReference" = None,
        binary: "BinaryBuildSource" = None,
        lastVersion: int = None,
        env: List["k8sv1.EnvVar"] = None,
        triggeredBy: List["BuildTriggerCause"] = None,
        dockerStrategyOptions: "DockerStrategyOptions" = None,
        sourceStrategyOptions: "SourceStrategyOptions" = None,
    ):
        super().__init__(
            apiVersion="build.openshift.io/v1",
            kind="BuildRequest",
            **({"namespace": namespace} if namespace is not None else {}),
            **({"name": name} if name is not None else {}),
            **({"labels": labels} if labels is not None else {}),
            **({"annotations": annotations} if annotations is not None else {}),
        )
        self.__revision = revision
        self.__triggeredByImage = triggeredByImage
        self.__from_ = from_
        self.__binary = binary
        self.__lastVersion = lastVersion
        self.__env = env if env is not None else []
        self.__triggeredBy = triggeredBy if triggeredBy is not None else []
        self.__dockerStrategyOptions = dockerStrategyOptions
        self.__sourceStrategyOptions = sourceStrategyOptions

    @typechecked
    def _root(self) -> Dict[str, Any]:
        v = super()._root()
        revision = self.revision()
        check_type("revision", revision, Optional["SourceRevision"])
        if revision is not None:  # omit empty
            v["revision"] = revision
        triggeredByImage = self.triggeredByImage()
        check_type(
            "triggeredByImage", triggeredByImage, Optional["k8sv1.ObjectReference"]
        )
        if triggeredByImage is not None:  # omit empty
            v["triggeredByImage"] = triggeredByImage
        from_ = self.from_()
        check_type("from_", from_, Optional["k8sv1.ObjectReference"])
        if from_ is not None:  # omit empty
            v["from"] = from_
        binary = self.binary()
        check_type("binary", binary, Optional["BinaryBuildSource"])
        if binary is not None:  # omit empty
            v["binary"] = binary
        lastVersion = self.lastVersion()
        check_type("lastVersion", lastVersion, Optional[int])
        if lastVersion is not None:  # omit empty
            v["lastVersion"] = lastVersion
        env = self.env()
        check_type("env", env, Optional[List["k8sv1.EnvVar"]])
        if env:  # omit empty
            v["env"] = env
        triggeredBy = self.triggeredBy()
        check_type("triggeredBy", triggeredBy, List["BuildTriggerCause"])
        v["triggeredBy"] = triggeredBy
        dockerStrategyOptions = self.dockerStrategyOptions()
        check_type(
            "dockerStrategyOptions",
            dockerStrategyOptions,
            Optional["DockerStrategyOptions"],
        )
        if dockerStrategyOptions is not None:  # omit empty
            v["dockerStrategyOptions"] = dockerStrategyOptions
        sourceStrategyOptions = self.sourceStrategyOptions()
        check_type(
            "sourceStrategyOptions",
            sourceStrategyOptions,
            Optional["SourceStrategyOptions"],
        )
        if sourceStrategyOptions is not None:  # omit empty
            v["sourceStrategyOptions"] = sourceStrategyOptions
        return v

    def revision(self) -> Optional["SourceRevision"]:
        """
        revision is the information from the source for a specific repo snapshot.
        """
        return self.__revision

    def triggeredByImage(self) -> Optional["k8sv1.ObjectReference"]:
        """
        triggeredByImage is the Image that triggered this build.
        """
        return self.__triggeredByImage

    def from_(self) -> Optional["k8sv1.ObjectReference"]:
        """
        from is the reference to the ImageStreamTag that triggered the build.
        """
        return self.__from_

    def binary(self) -> Optional["BinaryBuildSource"]:
        """
        binary indicates a request to build from a binary provided to the builder
        """
        return self.__binary

    def lastVersion(self) -> Optional[int]:
        """
        lastVersion (optional) is the LastVersion of the BuildConfig that was used
        to generate the build. If the BuildConfig in the generator doesn't match, a build will
        not be generated.
        """
        return self.__lastVersion

    def env(self) -> Optional[List["k8sv1.EnvVar"]]:
        """
        env contains additional environment variables you want to pass into a builder container.
        """
        return self.__env

    def triggeredBy(self) -> List["BuildTriggerCause"]:
        """
        triggeredBy describes which triggers started the most recent update to the
        build configuration and contains information about those triggers.
        """
        return self.__triggeredBy

    def dockerStrategyOptions(self) -> Optional["DockerStrategyOptions"]:
        """
        DockerStrategyOptions contains additional docker-strategy specific options for the build
        """
        return self.__dockerStrategyOptions

    def sourceStrategyOptions(self) -> Optional["SourceStrategyOptions"]:
        """
        SourceStrategyOptions contains additional source-strategy specific options for the build
        """
        return self.__sourceStrategyOptions
