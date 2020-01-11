import json

from urllib.parse import urlparse
from twitter_ads_v2.http import Request
from twitter_ads_v2.utils import CustomDecorators
from twitter_ads_v2.resources import RESOURCE_TABLE


class Base(object):

    _METHOD_MAP = {
        'all': 'GET',
        'load': 'GET',
        'create': 'POST',
        'update': 'PUT',
        'delete': 'DELETE',
        'batch': 'POST'
    }

    @CustomDecorators.resource_controller('accounts')
    @CustomDecorators.flatten_params
    def accounts(self, endpoint_type, **kwargs):
        """Accounts
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/accounts

        Supported `endpoint_type`:
            `all`, `load`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
            id (:obj:`str`, optional): An Ads Account ID to retrieve.
            Required when `endpoint_type` is `load`.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('authenticated_user_access')
    @CustomDecorators.flatten_params
    def authenticated_user_access(self, endpoint_type, **kwargs):
        """Authenticated User Access
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/authenticated-user-access

        Supported `endpoint_type`:
            `all`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('bidding_rules')
    @CustomDecorators.flatten_params
    def bidding_rules(self, endpoint_type, **kwargs):
        """Bidding Rules
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/bidding-rules

        Supported `endpoint_type`:
            `all`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('campaigns')
    @CustomDecorators.flatten_params
    def campaigns(self, endpoint_type, *, data=None, **kwargs):
        """Campaigns
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/campaigns

        Supported `endpoint_type`:
            `all`, `load`, `create`, `batch`, `update`, `delete`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
            data (:obj:`list`, optional): A JSON POST body data to send.
            Required when `endpoint_type` is `batch`.
        """
        return Request(self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'),
                       headers=kwargs.get('_headers', {}), body=data, params=kwargs).perform()

    @CustomDecorators.resource_controller('content_categories')
    @CustomDecorators.flatten_params
    def content_categories(self, endpoint_type, **kwargs):
        """Content Categories
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/content-categories

        Supported `endpoint_type`:
            `all`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('funding_instruments')
    @CustomDecorators.flatten_params
    def funding_instruments(self, endpoint_type, **kwargs):
        """Funding Instruments
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/funding-instruments

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('iab_categories')
    @CustomDecorators.flatten_params
    def iab_categories(self, endpoint_type, **kwargs):
        """IAB Categories
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/iab-categories

        Supported `endpoint_type`:
            `all`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('line_items')
    @CustomDecorators.flatten_params
    def line_items(self, endpoint_type, *, data=None, **kwargs):
        """Line Items
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/line-items

        Supported `endpoint_type`:
            `all`, `load`, `create`, `batch`, `update`, `delete`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
            data (:obj:`list`, optional): A JSON POST body data to send.
            Required when `endpoint_type` is `batch`.
        """
        return Request(self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'),
                       headers=kwargs.get('_headers', {}), body=data, params=kwargs).perform()

    @CustomDecorators.resource_controller('line_item_apps')
    @CustomDecorators.flatten_params
    def line_item_apps(self, endpoint_type, **kwargs):
        """Line Item Apps
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/line-item-apps

        Supported `endpoint_type`:
            `all`, `load`, `create`, `delete`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('line_item_placements')
    @CustomDecorators.flatten_params
    def line_item_placements(self, endpoint_type, **kwargs):
        """Line Item Placements
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/line-item-placements

        Supported `endpoint_type`:
            `all`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('media_creatives')
    @CustomDecorators.flatten_params
    def media_creatives(self, endpoint_type, **kwargs):
        """Media Creatives
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/media-creatives

        Supported `endpoint_type`:
            `all`, `load`, `create`, `delete`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('promoted_accounts')
    @CustomDecorators.flatten_params
    def promoted_accounts(self, endpoint_type, **kwargs):
        """Promoted Accounts
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/promoted-accounts

        Supported `endpoint_type`:
            `all`, `load`, `create`, `delete`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('promoted_tweets')
    @CustomDecorators.flatten_params
    def promoted_tweets(self, endpoint_type, **kwargs):
        """Promoted Tweets
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/promoted-tweets

        Supported `endpoint_type`:
            `all`, `load`, `create`, `delete`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('promotable_users')
    @CustomDecorators.flatten_params
    def promotable_users(self, endpoint_type, **kwargs):
        """Promotable Users
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/promotable-users

        Supported `endpoint_type`:
            `all`, `load`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('scheduled_promoted_tweets')
    @CustomDecorators.flatten_params
    def scheduled_promoted_tweets(self, endpoint_type, **kwargs):
        """Scheduled Promoted Tweets
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/scheduled-promoted-tweets

        Supported `endpoint_type`:
            `all`, `load`, `create`, `delete`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('targeting_criteria')
    @CustomDecorators.flatten_params
    def targeting_criteria(self, endpoint_type, **kwargs):
        """Targeting Criteria
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-criteria

        Supported `endpoint_type`:
            `all`, `load`, `create`, `delete`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('targeting_suggestions')
    @CustomDecorators.flatten_params
    def targeting_suggestions(self, endpoint_type, **kwargs):
        """Targeting Suggestions
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-suggestions

        Supported `endpoint_type`:
            `all`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller(
        'targeting_criteria_app_store_categories', default_operation='all')
    @CustomDecorators.flatten_params
    def targeting_criteria_app_store_categories(self, endpoint_type, **kwargs):

        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller(
        'targeting_criteria_behavior_taxonomies', default_operation='all')
    @CustomDecorators.flatten_params
    def targeting_criteria_behavior_taxonomies(self, endpoint_type, **kwargs):

        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('targeting_criteria_behaviors', default_operation='all')
    @CustomDecorators.flatten_params
    def targeting_criteria_behaviors(self, endpoint_type, **kwargs):

        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller(
        'targeting_criteria_conversations', default_operation='all')
    @CustomDecorators.flatten_params
    def targeting_criteria_conversations(self, endpoint_type, **kwargs):

        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('targeting_criteria_devices', default_operation='all')
    @CustomDecorators.flatten_params
    def targeting_criteria_devices(self, endpoint_type, **kwargs):

        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('targeting_criteria_events', default_operation='all')
    @CustomDecorators.flatten_params
    def targeting_criteria_events(self, endpoint_type, **kwargs):

        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('targeting_criteria_interests', default_operation='all')
    @CustomDecorators.flatten_params
    def targeting_criteria_interests(self, endpoint_type, **kwargs):

        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('targeting_criteria_languages', default_operation='all')
    @CustomDecorators.flatten_params
    def targeting_criteria_languages(self, endpoint_type, **kwargs):

        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('targeting_criteria_locations', default_operation='all')
    @CustomDecorators.flatten_params
    def targeting_criteria_locations(self, endpoint_type, **kwargs):

        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller(
        'targeting_criteria_network_operators', default_operation='all')
    @CustomDecorators.flatten_params
    def targeting_criteria_network_operators(self, endpoint_type, **kwargs):

        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller(
        'targeting_criteria_platform_versions', default_operation='all')
    @CustomDecorators.flatten_params
    def targeting_criteria_platform_versions(self, endpoint_type, **kwargs):

        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('targeting_criteria_platforms', default_operation='all')
    @CustomDecorators.flatten_params
    def targeting_criteria_platforms(self, endpoint_type, **kwargs):

        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('targeting_criteria_tv_markets', default_operation='all')
    @CustomDecorators.flatten_params
    def targeting_criteria_tv_markets(self, endpoint_type, **kwargs):

        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('targeting_criteria_tv_shows', default_operation='all')
    @CustomDecorators.flatten_params
    def targeting_criteria_tv_shows(self, endpoint_type, **kwargs):

        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('reach_estimate', default_operation='all')
    @CustomDecorators.flatten_params
    def reach_estimate(self, endpoint_type, **kwargs):
        """Reach Estimate
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/reach-estimate

        Supported `endpoint_type`:
            `all`

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('tax_settings')
    @CustomDecorators.flatten_params
    def tax_settings(self, endpoint_type, **kwargs):
        """Tax Settings
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/tax-settings

        Supported `endpoint_type`:
            `all`, `update`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('user_settings')
    @CustomDecorators.flatten_params
    def user_settings(self, endpoint_type, **kwargs):
        """User Settings
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/user-settings

        Supported `endpoint_type`:
            `load`, `update`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('account_media')
    @CustomDecorators.flatten_params
    def account_media(self, endpoint_type, **kwargs):
        """Account Media
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/account-media

        Supported `endpoint_type`:
            `all`, `load`, `delete`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('scheduled_tweets')
    @CustomDecorators.flatten_params
    def scheduled_tweets(self, endpoint_type, **kwargs):
        """Scheduled Tweets
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/scheduled-tweets

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('draft_tweets')
    @CustomDecorators.flatten_params
    def draft_tweets(self, endpoint_type, **kwargs):
        """Draft Tweets
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/draft-tweets

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    def draft_tweets_preview(self, endpoint_type='create', *,
                             resource=None, draft_tweet_id):
        """Draft Tweets Preview
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/draft-tweets#post-accounts-account-id-draft-tweets-preview-draft-tweet-id

        Supported `endpoint_type`:
            `create` (default)

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
            draft_tweet_id (:obj:`str`): A Draft Tweet ID to preview.
        """
        base = RESOURCE_TABLE['draft_tweets_preview']['RESOURCE']
        resource = base.format(account_id=self.account_id, id=draft_tweet_id)
        return Request(self, self._METHOD_MAP[endpoint_type], resource, params={}).perform()

    @CustomDecorators.flatten_params
    def tweets(self, endpoint_type, **kwargs):
        """Tweets
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/tweets

        Supported `endpoint_type`:
            `all`, `create`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        if endpoint_type == 'all':
            base = RESOURCE_TABLE['tweets']['RESOURCE_GET']
        else:
            base = RESOURCE_TABLE['tweets']['RESOURCE_POST']
        resource = base.format(account_id=self.account_id)
        return Request(
            self, self._METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @CustomDecorators.resource_controller('tweet_previews', default_operation='all')
    @CustomDecorators.flatten_params
    def tweet_previews(self, endpoint_type, **kwargs):
        """Tweet Previews
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/tweet-previews

        Supported `endpoint_type`:
            `all`

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('image_app_download_cards')
    @CustomDecorators.flatten_params
    def image_app_download_cards(self, endpoint_type, **kwargs):
        """Image App Download Cards
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/image-app-download

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('image_conversation_cards')
    @CustomDecorators.flatten_params
    def image_conversation_cards(self, endpoint_type, **kwargs):
        """Image Conversation Cards
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/image-conversation

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('video_app_download_cards')
    @CustomDecorators.flatten_params
    def video_app_download_cards(self, endpoint_type, **kwargs):
        """Video App Download Cards
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/video-app-download

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('video_conversation_cards')
    @CustomDecorators.flatten_params
    def video_conversation_cards(self, endpoint_type, **kwargs):
        """Video Conversation Cards
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/video-conversation

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('video_website_cards')
    @CustomDecorators.flatten_params
    def video_website_cards(self, endpoint_type, **kwargs):
        """Video Website Cards
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/video-website

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('website_cards')
    @CustomDecorators.flatten_params
    def website_cards(self, endpoint_type, **kwargs):
        """Website Cards
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/website

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('image_direct_message_cards')
    @CustomDecorators.flatten_params
    def image_direct_message_cards(self, endpoint_type, **kwargs):
        """Image Direct Message Cards
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/image-direct-message

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('video_direct_message_cards')
    @CustomDecorators.flatten_params
    def video_direct_message_cards(self, endpoint_type, **kwargs):
        """Video Direct Message Cards
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/video-direct-message

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('poll_cards')
    @CustomDecorators.flatten_params
    def poll_cards(self, endpoint_type, **kwargs):
        """Poll Cards
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/poll

        Supported `endpoint_type`:
            `all`, `load`, `create`, `delete`

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('media_library')
    @CustomDecorators.flatten_params
    def media_library(self, endpoint_type, **kwargs):
        """Media Library
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/media-library

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('cards_fetch')
    @CustomDecorators.flatten_params
    def cards_fetch(self, endpoint_type, **kwargs):
        """Cards Fetch
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/cards-fetch

        Supported `endpoint_type`:
            `all`, `load`
        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('preroll_call_to_actions')
    @CustomDecorators.flatten_params
    def preroll_call_to_actions(self, endpoint_type, **kwargs):
        """Preroll Call To Actions
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/preroll-call-to-actions

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('active_entities', default_operation='all')
    @CustomDecorators.flatten_params
    def active_entities(self, endpoint_type, **kwargs):
        """Active Entities
        https://developer.twitter.com/en/docs/ads/analytics/api-reference/active-entities

        Supported `endpoint_type`:
            `all` (default)

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('analytics_sync_stats', default_operation='all')
    @CustomDecorators.flatten_params
    def analytics_sync_stats(self, endpoint_type, **kwargs):
        """Synchronous Analytics
        https://developer.twitter.com/en/docs/ads/analytics/api-reference/synchronous

        Supported `endpoint_type`:
            `all` (default)

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """

        # TODO: some helper functions here?
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('analytics_async_jobs')
    @CustomDecorators.flatten_params
    def analytics_async_jobs(self, endpoint_type, **kwargs):
        """Asynchronous Analytics
        Retrieve details for some or all asynchronous analytics jobs for the current account.
        https://developer.twitter.com/en/docs/ads/analytics/api-reference/asynchronous#get-stats-jobs-accounts-account-id
        Cancel an asynchronous analytics job for a given ads account.
        https://developer.twitter.com/en/docs/ads/analytics/api-reference/asynchronous#delete-stats-jobs-accounts-account-id-job-id

        Supported `endpoint_type`:
            `all`, `delete`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """

        # TODO: some helper functions here?
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('analytics_async_create_job', default_operation='create')
    @CustomDecorators.flatten_params
    def analytics_async_create_job(self, endpoint_type, **kwargs):
        """Asynchronous Analytics
        Create an asynchronous analytics job for the current account.
        https://developer.twitter.com/en/docs/ads/analytics/api-reference/asynchronous#post-stats-jobs-accounts-account-id

        Supported `endpoint_type`:
            `create` (default)

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """

        # TODO: some helper functions here?
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    def analytics_async_job_data(self, endpoint_type='load', *, url):
        """Returns the results of the specified async job data URL.

        Supported `endpoint_type`:
            `load`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
            url (:obj:`str`): A job data URL to download.
        """
        # TODO: some helper functions here?
        resource = urlparse(url)
        domain = '{0}://{1}'.format(resource.scheme, resource.netloc)
        return Request(
            self,
            self._METHOD_MAP[endpoint_type],
            resource.path,
            domain=domain,
            raw_body=True,
            stream=True).perform()

    @CustomDecorators.resource_controller('reach_frequency_campaigns', default_operation='all')
    @CustomDecorators.flatten_params
    def reach_frequency_campaigns(self, endpoint_type, **kwargs):
        """Reach and Average Frequency (campaigns)
        https://developer.twitter.com/en/docs/ads/analytics/api-reference/reach#get-stats-accounts-account-id-reach-campaigns

        Supported `endpoint_type`:
            `all` (default)

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller(
        'reach_frequency_funding_instruments', default_operation='all')
    @CustomDecorators.flatten_params
    def reach_frequency_funding_instruments(self, endpoint_type, **kwargs):
        """Reach and Average Frequency (funding_instruments)
        https://developer.twitter.com/en/docs/ads/analytics/api-reference/reach#get-stats-accounts-account-id-reach-funding-instruments

        Supported `endpoint_type`:
            `all` (default)

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('tailored_audiences')
    @CustomDecorators.flatten_params
    def tailored_audiences(self, endpoint_type, **kwargs):
        """Tailored Audiences
        https://developer.twitter.com/en/docs/ads/audiences/api-reference/tailored-audiences

        Supported `endpoint_type`:
            `all`, `load`, `create`, `delete`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    def tailored_audiences_users(self, endpoint_type='create', *,
                                 tailored_audience_id, data=[]):
        """Tailored Audiences Users
        https://developer.twitter.com/en/docs/ads/audiences/api-reference/audience

        Supported `endpoint_type`:
            `create`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
            tailored_audience_id (:obj:`str`): A Tailored Audience ID to update.
            data (:obj:`list`): A JSON POST body data to send.
        """
        base = RESOURCE_TABLE['tailored_audiences_users']['RESOURCE']
        resource = base.format(account_id=self.account_id, id=tailored_audience_id)
        return Request(
            self,
            self._METHOD_MAP[endpoint_type],
            resource,
            headers={'content-type': 'application/json'},
            params={},
            body=json.dumps(data)).perform()

    @CustomDecorators.flatten_params
    def tailored_audience_permissions(self, endpoint_type, **kwargs):
        """Tailored Audience Permissions
        https://developer.twitter.com/en/docs/ads/audiences/api-reference/tailored-audience-permissions

        Supported `endpoint_type`:
            `all`, `create`, `delete`

        Args:
            endpoint_type (:obj:`str`): An endpoint type.
        """
        if endpoint_type in ['all', 'create']:
            base = RESOURCE_TABLE['tailored_audience_permissions']['RESOURCE_COLLECTION']
            resource = base.format(
                account_id=self.account_id,
                tailored_audience_id=kwargs.get('tailored_audience_id')
            )
        elif endpoint_type == 'delete':
            base = RESOURCE_TABLE['tailored_audience_permissions']['RESOURCE']
            resource = base.format(
                account_id=self.account_id,
                tailored_audience_id=kwargs.get('tailored_audience_id'),
                tailored_audience_permission_id=kwargs.get('tailored_audience_permission_id')
            )
        else:
            raise NotImplementedError
        return Request(
            self, self._METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @CustomDecorators.resource_controller('insights', default_operation='all')
    @CustomDecorators.flatten_params
    def insights(self, endpoint_type, **kwargs):
        """Insights
        https://developer.twitter.com/en/docs/ads/audiences/api-reference/insights

        Supported `endpoint_type`:
            `all` (default)

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('insights_available_audiences', default_operation='all')
    def insights_available_audiences(self, endpoint_type, **kwargs):
        """Insights (available_audiences)
        https://developer.twitter.com/en/docs/ads/audiences/api-reference/insights#get-insights-accounts-account-id-available-audiences

        Supported `endpoint_type`:
            `all` (default)

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()

    @CustomDecorators.resource_controller('keyword_insights', default_operation='all')
    @CustomDecorators.flatten_params
    def keyword_insights(self, endpoint_type, **kwargs):
        """Keyword Insights
        https://developer.twitter.com/en/docs/ads/audiences/api-reference/keyword-insights

        Supported `endpoint_type`:
            `all` (default)

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        return Request(
            self, self._METHOD_MAP[endpoint_type], kwargs.get('_resource'), params=kwargs).perform()
