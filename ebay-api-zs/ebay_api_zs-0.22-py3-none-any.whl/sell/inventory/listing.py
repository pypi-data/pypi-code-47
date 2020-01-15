from .base import InventoryAPI


class BulkMigrateListing(InventoryAPI):
    resource = ''
    method_type = 'POST'
    url_postfix = 'bulk_migrate_listing'
