from .base import MetadataAPI


class MarketplaceAPI(MetadataAPI):
    method_type = 'GET'
    resource = 'marketplace'
    required_path_params = ['marketplace_id']
    allowed_query_params = ['filter']


class GetListingStructurePolicies(MarketplaceAPI):
    url_postfix = 'get_listing_structure_policies'


class GetItemConditionPolicies(MarketplaceAPI):
    url_postfix = 'get_item_condition_policies'


class GetAutomotivePartsCompatibilityPolicies(MarketplaceAPI):
    url_postfix = 'get_automotive_parts_compatibility_policies'
