# Copyright (c) 2014 Scopely, Inc.
# Copyright (c) 2015 Mitch Garnaat
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from skew.resources.aws import AWSResource


class DBCluster(AWSResource):

    class Meta(object):
        service = 'rds'
        type = 'cluster'
        enum_spec = ('describe_db_clusters', 'DBClusters', None)
        tags_spec = ('list_tags_for_resource', 'TagList',
                     'ResourceName', 'arn')
        detail_spec = None
        id = 'DBClusterIdentifier'
        filter_name = 'DBClusterIdentifier'
        filter_type = 'scalar'
        name = 'Database.Name'
        date = 'ClusterCreateTime'
        dimension = 'DBClusterIdentifier'

    @property
    def arn(self):
        return 'arn:aws:%s:%s:%s:%s:%s' % (
            self._client.service_name,
            self._client.region_name,
            self._client.account_id, self.resourcetype, self.id)


class DBInstance(AWSResource):

    class Meta(object):
        service = 'rds'
        type = 'db'
        enum_spec = ('describe_db_instances', 'DBInstances', None)
        tags_spec = ('list_tags_for_resource', 'TagList',
                     'ResourceName', 'arn')
        detail_spec = None
        id = 'DBInstanceIdentifier'
        filter_name = 'DBInstanceIdentifier'
        filter_type = 'scalar'
        name = 'Endpoint.Address'
        date = 'InstanceCreateTime'
        dimension = 'DBInstanceIdentifier'

    @property
    def arn(self):
        return 'arn:aws:%s:%s:%s:%s:%s' % (
            self._client.service_name,
            self._client.region_name,
            self._client.account_id, self.resourcetype, self.id)


class DBSecurityGroup(AWSResource):

    class Meta(object):
        service = 'rds'
        type = 'secgrp'
        enum_spec = ('describe_db_security_groups', 'DBSecurityGroups', None)
        detail_spec = None
        id = 'DBSecurityGroupName'
        filter_name = 'DBSecurityGroupName'
        filter_type = 'scalar'
        name = 'DBSecurityGroupDescription'
        date = None
        dimension = None
        tags_spec = ('list_tags_for_resource', 'TagList', 'ResourceName', 'arn')

    @property
    def arn(self):
        return 'arn:aws:%s:%s:%s:%s:%s' % (
            self._client.service_name,
            self._client.region_name,
            self._client.account_id, self.resourcetype, self.id)

class DBParameterGroups(AWSResource):

    class Meta(object):
        service = 'rds'
        type = 'pg'
        enum_spec = ('describe_db_parameter_groups', 'DBParameterGroups', None)
        detail_spec = None
        id = 'DBParameterGroupName'
        filter_name = 'DBParameterGroupName'
        filter_type = 'scalar'
        name = 'Description'
        date = None
        dimension = None
        tags_spec = ('list_tags_for_resource', 'TagList', 'ResourceName', 'arn')

    @property
    def arn(self):
        return 'arn:aws:%s:%s:%s:%s:%s' % (
            self._client.service_name,
            self._client.region_name,
            self._client.account_id, self.resourcetype, self.id)

class DBSnapshots(AWSResource):

    class Meta(object):
        service = 'rds'
        type = 'snapshot'
        enum_spec = ('describe_db_snapshots', 'DBSnapshots', None)
        detail_spec = None
        id = 'DBSnapshotIdentifier'
        filter_name = 'DBSnapshotIdentifier'
        filter_type = 'scalar'
        name = 'DBSnapshotIdentifier'
        date = None
        dimension = None
        tags_spec = ('list_tags_for_resource', 'TagList', 'ResourceName', 'arn')

    @property
    def arn(self):
        return 'arn:aws:%s:%s:%s:%s:%s' % (
            self._client.service_name,
            self._client.region_name,
            self._client.account_id, self.resourcetype, self.id)

class DBOptionGroups(AWSResource):

    class Meta(object):
        service = 'rds'
        type = 'og'
        enum_spec = ('describe_option_groups', 'OptionGroupsList', None)
        detail_spec = None
        id = 'OptionGroupName'
        filter_name = 'OptionGroupName'
        filter_type = 'scalar'
        name = 'OptionGroupName'
        date = None
        dimension = None
        tags_spec = ('list_tags_for_resource', 'TagList', 'ResourceName', 'arn')

    @property
    def arn(self):
        return 'arn:aws:%s:%s:%s:%s:%s' % (
            self._client.service_name,
            self._client.region_name,
            self._client.account_id, self.resourcetype, self.id)


class DBSubnetGroups(AWSResource):

    class Meta(object):
        service = 'rds'
        type = 'subgrp'
        enum_spec = ('describe_db_subnet_groups', 'DBSubnetGroups', None)
        detail_spec = None
        id = 'DBSubnetGroupName'
        filter_name = 'DBSubnetGroupName'
        filter_type = 'scalar'
        name = 'DBSubnetGroupName'
        date = None
        dimension = None
        tags_spec = ('list_tags_for_resource', 'TagList', 'ResourceName', 'arn')

    @property
    def arn(self):
        return 'arn:aws:%s:%s:%s:%s:%s' % (
            self._client.service_name,
            self._client.region_name,
            self._client.account_id, self.resourcetype, self.id)

class DBClusterSnapshots(AWSResource):

    class Meta(object):
        service = 'rds'
        type = 'cluster-snapshot'
        enum_spec = ('describe_db_cluster_snapshots', 'DBClusterSnapshots', None)
        detail_spec = None
        id = 'DBClusterSnapshotIdentifier'
        filter_name = 'DBClusterSnapshotIdentifier'
        filter_type = 'scalar'
        name = 'DBClusterSnapshotIdentifier'
        date = None
        dimension = None
        tags_spec = ('list_tags_for_resource', 'TagList', 'ResourceName', 'arn')

    @property
    def arn(self):
        return 'arn:aws:%s:%s:%s:%s:%s' % (
            self._client.service_name,
            self._client.region_name,
            self._client.account_id, self.resourcetype, self.id)

class DBClusterParameterGroups(AWSResource):

    class Meta(object):
        service = 'rds'
        type = 'cluster-pg'
        enum_spec = ('describe_db_cluster_parameter_groups', 'DBClusterParameterGroups', None)
        detail_spec = None
        id = 'DBClusterParameterGroupName'
        filter_name = 'DBClusterParameterGroupName'
        filter_type = 'scalar'
        name = 'Description'
        date = None
        dimension = None
        tags_spec = ('list_tags_for_resource', 'TagList', 'ResourceName', 'arn')

    @property
    def arn(self):
        return 'arn:aws:%s:%s:%s:%s:%s' % (
            self._client.service_name,
            self._client.region_name,
            self._client.account_id, self.resourcetype, self.id)

