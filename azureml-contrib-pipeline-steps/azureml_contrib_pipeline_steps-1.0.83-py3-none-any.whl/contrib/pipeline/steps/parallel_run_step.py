# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""To add a step to run user's script in parallel mode on multiple aml-compute targets."""
import logging
import re
import json
import os
import sys

from azureml.contrib.pipeline.steps import ParallelRunConfig
from azureml.core import Workspace
from azureml.core.runconfig import RunConfiguration
from azureml.core.conda_dependencies import CondaDependencies
from azureml.core.datastore import Datastore
from azureml.data.azure_storage_datastore import AzureBlobDatastore
from azureml.data.data_reference import DataReference
from azureml.data.dataset_consumption_config import DatasetConsumptionConfig
from azureml.data.file_dataset import FileDataset
from azureml.data.tabular_dataset import TabularDataset
from azureml.pipeline.steps import PythonScriptStep
from azureml.pipeline.core.graph import PipelineParameter
from azureml.pipeline.core.graph import ParamDef
from azureml.pipeline.core.pipeline_output_dataset import PipelineOutputFileDataset

DEFAULT_BATCH_SCORE_MAIN_FILE_NAME = "driver/amlbi_main.py"
DEFAULT_MINI_BATCH_SIZE = 1
DEFAULT_MINI_BATCH_SIZE_FILEDATASET = 10
DEFAULT_MINI_BATCH_SIZE_TABULARDATASET = 1024 * 1024
ALLOWED_INPUT_TYPES = (DatasetConsumptionConfig, PipelineOutputFileDataset)

module_logger = logging.getLogger(__name__)


