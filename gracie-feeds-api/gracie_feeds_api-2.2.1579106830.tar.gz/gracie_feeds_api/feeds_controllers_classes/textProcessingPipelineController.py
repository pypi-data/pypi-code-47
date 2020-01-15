from gracie_feeds_api import GracieBaseAPI


class textProcessingPipelineController(GracieBaseAPI):
    """Text Processing Pipeline Controller"""

    _controller_name = "textProcessingPipelineController"

    def add(self, name, pipeline, **kwargs):
        """Create new text processing pipeline for authenticated user.

        Args:
            description: (string): description
            name: (string): name
            pipeline: (string): pipeline

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'description': {'name': 'description', 'required': False, 'in': 'query'}, 'name': {'name': 'name', 'required': True, 'in': 'query'}, 'pipeline': {'name': 'pipeline', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/textProcessingPipeline/add'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def default(self):
        """Returns default text processing pipeline."""

        all_api_parameters = {}
        parameters_names_map = {}
        api = '/textProcessingPipeline/default'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def edit(self, name, pipeline, textProcessingPipelineId, **kwargs):
        """Edit existing text processing pipeline by ID.

        Args:
            description: (string): description
            name: (string): name
            pipeline: (string): pipeline
            textProcessingPipelineId: (string): textProcessingPipelineId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'description': {'name': 'description', 'required': False, 'in': 'query'}, 'name': {'name': 'name', 'required': True, 'in': 'query'}, 'pipeline': {'name': 'pipeline', 'required': True, 'in': 'query'}, 'textProcessingPipelineId': {'name': 'textProcessingPipelineId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/textProcessingPipeline/edit'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def list(self, **kwargs):
        """Return the list of text processing pipeline for authenticated user.

        Args:
            withPipeline: (boolean): withPipeline

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'withPipeline': {'name': 'withPipeline', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/textProcessingPipeline/list'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def remove(self, textProcessingPipelineId):
        """Remove existing text processing pipeline for authenticated user.

        Args:
            textProcessingPipelineId: (string): textProcessingPipelineId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'textProcessingPipelineId': {'name': 'textProcessingPipelineId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/textProcessingPipeline/remove'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def retrieve(self, textProcessingPipelineId):
        """Return the text processing pipeline with specified ID.

        Args:
            textProcessingPipelineId: (string): textProcessingPipelineId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'textProcessingPipelineId': {'name': 'textProcessingPipelineId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/textProcessingPipeline/retrieve'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
