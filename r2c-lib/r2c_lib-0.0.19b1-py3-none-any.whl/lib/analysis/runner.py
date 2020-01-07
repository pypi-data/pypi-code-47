import copy
import json
import logging
import os
import pathlib
import subprocess
import sys
import threading
import time
from pathlib import Path
from typing import Any, List, NewType, Optional, Tuple, Union, cast

import attr
import docker
import jsonschema

from r2c.lib.analysis import (
    DependencyMounter,
    ExecutionEntry,
    ExecutionOrder,
    MountManager,
    OutputStorage,
    get_manager,
)
from r2c.lib.analyzer import SpecifiedAnalyzer, VersionedAnalyzer
from r2c.lib.errors import AnalyzerOutputNotFound
from r2c.lib.filestore import FileStore
from r2c.lib.input import AnalyzerInput, GitRepoCommit, LocalCode
from r2c.lib.jobdef import CacheKey
from r2c.lib.manifest import AnalyzerManifest, AnalyzerOutputType
from r2c.lib.registry import RegistryData
from r2c.lib.util import Timeout

ContainerLog = NewType("ContainerLog", str)
ContainerStats = NewType("ContainerStats", List[Any])
VOLUME_MOUNT_IN_DOCKER = "/analysis"


def watch_log(stream, is_stdout):
    """Helper function that we run in a thread to preserve stdout/stderr distinction from the docker container
    """
    for line in stream:
        if is_stdout:
            sys.stdout.write(line.decode("utf-8"))
        else:
            sys.stderr.write(line.decode("utf-8"))


@attr.s(auto_attribs=True, frozen=True)
class AnalyzerNonZeroExitError(Exception):
    """
        Thrown when analyzer docker container exists with non-zero exit code
    """

    status_code: int
    log: ContainerLog
    stats: Any
    versioned_analyzer: Optional[VersionedAnalyzer] = None

    def __str__(self):
        analyzer = self.versioned_analyzer if self.versioned_analyzer else "unknown"
        return f"Analyzer {analyzer} finished with non-zero exit code: {self.status_code}.\n Container log:\n {self.log}"


class AnalyzerImagePullFail(Exception):
    """
        Thrown when analyzer image fails to pull
    """


@attr.s(auto_attribs=True)
class InvalidAnalyzerOutput(Exception):
    """Thrown when the analyzer's output doesn't conform to its schema."""

    inner: Union[jsonschema.ValidationError, json.JSONDecodeError]


