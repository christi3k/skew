import logging
from skew.resources.aws import AWSResource

LOG = logging.getLogger(__name__)

class Secret(AWSResource):

    class Meta(object):
        service = 'secretsmanager'
        type = 'secret'
        enum_spec = ('list_secrets', 'SecretList', None)
        detail_spec = None
        id = 'ARN'
        filter_name = None
        name = 'Name'
        date = 'LastChangedDate'

    @property
    def arn(self):
        return self.id
