# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of US labor ppi industry data."""

from ._us_labor_base_blob_info import UsLaborBaseBlobInfo


class UsLaborPPIIndustryBlobInfo(UsLaborBaseBlobInfo):
    """Blob info of US labor ppi industry Data."""

    def __init__(self):
        """Initialize Blob Info."""
        self.registry_id = 'us_labor_ppi_industry'
        self.blob_relative_path = "ppi_industry/"