@attr.s(auto_attribs=True)
class AnalysisRunner:
    _registry_data: RegistryData
    _output_storage: OutputStorage
    _log_store: FileStore
    _stats_store: FileStore
    # Controls whether analyzer stdout/stderr is forwarded to the process's
    # stdout/stderr.
    _pass_analyzer_output: bool = False
    _timeout: int = 1200
    # If set, should be a string like "2G" or "1024M".
    _memory_limit: Optional[str] = None
    _env_args_dict: Optional[dict] = None
    _docker_client: Any = attr.ib(factory=lambda: docker.from_env(), init=False)
    _logger: logging.Logger = attr.ib(
        factory=lambda: logging.getLogger(__name__), init=False
    )
    dependency_mounter: DependencyMounter = attr.ib(init=False)

    @dependency_mounter.default
    def _build_dependency_mounter(self) -> DependencyMounter:
        return DependencyMounter(self._registry_data, self._output_storage)

    def reset_registry_data(self, registry_data: RegistryData) -> None:
        self._registry_data.data = copy.deepcopy(registry_data.data)

    @staticmethod
    def get_analyzer_output_path(
        output_dir: Path, output_type: AnalyzerOutputType
    ) -> Path:
        """For an analyzer of this output type, where does the single-file output live?

        """
        if output_type == AnalyzerOutputType.json:
            return output_dir / "output.json"
        elif output_type == AnalyzerOutputType.filesystem:
            return output_dir / "fs.tar.gz"
        else:
            raise RuntimeError(
                f"non-implemented; don't know where to find output for analyzer with output type: {output_type}"
            )

    def full_analyze_request(
        self,
        analyzer_input: AnalyzerInput,
        specified_analyzer: SpecifiedAnalyzer,
        force: bool,
        interactive: Optional[Union[int, str]] = None,
    ) -> dict:
        """
            Handle an analysis request and uploading output.

            Args:
                specified_analyzer: unique identifier for analyzer container to run w/ parameter
                analyzed_input: input to analyze
                force: if true, the analysis will proceed even if there is already a cached result for this request.
                interactive: if set, the analyzer in the execution graph (defaults to last if interactive_index not specified)  will drop into shell rather than running automatically.

            Returns:
                A dict with information about the final output last analyzer in the dependency graph to run.
        """

        execution_order = ExecutionOrder.compute(
            self._registry_data,
            analyzer=specified_analyzer,
            interactive=interactive,
            analyzer_input=analyzer_input,
        )

        analyzer_execution_str = "".join(
            [
                f"\n\t{i}: {entry.analyzer}"
                for i, entry in enumerate(execution_order.all_phases())
            ]
        )
        self._logger.info(
            f"All analyzers that will be run, in order: {analyzer_execution_str}"
        )

        self._logger.info("Executing fetch phase")
        self.dependency_mounter.fetched_code = self._fetch_input(
            analyzer_input, execution_order, force=force
        )
        self._logger.info(
            f"Code fetched, located at {self.dependency_mounter.fetched_code}"
        )

        skipped = True
        for entry in execution_order.analysis_phase:
            if self._analyze(entry, analyzer_input, force=force):
                skipped = False

        output_type = self._registry_data.manifest_for(
            specified_analyzer.versioned_analyzer
        ).output_type
        return {"skipped": skipped, "output_type": output_type.name}

    def _fetch_input(
        self,
        analyzer_input: AnalyzerInput,
        execution_order: ExecutionOrder,
        force: bool,
    ) -> Path:
        """Fetches the given input, returning a path to it on disk.

        If the input is a LocalCode, it just returns its code_dir, since we
        already have it on disk.
        """
        if isinstance(analyzer_input, LocalCode):
            assert not execution_order.fetch_phase
            return Path(analyzer_input.code_dir)

        assert execution_order.code_fetcher
        for entry in execution_order.fetch_phase:
            self._analyze(entry, analyzer_input, force=force)

        fetched = self._output_storage.fetch_analyzer_output(
            CacheKey(analyzer=execution_order.code_fetcher, input=analyzer_input),
            AnalyzerOutputType.filesystem,
        )
        if fetched is None:
            # should never happen, since we just ran the code fetcher
            raise RuntimeError(
                f"Failed to find output of analyzer {execution_order.code_fetcher}?"
            )
        return fetched

    def _validate_output(self, manifest: AnalyzerManifest, output_dir: Path) -> None:
        """Validates the output, then migrates it to the latest schema.

        Note that if the analyzer's output is not JSON, this does nothing since
        we don't have a way to validate non-JSON outputs.

        Throws:
            InvalidAnalyzerOutput: If validation fails.

        """
        if manifest.output_type != AnalyzerOutputType.json:
            return

        path = self.get_analyzer_output_path(output_dir, manifest.output_type)
        with open(path) as f:
            try:
                output = json.load(f)
            except json.JSONDecodeError as err:
                raise InvalidAnalyzerOutput(err)

        try:
            manifest.output.validator(output).validate(output)
        except jsonschema.ValidationError as err:
            raise InvalidAnalyzerOutput(err) from err
        except Exception as err:
            raise RuntimeError(
                f"There was an error validating your output. Please check that you're outputing a valid output and try again: {err}"
            )

    def upload_output(self, cache_key: CacheKey, output_dir: Path) -> Path:
        """
            Upload analyzer results

            Args:
                specified_analyzer: uniquely identifies analyzer container w/ parameters
                analyzer_input: the input that was analyzed
                manager: The MountManager used to talk with the analyzer

            Returns:
                The inside-container path to the analyzer output that was uploaded.

            Raises:
                InvalidAnalyzerOutput: if output fails to validate
                                       note that output is still uploaded
        """
        manifest = self._registry_data.manifest_for(
            cache_key.analyzer.versioned_analyzer
        )
        output_path = self._output_storage.upload(
            cache_key, manifest.output_type, output_dir
        )

        # Invalid outputs should still be uploaded, but we want to
        # count them as failing.
        self._validate_output(manifest, output_dir)
        return output_path

    def prepare_mount_volume(
        self, specified_analyzer: SpecifiedAnalyzer, analyzer_input: AnalyzerInput
    ) -> MountManager:
        """
            Prepares directory to be mounted to docker container IMAGE_ID to
            run analysis on analyzer input. Raises exception when cannot
            prepare directory with necessary dependencies.

            Args:
                specified_analyzer: uniquely identifies analyzer container w/ parameters
                analyzer_input: input to run analysis on

            Returns:
                A MountManager context manager. The input will be cleaned up when this returns.
        """
        manager = get_manager(pathlib.Path(VOLUME_MOUNT_IN_DOCKER), self._docker_client)
        input_dir = manager.input_dir()
        with (input_dir / "parameters.json").open("w") as f:
            json.dump(specified_analyzer.parameters, f)
        with (input_dir / "target.json").open("w") as f:
            json.dump(analyzer_input.to_json(), f)

        # TODO: remove this after fixing cloner to respect new target file
        if isinstance(analyzer_input, GitRepoCommit):
            repo_commit = cast(GitRepoCommit, analyzer_input)
            arguments = {
                "git_url": repo_commit.repo_url,
                "commit_hash": repo_commit.commit_hash,
            }
            with (input_dir / "cloner-input.json").open("w") as f:
                json.dump(arguments, f)

        self.dependency_mounter.mount_all(specified_analyzer, analyzer_input, manager)

        return manager

    def _docker_pull_with_retry(self, image_id, max_tries=5):
        num_tries = 0
        time_sleep = 2
        while True:
            num_tries += 1
            try:
                with Timeout(900):
                    self._logger.info(f"Trying to pull {image_id}")
                    self._docker_client.images.pull(image_id)
                    break
            except Exception as e:
                if num_tries > max_tries:
                    raise e

                self._logger.info(f"Docker pull failed {e} sleeping for {time_sleep}")
                # Maybe hitting API limits. Sleep for a while
                time.sleep(time_sleep)
                time_sleep *= 2
                continue

    def _has_network_privileges(self, versioned_analyzer: VersionedAnalyzer) -> bool:
        # Eventually, we'll have some kind of whitelist mechanism. For now we
        # just let everything use the network.
        return True

    def run_image_on_folder(
        self,
        versioned_analyzer: VersionedAnalyzer,
        manager: MountManager,
        interactive: bool,
    ) -> Tuple[ContainerLog, ContainerStats]:
        """
            Mount MOUNT_FOLDER as /analysis in docker container and run IMAGE_ID on it

            Args:
                versioned_analyzer: uniquely identifies docker image, as well as name and version
                mount_folder: path to directory we will mount as /analysis. In analyzer spec v3
                this is the directory that contains inputs/ and output. Assumes this directory is
                properly prepared
                interactive: if true, change the run command so that it drops into bash shell. Useful for debugging.
            Raises:
                AnalyzerImagePullFail: if IMAGE_ID is not available and fails to pull
                TimeoutError: on timeout
                AnalyzerNonZeroExitError: when container exits with non-zero exit code
            Returns:
                container_log: stdout and err of container as a string
        """
        image_id = versioned_analyzer.image_id
        try:
            self._docker_client.images.get(image_id)
        except docker.errors.ImageNotFound:
            self._logger.info(f"Image {image_id} not found. Pulling.")
            try:
                self._docker_pull_with_retry(image_id)
            except Exception as e:
                raise AnalyzerImagePullFail(str(e))
        container = None
        stats = []

        # we can't use volume mounting with remote docker (for example, on
        # CircleCI), have to docker cp
        is_remote_docker = os.environ.get("DOCKER_HOST") is not None

        if is_remote_docker and interactive:
            self._logger.error("Wait for start not supported with remote docker client")
            interactive = False

        self._logger.info(
            f"""Running container {image_id} (memory limit: {self._memory_limit})"""
        )

        try:
            with Timeout(self._timeout):
                container = self._docker_client.containers.create(
                    image_id,
                    volumes=manager.volumes(),
                    command="tail -f /dev/null" if interactive else None,
                    mem_limit=self._memory_limit,
                    environment=self._env_args_dict,
                    network_mode="bridge"
                    if self._has_network_privileges(versioned_analyzer)
                    else "none",
                )

                container.start()

                if interactive:
                    self._logger.info(
                        f"\n\nYour container is ready: running \n\tdocker exec -i -t {container.id} /bin/sh"
                    )
                    subprocess.call(
                        ["docker", "exec", "-i", "-t", container.id, "/bin/sh"]
                    )
                    sys.exit(1)

                # launch two threads to display stdout and stderr while the container is running
                if self._pass_analyzer_output:
                    stdout_watch = threading.Thread(
                        target=watch_log,
                        args=(
                            container.logs(stdout=True, stderr=False, stream=True),
                            True,
                        ),
                    )
                    stdout_watch.start()
                try:
                    for stat in container.stats(decode=True, stream=True):
                        if (
                            stat["read"] == "0001-01-01T00:00:00Z"
                        ):  # stats from stopped containers is 0 so read stats until this
                            break
                        stats.append(stat)
                        self._logger.info(f"Collected stat from {container.id}")
                        container.reload()  # refresh from server
                        if container.status != "running":
                            break
                except TimeoutError as e:
                    self._logger.info(
                        "caught TimeoutError in stats collection, re-raising"
                    )
                    raise e  # don't catch timeout errors
                except Exception as e:
                    self._logger.exception("error getting stats")
                    raise e  # TODO Somehow TimeoutErrors are being hidden under other errors. For now just raise everything

                # Block until completion
                # We run with container detached so we can kill on timeout
                status = container.wait()

                # Retrieve status code and logs before removing container
                status_code = status.get("StatusCode")

                # full, merged stdout + stderr log
                container_log = container.logs(stdout=True, stderr=True).decode("utf-8")
                # self._logger.info(f"Container output: {container_log}")

                container.remove()
                container = None

            if status_code != 0:
                raise AnalyzerNonZeroExitError(
                    status_code, container_log, stats, versioned_analyzer
                )

        except Exception as e:
            # skip AnalyzerNonZeroExitError for debugability
            if isinstance(e, AnalyzerNonZeroExitError):
                raise e

            self._logger.exception(f"There was an error running {image_id}: {e}")

            if container:
                self._logger.info(f"killing container {container.id}")
                try:
                    # Kill and Remove Container as well as associated volumes
                    container.remove(v=True, force=True)
                    self._logger.info(f"successfully killed container {container.id}")
                except Exception:
                    self._logger.exception("error killing container")

            raise e

        return ContainerLog(container_log), ContainerStats(stats)

    def _analyze(
        self, entry: ExecutionEntry, analyzer_input: AnalyzerInput, force: bool
    ) -> bool:
        """Runs the analysis specified by the given execution entry.

        This also uploads the output to the JSON/filessytem output stores.

        If `force` is true, then the analyzer is run even if there's cached
        output.

        Returns:
            Whether analysis was actually run.

        """
        analyzer = entry.analyzer
        interactive = entry.interactive
        if interactive:
            print(f"Calling `docker exec` into {analyzer}")
        self._logger.info(f"Running {analyzer}")
        cache_key = CacheKey(analyzer=analyzer, input=analyzer_input)

        if (
            # TODO check freshness here
            self.dependency_mounter.contains(
                CacheKey(analyzer=analyzer, input=analyzer_input)
            )
            and not force
            and not interactive
        ):
            # use cache when non-interactive, non-forcing, dependency
            self._logger.info(
                f"Analysis for {analyzer_input.to_json()} {analyzer} already exists. Keeping old analysis report"
            )
            return False

        try:
            with self.prepare_mount_volume(analyzer, analyzer_input) as manager:
                manager.copy_input()
                container_log, stats = self.run_image_on_folder(
                    versioned_analyzer=analyzer.versioned_analyzer,
                    manager=manager,
                    interactive=interactive,
                )
                manager.copy_output()
                # This has to go inside the manager with-block because the
                # manager will clean up after itself.
                try:
                    self.upload_output(cache_key, manager.output_dir())
                except FileNotFoundError:
                    output_type = self._registry_data.manifest_for(
                        analyzer.versioned_analyzer
                    ).output_type
                    output_path = self.get_analyzer_output_path(
                        Path(VOLUME_MOUNT_IN_DOCKER) / "output", output_type
                    )
                    raise AnalyzerOutputNotFound(output_path=str(output_path))
        except AnalyzerNonZeroExitError as e:
            container_log = e.log
            stats = e.stats
            self._log_store.write(cache_key, container_log)
            self._logger.info(f"Uploading analyzer stats: {len(stats)}")
            self._stats_store.write(cache_key, json.dumps(stats))
            raise e

        self._logger.info("Analyzer finished running.")
        self._logger.info("Uploading analyzer log")
        self._log_store.write(cache_key, container_log)
        self._logger.info(f"Uploading analyzer stats: {len(stats)}")
        self._stats_store.write(cache_key, json.dumps(stats))

        self._logger.info("Uploading analyzer output")

        return True
