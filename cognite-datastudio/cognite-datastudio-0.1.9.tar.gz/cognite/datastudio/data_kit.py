import json
from typing import List, Optional

from cognite.client.data_classes.assets import AssetList
from cognite.client.data_classes.files import FileMetadataList
from cognite.client.data_classes.time_series import TimeSeriesList


class DataKit:
    assets: Optional[List[AssetList]] = None
    time_series: Optional[List[TimeSeriesList]] = None
    files: Optional[List[FileMetadataList]] = None
    name: str = "Data kit"

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        obj = {"name": self.name}
        if self.assets:
            obj["assets"] = "%d assets" % len(self.assets)
        if self.time_series:
            obj["time_series"] = "%d time series" % len(self.time_series)
        if self.files:
            obj["files"] = "%d files" % len(self.files)
        return "<DataKit>: " + json.dumps(obj)
