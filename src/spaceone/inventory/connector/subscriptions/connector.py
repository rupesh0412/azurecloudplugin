import logging

from spaceone.inventory.libs.connector import AzureConnector
from spaceone.inventory.error import *

__all__ = ['SubscriptionsConnector']
_LOGGER = logging.getLogger(__name__)


class SubscriptionsConnector(AzureConnector):

    def __init__(self, **kwargs):
        super().__init__()
        self.set_connect(kwargs.get('secret_data'))

    def get_subscription_info(self, subscription_id):
        return self.subscription_client.subscriptions.get(subscription_id)

    def list_location_info(self, subscription_id):
        return self.subscription_client.subscriptions.list_locations(subscription_id)
