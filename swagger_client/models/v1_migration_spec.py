# coding: utf-8

"""


    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version:

    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1MigrationSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, selector=None, node_selector=None):
        """
        V1MigrationSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'selector': 'V1VMSelector',
            'node_selector': 'object'
        }

        self.attribute_map = {
            'selector': 'selector',
            'node_selector': 'nodeSelector'
        }

        self._selector = selector
        self._node_selector = node_selector

    @property
    def selector(self):
        """
        Gets the selector of this V1MigrationSpec.
        Criterias for selecting the VM to migrate. For example selector:   name: testvm will select the VM `testvm` for migration

        :return: The selector of this V1MigrationSpec.
        :rtype: V1VMSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1MigrationSpec.
        Criterias for selecting the VM to migrate. For example selector:   name: testvm will select the VM `testvm` for migration

        :param selector: The selector of this V1MigrationSpec.
        :type: V1VMSelector
        """

        self._selector = selector

    @property
    def node_selector(self):
        """
        Gets the node_selector of this V1MigrationSpec.
        Criteria to use when selecting the destination for the migration for example, to select by the hostname, specify `kubernetes.io/hostname: master` other possible choices include the hardware required to run the vm or or lableing of the nodes to indicate their roles in larger applications. examples: disktype: ssd, randomGenerator: /dev/random, randomGenerator: superfastdevice, app: mysql, licensedForServiceX: true Note that these selectors are additions to the node selectors on the VM itself and they must not exist on the VM. If they are conflicting with the VM, no migration will be started.

        :return: The node_selector of this V1MigrationSpec.
        :rtype: object
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """
        Sets the node_selector of this V1MigrationSpec.
        Criteria to use when selecting the destination for the migration for example, to select by the hostname, specify `kubernetes.io/hostname: master` other possible choices include the hardware required to run the vm or or lableing of the nodes to indicate their roles in larger applications. examples: disktype: ssd, randomGenerator: /dev/random, randomGenerator: superfastdevice, app: mysql, licensedForServiceX: true Note that these selectors are additions to the node selectors on the VM itself and they must not exist on the VM. If they are conflicting with the VM, no migration will be started.

        :param node_selector: The node_selector of this V1MigrationSpec.
        :type: object
        """

        self._node_selector = node_selector

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other