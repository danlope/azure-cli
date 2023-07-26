# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "cosmosdb postgres cluster list",
    is_preview=True,
)
class List(AAZCommand):
    """List all clusters in a subscription or a resource group.

    :example: List clusters in a resource group
        az cosmosdb postgres cluster list -g "testGroup" --subscription "ffffffff-ffff-ffff-ffff-ffffffffffff"

    :example: List clusters in a subscription
        az cosmosdb postgres cluster list --subscription "ffffffff-ffff-ffff-ffff-ffffffffffff"
    """

    _aaz_info = {
        "version": "2022-11-08",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.dbforpostgresql/servergroupsv2", "2022-11-08"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.dbforpostgresql/servergroupsv2", "2022-11-08"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        condition_1 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        if condition_0:
            self.ClustersListByResourceGroup(ctx=self.ctx)()
        if condition_1:
            self.ClustersList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class ClustersListByResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-08",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _ListHelper._build_schema_system_data_read(_element.system_data)
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.administrator_login = AAZStrType(
                serialized_name="administratorLogin",
                flags={"read_only": True},
            )
            properties.citus_version = AAZStrType(
                serialized_name="citusVersion",
            )
            properties.coordinator_enable_public_ip_access = AAZBoolType(
                serialized_name="coordinatorEnablePublicIpAccess",
            )
            properties.coordinator_server_edition = AAZStrType(
                serialized_name="coordinatorServerEdition",
            )
            properties.coordinator_storage_quota_in_mb = AAZIntType(
                serialized_name="coordinatorStorageQuotaInMb",
            )
            properties.coordinator_v_cores = AAZIntType(
                serialized_name="coordinatorVCores",
            )
            properties.earliest_restore_time = AAZStrType(
                serialized_name="earliestRestoreTime",
                flags={"read_only": True},
            )
            properties.enable_ha = AAZBoolType(
                serialized_name="enableHa",
            )
            properties.enable_shards_on_coordinator = AAZBoolType(
                serialized_name="enableShardsOnCoordinator",
            )
            properties.maintenance_window = AAZObjectType(
                serialized_name="maintenanceWindow",
            )
            properties.node_count = AAZIntType(
                serialized_name="nodeCount",
            )
            properties.node_enable_public_ip_access = AAZBoolType(
                serialized_name="nodeEnablePublicIpAccess",
            )
            properties.node_server_edition = AAZStrType(
                serialized_name="nodeServerEdition",
            )
            properties.node_storage_quota_in_mb = AAZIntType(
                serialized_name="nodeStorageQuotaInMb",
            )
            properties.node_v_cores = AAZIntType(
                serialized_name="nodeVCores",
            )
            properties.point_in_time_utc = AAZStrType(
                serialized_name="pointInTimeUTC",
            )
            properties.postgresql_version = AAZStrType(
                serialized_name="postgresqlVersion",
            )
            properties.preferred_primary_zone = AAZStrType(
                serialized_name="preferredPrimaryZone",
            )
            properties.private_endpoint_connections = AAZListType(
                serialized_name="privateEndpointConnections",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.read_replicas = AAZListType(
                serialized_name="readReplicas",
                flags={"read_only": True},
            )
            properties.server_names = AAZListType(
                serialized_name="serverNames",
                flags={"read_only": True},
            )
            properties.source_location = AAZStrType(
                serialized_name="sourceLocation",
            )
            properties.source_resource_id = AAZStrType(
                serialized_name="sourceResourceId",
            )
            properties.state = AAZStrType(
                flags={"read_only": True},
            )

            maintenance_window = cls._schema_on_200.value.Element.properties.maintenance_window
            maintenance_window.custom_window = AAZStrType(
                serialized_name="customWindow",
            )
            maintenance_window.day_of_week = AAZIntType(
                serialized_name="dayOfWeek",
            )
            maintenance_window.start_hour = AAZIntType(
                serialized_name="startHour",
            )
            maintenance_window.start_minute = AAZIntType(
                serialized_name="startMinute",
            )

            private_endpoint_connections = cls._schema_on_200.value.Element.properties.private_endpoint_connections
            private_endpoint_connections.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _ListHelper._build_schema_system_data_read(_element.system_data)
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties
            properties.group_ids = AAZListType(
                serialized_name="groupIds",
            )
            properties.private_endpoint = AAZObjectType(
                serialized_name="privateEndpoint",
            )
            properties.private_link_service_connection_state = AAZObjectType(
                serialized_name="privateLinkServiceConnectionState",
            )

            group_ids = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties.group_ids
            group_ids.Element = AAZStrType()

            private_endpoint = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties.private_endpoint
            private_endpoint.id = AAZStrType()

            private_link_service_connection_state = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties.private_link_service_connection_state
            private_link_service_connection_state.actions_required = AAZStrType(
                serialized_name="actionsRequired",
            )
            private_link_service_connection_state.description = AAZStrType()
            private_link_service_connection_state.status = AAZStrType()

            read_replicas = cls._schema_on_200.value.Element.properties.read_replicas
            read_replicas.Element = AAZStrType()

            server_names = cls._schema_on_200.value.Element.properties.server_names
            server_names.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.server_names.Element
            _element.fully_qualified_domain_name = AAZStrType(
                serialized_name="fullyQualifiedDomainName",
                flags={"read_only": True},
            )
            _element.name = AAZStrType()

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class ClustersList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-08",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _ListHelper._build_schema_system_data_read(_element.system_data)
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.administrator_login = AAZStrType(
                serialized_name="administratorLogin",
                flags={"read_only": True},
            )
            properties.citus_version = AAZStrType(
                serialized_name="citusVersion",
            )
            properties.coordinator_enable_public_ip_access = AAZBoolType(
                serialized_name="coordinatorEnablePublicIpAccess",
            )
            properties.coordinator_server_edition = AAZStrType(
                serialized_name="coordinatorServerEdition",
            )
            properties.coordinator_storage_quota_in_mb = AAZIntType(
                serialized_name="coordinatorStorageQuotaInMb",
            )
            properties.coordinator_v_cores = AAZIntType(
                serialized_name="coordinatorVCores",
            )
            properties.earliest_restore_time = AAZStrType(
                serialized_name="earliestRestoreTime",
                flags={"read_only": True},
            )
            properties.enable_ha = AAZBoolType(
                serialized_name="enableHa",
            )
            properties.enable_shards_on_coordinator = AAZBoolType(
                serialized_name="enableShardsOnCoordinator",
            )
            properties.maintenance_window = AAZObjectType(
                serialized_name="maintenanceWindow",
            )
            properties.node_count = AAZIntType(
                serialized_name="nodeCount",
            )
            properties.node_enable_public_ip_access = AAZBoolType(
                serialized_name="nodeEnablePublicIpAccess",
            )
            properties.node_server_edition = AAZStrType(
                serialized_name="nodeServerEdition",
            )
            properties.node_storage_quota_in_mb = AAZIntType(
                serialized_name="nodeStorageQuotaInMb",
            )
            properties.node_v_cores = AAZIntType(
                serialized_name="nodeVCores",
            )
            properties.point_in_time_utc = AAZStrType(
                serialized_name="pointInTimeUTC",
            )
            properties.postgresql_version = AAZStrType(
                serialized_name="postgresqlVersion",
            )
            properties.preferred_primary_zone = AAZStrType(
                serialized_name="preferredPrimaryZone",
            )
            properties.private_endpoint_connections = AAZListType(
                serialized_name="privateEndpointConnections",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.read_replicas = AAZListType(
                serialized_name="readReplicas",
                flags={"read_only": True},
            )
            properties.server_names = AAZListType(
                serialized_name="serverNames",
                flags={"read_only": True},
            )
            properties.source_location = AAZStrType(
                serialized_name="sourceLocation",
            )
            properties.source_resource_id = AAZStrType(
                serialized_name="sourceResourceId",
            )
            properties.state = AAZStrType(
                flags={"read_only": True},
            )

            maintenance_window = cls._schema_on_200.value.Element.properties.maintenance_window
            maintenance_window.custom_window = AAZStrType(
                serialized_name="customWindow",
            )
            maintenance_window.day_of_week = AAZIntType(
                serialized_name="dayOfWeek",
            )
            maintenance_window.start_hour = AAZIntType(
                serialized_name="startHour",
            )
            maintenance_window.start_minute = AAZIntType(
                serialized_name="startMinute",
            )

            private_endpoint_connections = cls._schema_on_200.value.Element.properties.private_endpoint_connections
            private_endpoint_connections.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _ListHelper._build_schema_system_data_read(_element.system_data)
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties
            properties.group_ids = AAZListType(
                serialized_name="groupIds",
            )
            properties.private_endpoint = AAZObjectType(
                serialized_name="privateEndpoint",
            )
            properties.private_link_service_connection_state = AAZObjectType(
                serialized_name="privateLinkServiceConnectionState",
            )

            group_ids = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties.group_ids
            group_ids.Element = AAZStrType()

            private_endpoint = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties.private_endpoint
            private_endpoint.id = AAZStrType()

            private_link_service_connection_state = cls._schema_on_200.value.Element.properties.private_endpoint_connections.Element.properties.private_link_service_connection_state
            private_link_service_connection_state.actions_required = AAZStrType(
                serialized_name="actionsRequired",
            )
            private_link_service_connection_state.description = AAZStrType()
            private_link_service_connection_state.status = AAZStrType()

            read_replicas = cls._schema_on_200.value.Element.properties.read_replicas
            read_replicas.Element = AAZStrType()

            server_names = cls._schema_on_200.value.Element.properties.server_names
            server_names.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.server_names.Element
            _element.fully_qualified_domain_name = AAZStrType(
                serialized_name="fullyQualifiedDomainName",
                flags={"read_only": True},
            )
            _element.name = AAZStrType()

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_system_data_read = None

    @classmethod
    def _build_schema_system_data_read(cls, _schema):
        if cls._schema_system_data_read is not None:
            _schema.created_at = cls._schema_system_data_read.created_at
            _schema.created_by = cls._schema_system_data_read.created_by
            _schema.created_by_type = cls._schema_system_data_read.created_by_type
            _schema.last_modified_at = cls._schema_system_data_read.last_modified_at
            _schema.last_modified_by = cls._schema_system_data_read.last_modified_by
            _schema.last_modified_by_type = cls._schema_system_data_read.last_modified_by_type
            return

        cls._schema_system_data_read = _schema_system_data_read = AAZObjectType(
            flags={"read_only": True}
        )

        system_data_read = _schema_system_data_read
        system_data_read.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data_read.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data_read.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data_read.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data_read.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data_read.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.created_at = cls._schema_system_data_read.created_at
        _schema.created_by = cls._schema_system_data_read.created_by
        _schema.created_by_type = cls._schema_system_data_read.created_by_type
        _schema.last_modified_at = cls._schema_system_data_read.last_modified_at
        _schema.last_modified_by = cls._schema_system_data_read.last_modified_by
        _schema.last_modified_by_type = cls._schema_system_data_read.last_modified_by_type


__all__ = ["List"]