class ParallelRunStep(PythonScriptStep):
    r"""Add a step to run a Batch Inference job in a Pipeline.

    :param name: Name of the step, should follow regex pattern '^[a-z]([-a-z0-9]*[a-z0-9])?$',
        length of name should be 3-32 characters.
    :type name: str
    :param parallel_run_config: An ParallelRunConfig object used to determine required run properties.
    :type parallel_run_config: azureml.contrib.pipeline.steps.ParallelRunConfig
    :param inputs: List of input datasets.
    :type inputs: list[azureml.data.dataset_consumption_config.DatasetConsumptionConfig]
    :param output: Output port binding, may be used by later pipeline steps.
    :type output: azureml.pipeline.core.builder.PipelineData, azureml.pipeline.core.graph.OutputPortBinding
    :param models: A list of zero or more model objects.
    :type models: list[azureml.core.model.Model]
    :param arguments: List of command-line arguments to pass to the Python entry_script.
    :type arguments: list[str]
    :param allow_reuse: Whether the step should reuse previous results when run with the same settings/inputs.
        If this is false, a new run will always be generated for this step during pipeline execution.
    :type allow_reuse: bool
    :param tags: Dictionary of key value tags for step.
    :type tags: dict[str, str]
    :param properties: Dictionary of key value properties for step.
    :type properties: dict[str, str]
    """

    def __init__(
        self,
        name,
        parallel_run_config,
        inputs,
        output,
        models=None,
        arguments=None,
        allow_reuse=True,
        tags=None,
        properties=None,
    ):
        r"""Add a step to run a Batch Inference job in a Pipeline.

        :param name: Name of the step, should follow regex pattern '^[a-z]([-a-z0-9]*[a-z0-9])?$',
            length of name should be 3-32 characters.
        :type name: str
        :param parallel_run_config: An ParallelRunConfig object used to determine required run properties.
        :type parallel_run_config: azureml.contrib.pipeline.steps.ParallelRunConfig
        :param inputs: List of input datasets.
        :type inputs: list[azureml.data.dataset_consumption_config.DatasetConsumptionConfig]
        :param output: Output port binding, may be used by later pipeline steps.
        :type output: azureml.pipeline.core.builder.PipelineData, azureml.pipeline.core.graph.OutputPortBinding
        :param models: A list of zero or more model objects.
        :type models: list[azureml.core.model.Model]
        :param arguments: List of command-line arguments to pass to the Python entry_script.
        :type arguments: list[str]
        :param allow_reuse: Whether the step should reuse previous results when run with the same settings/inputs.
            If this is false, a new run will always be generated for this step during pipeline execution.
        :type allow_reuse: bool
        :param tags: Dictionary of key value tags for step.
        :type tags: dict[str, str]
        :param properties: Dictionary of key value properties for step.
        :type properties: dict[str, str]
        """
        self._name = name
        self._parallel_run_config = parallel_run_config
        self._inputs = inputs
        self._output = output
        self._arguments = arguments
        self._models = models
        self._node_count = self._parallel_run_config.node_count
        self._process_count_per_node = self._parallel_run_config.process_count_per_node
        self._compute_target = self._parallel_run_config.compute_target
        self._tags = tags
        self._properties = properties
        self._pystep_inputs = []

        self._validate()
        self._gen_input_data_ref_if_needed()

        pipeline_runconfig_params = self._get_pipeline_runconfig_params()
        prun_runconfig = self._generate_runconfig()
        prun_main_file_args = self._generate_main_file_args()

        super(ParallelRunStep, self).__init__(
            name=self._name,
            source_directory=self._parallel_run_config.source_directory,
            script_name=self._parallel_run_config.entry_script,
            runconfig=prun_runconfig,
            runconfig_pipeline_params=pipeline_runconfig_params,
            arguments=prun_main_file_args,
            compute_target=self._compute_target,
            inputs=self._pystep_inputs,
            outputs=[self._output],
            allow_reuse=allow_reuse,
        )

    def _validate(self):
        """Validate input params to init parallel run step class."""
        nameLength = len(self._name)
        if nameLength < 3 or nameLength > 32:
            raise Exception("Step name must have 3-32 characters")

        pattern = re.compile("^[a-z]([-a-z0-9]*[a-z0-9])?$")
        if not pattern.match(self._name):
            raise Exception("Step name must follow regex rule ^[a-z]([-a-z0-9]*[a-z0-9])?$")

        if not isinstance(self._parallel_run_config, ParallelRunConfig):
            raise Exception("Param parallel_run_config must be a azureml.core.model.ParallelRunConfig")

        self._validate_source_directory()
        self._validate_entry_script()

        assert (
            isinstance(self._inputs, list) and len(self._inputs) > 0
        ), "The parameter 'inputs' must be a list and have at least one element."

        input_type = type(self._inputs[0])
        if input_type not in ALLOWED_INPUT_TYPES:
            raise Exception("Step input must be of any type: {}, found {}".format(ALLOWED_INPUT_TYPES, input_type))

        if isinstance(self._inputs[0], DatasetConsumptionConfig):
            input_ds_type = None
            for input in self._inputs:
                if not isinstance(input, DatasetConsumptionConfig):
                    raise Exception("All inputs of step must be same type")
                if input_ds_type is None:
                    input_ds_type = type(input.dataset)
                else:
                    if not isinstance(input.dataset, input_ds_type):
                        raise Exception("All inputs of step must be same Dataset type")
        else:
            for input in self._inputs:
                if not isinstance(input, input_type):
                    raise Exception("All inputs of step must be same type")

        if self._parallel_run_config.mini_batch_size is None:
            if isinstance(self._inputs[0], PipelineOutputFileDataset) or isinstance(
                self._inputs[0].dataset, FileDataset
            ):
                self._parallel_run_config.mini_batch_size = DEFAULT_MINI_BATCH_SIZE_FILEDATASET
            elif isinstance(self._inputs[0].dataset, TabularDataset):
                self._parallel_run_config.mini_batch_size = DEFAULT_MINI_BATCH_SIZE_TABULARDATASET

    def _validate_source_directory(self):
        """Validate the source_directory param."""
        source_dir = self._parallel_run_config.source_directory
        if source_dir and source_dir != "":
            if not os.path.exists(source_dir):
                raise ValueError("The value '{0}' sepcified in source_directory doesn't exist.".format(source_dir))
            if not os.path.isdir(source_dir):
                raise ValueError(
                    "The value '{0}' sepcified in source_directory is not a directory.".format(source_dir)
                )

            full_path = os.path.abspath(source_dir)
            if full_path not in sys.path:
                sys.path.insert(0, full_path)

    def _validate_entry_script(self):
        """Validate the entry script."""
        source_dir = self._parallel_run_config.source_directory
        entry_script = self._parallel_run_config.entry_script

        # In validation of ParallelRunConfig, verify if the entry_script is required.
        # Here we don't verify again.
        if entry_script and entry_script != "":
            if source_dir and source_dir != "":
                # entry script must be in this directory
                full_path = os.path.join(source_dir, entry_script)
                if not os.path.exists(full_path):
                    raise ValueError("The value '{0}' sepcified in entry_script doesn't exist.".format(entry_script))
                if not os.path.isfile(full_path):
                    raise ValueError("The value '{0}' sepcified in entry_script is not a file.".format(entry_script))

    def _gen_input_data_ref_if_needed(self):
        """Generate data reference if input is file dataset type."""
        first_input = self._inputs[0]
        if isinstance(first_input, DatasetConsumptionConfig) and isinstance(first_input.dataset, FileDataset):
            # check for characters which can be used in glob syntax: ^ \ $ | ? * ( ) [ ] { }
            pattern = re.compile(r"[\^\\\$\|\?\*\+\(\)\[\]\{\}]")
            for index, input in enumerate(self._inputs):
                datastores = self._get_datastores_of_dataset(input.dataset)
                # if workspace is available at dataset level then use that instead of constructing it
                # from datastore. Even though one dataset can refer to multiple datastore, all referenced
                # datastore must be from same workspace.
                ds_ws = None
                if input.dataset._registration is not None:
                    ds_ws = input.dataset._registration.workspace
                if datastores is not None:
                    for ds in datastores:
                        if not ds_ws:
                            ds_ws = Workspace(
                                subscription_id=ds["subscription"],
                                resource_group=ds["resourceGroup"],
                                workspace_name=ds["workspaceName"],
                            )

                        reg_ds = Datastore(ds_ws, name=ds["datastoreName"])

                        if not isinstance(reg_ds, AzureBlobDatastore):
                            raise Exception(
                                "Only FileDataset built on "
                                "azureml.data.azure_storage_datastore.AzureBlobDatastore "
                                "are supported"
                            )

                        if pattern.search(ds["path"]):
                            raise Exception(
                                "Can not support FileDataset which contains "
                                'wild cards or glob syntax in path "{}"'.format(ds["path"])
                            )

                        mode = "mount" if reg_ds.account_key else "download"
                        if mode == "download":
                            module_logger.info(
                                (
                                    "An account key was not provided to the datastore, "
                                    "defaulting to download for {}"
                                ).format(input.name)
                            )
                        input_df = DataReference(
                            datastore=reg_ds,
                            data_reference_name="{0}_{1}".format(input.name, index),
                            path_on_datastore=ds["path"],
                            mode=mode,
                        )
                        self._pystep_inputs.append(input_df)
        elif isinstance(first_input, PipelineOutputFileDataset):
            for index, input in enumerate(self._inputs):
                self._pystep_inputs.append(input._pipeline_data)

    def _get_datastores_of_dataset(self, input):
        """Get data stores from file dataset."""
        steps = input._dataflow._get_steps()
        if steps[0].step_type == "Microsoft.DPrep.GetDatastoreFilesBlock":
            return steps[0].arguments["datastores"]
        else:
            return None

    def _get_pipeline_runconfig_params(self):
        """
        Generate pipeline parameters for runconfig.

        :return: runconfig pipeline parameters
        :rtype: dict
        """
        prun_runconfig_pipeline_params = {}
        nodecount_param = PipelineParameter(name="aml_node_count", default_value=self._node_count)
        prun_runconfig_pipeline_params["NodeCount"] = nodecount_param
        return prun_runconfig_pipeline_params

    def _generate_runconfig(self):
        """
        Generate runconfig for parallel run step.

        :return: runConfig
        :rtype: RunConfig
        """
        run_config = RunConfiguration()
        run_config.node_count = self._node_count
        run_config.target = self._compute_target
        run_config.framework = "Python"
        # For AmlCompute we need to enable Docker.run_config.environment.docker.enabled = True
        run_config.environment = self._parallel_run_config.environment
        run_config.environment.docker.enabled = True

        if run_config.environment.python.conda_dependencies is None:
            run_config.environment.python.conda_dependencies = CondaDependencies.create()

        run_config.environment.python.conda_dependencies.add_pip_package("azure-storage-queue~=2.1")
        run_config.environment.python.conda_dependencies.add_pip_package("azure-storage-common~=2.1")
        run_config.environment.python.conda_dependencies.add_pip_package("azureml-core~=1.0")
        run_config.environment.python.conda_dependencies.add_pip_package("azureml-telemetry~=1.0")
        run_config.environment.python.conda_dependencies.add_pip_package("filelock~=3.0")
        run_config.environment.python.conda_dependencies.add_pip_package("pandas")
        run_config.environment.python.conda_dependencies.add_pip_package("pyarrow>=0.11.0,<0.15")
        run_config.environment.python.conda_dependencies.add_pip_package("azureml-dataprep[fuse,pandas]~=1.1")
        run_config.environment.python.conda_dependencies.add_pip_package("azureml-dataprep-native")
        run_config.environment.python.conda_dependencies.add_channel("anaconda")
        run_config.environment.python.conda_dependencies.add_conda_package("psutil")

        return run_config

    def _generate_main_file_args(self):
        """
        Generate main args for entry script.

        :return: The generated main args for entry script.
        :rtype: array
        """
        main_args = [
            "--scoring_module_name", self._parallel_run_config.entry_script,
            "--output", self._output,
            "--input_format", self._parallel_run_config.input_format,
            "--mini_batch_size", int(self._parallel_run_config.mini_batch_size),
            "--error_threshold", float(self._parallel_run_config.error_threshold),
            "--output_action", self._parallel_run_config.output_action,
            "--logging_level", self._parallel_run_config.logging_level,
            "--run_invocation_timeout", self._parallel_run_config.run_invocation_timeout,
        ]

        if self._process_count_per_node is not None:
            self._process_count_per_node = PipelineParameter(name="aml_process_count_per_node",
                                                             default_value=self._process_count_per_node)
            main_args.extend(["--process_count_per_node", self._process_count_per_node])

        main_args.extend(self._arguments)

        first_input = self._inputs[0]
        if isinstance(first_input, DatasetConsumptionConfig) and isinstance(first_input.dataset, TabularDataset):
            for index, input in enumerate(self._inputs):
                ws = None
                if input.dataset._registration is not None:
                    ws = input.dataset._registration.workspace
                else:
                    datastore = input.dataset._dataflow._get_steps()[0].arguments.to_pod()["datastores"][0]
                    ws = Workspace(datastore["subscription"], datastore["resourceGroup"], datastore["workspaceName"])
                dsid = input.dataset._ensure_saved(ws)
                main_args += ["--input_ds_{0}".format(index), dsid]
        else:
            for index, input in enumerate(self._pystep_inputs):
                main_args += ["--input{0}".format(index), input]

        return main_args

    def _generate_batch_inference_metadata(self):
        """
        Generate batch inference metadata which will be register to MMS service.

        :return: The generated batch inference metadata.
        :rtype: str
        """
        model_ids = []
        if self._models and isinstance(self._models, list):
            for model in self._models:
                model_ids.append(model.id)

        batch_inferencing_metadata = {
            "Name": self._name,
            "ComputeName": self._compute_target.name,
            "AppInsightsEnabled": False,
            "EventHubEnabled": False,
            "StorageEnabled": False,
            "EntryScript": self._parallel_run_config.entry_script,
            "NodeCount": self._node_count,
            "InputFormat": self._parallel_run_config.input_format,
            "MiniBatchSize": self._parallel_run_config.mini_batch_size,
            "ErrorThreshold": self._parallel_run_config.error_threshold,
            "OutputAction": self._parallel_run_config.output_action,
            "ModelIds": json.dumps(model_ids),
            "Tags": json.dumps(self._tags),
            "Properties": json.dumps(self._properties),
            "EnvironmentName": self._parallel_run_config.environment.name,
            "EnvironmentVersion": self._parallel_run_config.environment.version,
        }

        if self._process_count_per_node:
            batch_inferencing_metadata['ProcessCountPerNode'] = self._process_count_per_node.default_value

        return json.dumps(batch_inferencing_metadata)

    def create_node(self, graph, default_datastore, context):
        """
        Create a node for PythonScriptStep and add it to the specified graph.

        This method is not intended to be used directly. When a pipeline is instantiated with this step,
        Azure ML automatically passes the parameters required through this method so that step can be added to a
        pipeline graph that represents the workflow.

        :param graph: graph object
        :type graph: azureml.pipeline.core.graph.Graph
        :param default_datastore: default datastore
        :type default_datastore: azureml.core.AbstractAzureStorageDatastore, azureml.core.AzureDataLakeDatastore
        :param context: context
        :type context: _GraphContext

        :return: The created node.
        :rtype: azureml.pipeline.core.graph.Node
        """
        node = super(ParallelRunStep, self).create_node(graph, default_datastore, context)
        node.get_param("BatchInferencingMetaData").set_value(self._generate_batch_inference_metadata())
        node.get_param("Script").set_value(DEFAULT_BATCH_SCORE_MAIN_FILE_NAME)
        return node

    def create_module_def(
        self,
        execution_type,
        input_bindings,
        output_bindings,
        param_defs=None,
        create_sequencing_ports=True,
        allow_reuse=True,
        version=None,
    ):
        """
        Create the module definition object that describes the step.

        This method is not intended to be used directly.

        :param execution_type: The execution type of the module.
        :type execution_type: str
        :param input_bindings: The step input bindings.
        :type input_bindings: list
        :param output_bindings: The step output bindings.
        :type output_bindings: list
        :param param_defs: The step param definitions.
        :type param_defs: list
        :param create_sequencing_ports: If true sequencing ports will be created for the module.
        :type create_sequencing_ports: bool
        :param allow_reuse: If true the module will be available to be reused in future Pipelines.
        :type allow_reuse: bool
        :param version: The version of the module.
        :type version: str

        :return: The module def object.
        :rtype: azureml.pipeline.core.graph.ModuleDef
        """
        if param_defs is None:
            param_defs = []
        else:
            param_defs = list(param_defs)

        batch_inference_metadata_param_def = ParamDef(
            name="BatchInferencingMetaData",
            set_env_var=False,
            is_metadata_param=True,
            default_value="None",
            env_var_override=False,
        )
        param_defs.append(batch_inference_metadata_param_def)

        return super(ParallelRunStep, self).create_module_def(
            execution_type,
            input_bindings,
            output_bindings,
            param_defs,
            create_sequencing_ports,
            allow_reuse,
            version,
            "BatchInferencing",
        )
