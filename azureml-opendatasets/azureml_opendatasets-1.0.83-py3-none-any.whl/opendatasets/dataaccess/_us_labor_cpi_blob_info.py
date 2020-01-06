# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of US labor cpi data."""

from ._us_labor_base_blob_info import UsLaborBaseBlobInfo


class UsLaborCPIBlobInfo(UsLaborBaseBlobInfo):
    """Blob info of US labor cpi Data."""

    def __init__(self):
        """Initialize Blob Info."""
        self.registry_id = 'us_labor_cpi'
        self.blob_relative_path = "cpi/"
