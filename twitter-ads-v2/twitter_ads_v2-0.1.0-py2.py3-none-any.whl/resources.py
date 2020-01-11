"""List of the supported API endpoints' resource path."""


RESOURCE_TABLE = {
    'accounts': {
        'endpoint_types': ['all', 'load'],
        'RESOURCE': 'accounts/{id}',
        'RESOURCE_COLLECTION': 'accounts'
    },
    'authenticated_user_access': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'accounts/{account_id}/authenticated_user_access'
    },
    'bidding_rules': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'bidding_rules'
    },
    'campaigns': {
        'endpoint_types': ['all', 'load', 'create', 'update', 'delete', 'batch'],
        'BATCH': 'batch/accounts/{account_id}/campaigns',
        'RESOURCE': 'accounts/{account_id}/campaigns/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/campaigns'
    },
    'content_categories': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'content_categories'
    },
    'funding_instruments': {
        'endpoint_types': ['all', 'load', 'create', 'update', 'delete'],
        'RESOURCE': 'accounts/{account_id}/funding_instruments/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/funding_instruments'
    },
    'iab_categories': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'iab_categories'
    },
    'line_items': {
        'endpoint_types': ['all', 'load', 'create', 'update', 'delete', 'batch'],
        'BATCH': 'batch/accounts/{account_id}/line_items',
        'RESOURCE': 'accounts/{account_id}/line_items/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/line_items'
    },
    'line_item_placements': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'line_items/placements'
    },
    'line_item_apps': {
        'endpoint_types': ['all', 'load', 'create', 'delete'],
        'RESOURCE': 'accounts/{account_id}/line_item_apps/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/line_item_apps'
    },
    'media_creatives': {
        'endpoint_types': ['all', 'load', 'create', 'delete'],
        'RESOURCE': 'accounts/{account_id}/media_creatives/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/media_creatives'
    },
    'promoted_accounts': {
        'endpoint_types': ['all', 'load', 'create', 'delete'],
        'RESOURCE': 'accounts/{account_id}/promoted_accounts/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/promoted_accounts'
    },
    'promoted_tweets': {
        'endpoint_types': ['all', 'load', 'create', 'delete'],
        'RESOURCE': 'accounts/{account_id}/promoted_tweets/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/promoted_tweets'
    },
    'promotable_users': {
        'endpoint_types': ['all', 'load'],
        'RESOURCE': 'accounts/{account_id}/promotable_users/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/promotable_users'
    },
    'scheduled_promoted_tweets': {
        'endpoint_types': ['all', 'load', 'create', 'delete'],
        'RESOURCE': 'accounts/{account_id}/scheduled_promoted_tweets/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/scheduled_promoted_tweets'
    },
    'targeting_criteria': {
        'endpoint_types': ['all', 'load', 'create', 'delete'],
        'RESOURCE': 'accounts/{account_id}/targeting_criteria/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/targeting_criteria'
    },
    'targeting_suggestions': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'accounts/{account_id}/targeting_suggestions'
    },
    'targeting_criteria_app_store_categories': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'targeting_criteria/app_store_categories'
    },
    'targeting_criteria_behavior_taxonomies': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'targeting_criteria/behavior_taxonomies'
    },
    'targeting_criteria_behaviors': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'targeting_criteria/behaviors'
    },
    'targeting_criteria_conversations': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'targeting_criteria/conversations'
    },
    'targeting_criteria_devices': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'targeting_criteria/devices'
    },
    'targeting_criteria_events': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'targeting_criteria/events'
    },
    'targeting_criteria_interests': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'targeting_criteria/interests'
    },
    'targeting_criteria_languages': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'targeting_criteria/languages'
    },
    'targeting_criteria_locations': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'targeting_criteria/locations'
    },
    'targeting_criteria_network_operators': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'targeting_criteria/network_operators'
    },
    'targeting_criteria_platform_versions': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'targeting_criteria/platform_versions'
    },
    'targeting_criteria_platforms': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'targeting_criteria/platforms'
    },
    'targeting_criteria_tv_markets': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'targeting_criteria/tv_markets'
    },
    'targeting_criteria_tv_shows': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'targeting_criteria/tv_shows'
    },
    'reach_estimate': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'accounts/{account_id}/reach_estimate'
    },
    'tax_settings': {
        'endpoint_types': ['all', 'update'],
        'RESOURCE': 'accounts/{account_id}/tax_settings',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/tax_settings'
    },
    'user_settings': {
        'endpoint_types': ['load', 'update'],
        'RESOURCE': 'accounts/{account_id}/user_settings/{id}'
    },
    'account_media': {
        'endpoint_types': ['all', 'load', 'delete'],
        'RESOURCE': 'accounts/{account_id}/account_media/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/account_media'
    },
    'scheduled_tweets': {
        'endpoint_types': ['all', 'load', 'create', 'update', 'delete'],
        'RESOURCE': 'accounts/{account_id}/scheduled_tweets/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/scheduled_tweets'
    },
    'draft_tweets': {
        'endpoint_types': ['all', 'load', 'create', 'update', 'delete'],
        'RESOURCE': 'accounts/{account_id}/draft_tweets/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/draft_tweets'
    },
    'draft_tweets_preview': {
        'endpoint_types': ['create'],
        'RESOURCE': 'accounts/{account_id}/draft_tweets/preview/{id}',
    },
    'tweets': {
        'endpoint_types': ['all', 'create'],
        'RESOURCE_GET': 'accounts/{account_id}/tweets',
        'RESOURCE_POST': 'accounts/{account_id}/tweet',
    },
    'tweet_previews': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'accounts/{account_id}/tweet_previews'
    },
    'image_app_download_cards': {
        'endpoint_types': ['all', 'load', 'create', 'update', 'delete'],
        'RESOURCE': 'accounts/{account_id}/cards/image_app_download/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/cards/image_app_download'
    },
    'image_conversation_cards': {
        'endpoint_types': ['all', 'load', 'create', 'update', 'delete'],
        'RESOURCE': 'accounts/{account_id}/cards/image_conversation/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/cards/image_conversation'
    },
    'video_app_download_cards': {
        'endpoint_types': ['all', 'load', 'create', 'update', 'delete'],
        'RESOURCE': 'accounts/{account_id}/cards/video_app_download/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/cards/video_app_download'
    },
    'video_conversation_cards': {
        'endpoint_types': ['all', 'load', 'create', 'update', 'delete'],
        'RESOURCE': 'accounts/{account_id}/cards/video_conversation/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/cards/video_conversation'
    },
    'video_website_cards': {
        'endpoint_types': ['all', 'load', 'create', 'update', 'delete'],
        'RESOURCE': 'accounts/{account_id}/cards/video_website/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/cards/video_website'
    },
    'website_cards': {
        'endpoint_types': ['all', 'load', 'create', 'update', 'delete'],
        'RESOURCE': 'accounts/{account_id}/cards/website/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/cards/website'
    },
    'image_direct_message_cards': {
        'endpoint_types': ['all', 'load', 'create', 'update', 'delete'],
        'RESOURCE': 'accounts/{account_id}/cards/image_direct_message/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/cards/image_direct_message'
    },
    'video_direct_message_cards': {
        'endpoint_types': ['all', 'load', 'create', 'update', 'delete'],
        'RESOURCE': 'accounts/{account_id}/cards/video_direct_message/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/cards/video_direct_message'
    },
    'poll_cards': {
        'endpoint_types': ['all', 'load', 'create', 'delete'],
        'RESOURCE': 'accounts/{account_id}/cards/poll/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/cards/poll'
    },
    'cards_fetch': {
        'endpoint_types': ['all', 'load'],
        'RESOURCE': 'accounts/{account_id}/cards/all/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/cards/all'
    },
    'media_library': {
        'endpoint_types': ['all', 'load', 'create', 'update', 'delete'],
        'RESOURCE': 'accounts/{account_id}/media_library/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/media_library'
    },
    'preroll_call_to_actions': {
        'endpoint_types': ['all', 'load', 'create', 'update', 'delete'],
        'RESOURCE': 'accounts/{account_id}/preroll_call_to_actions/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/preroll_call_to_actions'
    },
    'active_entities': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'stats/accounts/{account_id}/active_entities'
    },
    'analytics_sync_stats': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'stats/accounts/{account_id}'
    },
    'analytics_async_jobs': {
        'endpoint_types': ['all', 'delete'],
        'RESOURCE': 'stats/jobs/accounts/{account_id}/{id}',
        'RESOURCE_COLLECTION': 'stats/jobs/accounts/{account_id}'
    },
    'analytics_async_create_job': {
        'endpoint_types': ['create'],
        'RESOURCE_COLLECTION': 'stats/jobs/accounts/{account_id}'
    },
    'reach_frequency_campaigns': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'stats/accounts/{account_id}/reach/campaigns'
    },
    'reach_frequency_funding_instruments': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'stats/accounts/{account_id}/reach/funding_instruments'
    },
    'tailored_audiences': {
        'endpoint_types': ['all', 'load', 'create', 'delete'],
        'RESOURCE': 'accounts/{account_id}/tailored_audiences/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/tailored_audiences'
    },
    'tailored_audiences_users': {
        'endpoint_types': ['create'],
        'RESOURCE': 'accounts/{account_id}/tailored_audiences/{id}/users'
    },
    'tailored_audience_permissions': {
        'endpoint_types': ['all', 'create', 'delete'],
        'RESOURCE': ('accounts/{account_id}/tailored_audiences/{tailored_audience_id}/'
                     'permissions/{tailored_audience_permission_id}'),
        'RESOURCE_COLLECTION': ('accounts/{account_id}/tailored_audiences/{tailored_audience_id}/'
                                'permissions')
    },
    'insights': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'insights/accounts/{account_id}'
    },
    'insights_available_audiences': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'insights/accounts/{account_id}/available_audiences'
    },
    'keyword_insights': {
        'endpoint_types': ['all'],
        'RESOURCE_COLLECTION': 'insights/keywords/search'
    },
}
