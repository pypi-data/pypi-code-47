class ExportError(Exception):
    pass


class LocalExportError(ExportError):
    pass


class RetryExportError(ExportError):
    pass


class TotalExportError(ExportError):
    pass
