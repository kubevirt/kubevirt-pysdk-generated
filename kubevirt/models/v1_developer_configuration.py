# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1DeveloperConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cpu_allocation_ratio': 'int',
        'feature_gates': 'list[str]',
        'log_verbosity': 'V1LogVerbosity',
        'memory_overcommit': 'int',
        'node_selectors': 'dict(str, str)',
        'pvc_tolerate_less_space_up_to_percent': 'int',
        'use_emulation': 'bool'
    }

    attribute_map = {
        'cpu_allocation_ratio': 'cpuAllocationRatio',
        'feature_gates': 'featureGates',
        'log_verbosity': 'logVerbosity',
        'memory_overcommit': 'memoryOvercommit',
        'node_selectors': 'nodeSelectors',
        'pvc_tolerate_less_space_up_to_percent': 'pvcTolerateLessSpaceUpToPercent',
        'use_emulation': 'useEmulation'
    }

    def __init__(self, cpu_allocation_ratio=None, feature_gates=None, log_verbosity=None, memory_overcommit=None, node_selectors=None, pvc_tolerate_less_space_up_to_percent=None, use_emulation=None):
        """
        V1DeveloperConfiguration - a model defined in Swagger
        """

        self._cpu_allocation_ratio = None
        self._feature_gates = None
        self._log_verbosity = None
        self._memory_overcommit = None
        self._node_selectors = None
        self._pvc_tolerate_less_space_up_to_percent = None
        self._use_emulation = None

        if cpu_allocation_ratio is not None:
          self.cpu_allocation_ratio = cpu_allocation_ratio
        if feature_gates is not None:
          self.feature_gates = feature_gates
        if log_verbosity is not None:
          self.log_verbosity = log_verbosity
        if memory_overcommit is not None:
          self.memory_overcommit = memory_overcommit
        if node_selectors is not None:
          self.node_selectors = node_selectors
        if pvc_tolerate_less_space_up_to_percent is not None:
          self.pvc_tolerate_less_space_up_to_percent = pvc_tolerate_less_space_up_to_percent
        if use_emulation is not None:
          self.use_emulation = use_emulation

    @property
    def cpu_allocation_ratio(self):
        """
        Gets the cpu_allocation_ratio of this V1DeveloperConfiguration.

        :return: The cpu_allocation_ratio of this V1DeveloperConfiguration.
        :rtype: int
        """
        return self._cpu_allocation_ratio

    @cpu_allocation_ratio.setter
    def cpu_allocation_ratio(self, cpu_allocation_ratio):
        """
        Sets the cpu_allocation_ratio of this V1DeveloperConfiguration.

        :param cpu_allocation_ratio: The cpu_allocation_ratio of this V1DeveloperConfiguration.
        :type: int
        """

        self._cpu_allocation_ratio = cpu_allocation_ratio

    @property
    def feature_gates(self):
        """
        Gets the feature_gates of this V1DeveloperConfiguration.

        :return: The feature_gates of this V1DeveloperConfiguration.
        :rtype: list[str]
        """
        return self._feature_gates

    @feature_gates.setter
    def feature_gates(self, feature_gates):
        """
        Sets the feature_gates of this V1DeveloperConfiguration.

        :param feature_gates: The feature_gates of this V1DeveloperConfiguration.
        :type: list[str]
        """

        self._feature_gates = feature_gates

    @property
    def log_verbosity(self):
        """
        Gets the log_verbosity of this V1DeveloperConfiguration.

        :return: The log_verbosity of this V1DeveloperConfiguration.
        :rtype: V1LogVerbosity
        """
        return self._log_verbosity

    @log_verbosity.setter
    def log_verbosity(self, log_verbosity):
        """
        Sets the log_verbosity of this V1DeveloperConfiguration.

        :param log_verbosity: The log_verbosity of this V1DeveloperConfiguration.
        :type: V1LogVerbosity
        """

        self._log_verbosity = log_verbosity

    @property
    def memory_overcommit(self):
        """
        Gets the memory_overcommit of this V1DeveloperConfiguration.

        :return: The memory_overcommit of this V1DeveloperConfiguration.
        :rtype: int
        """
        return self._memory_overcommit

    @memory_overcommit.setter
    def memory_overcommit(self, memory_overcommit):
        """
        Sets the memory_overcommit of this V1DeveloperConfiguration.

        :param memory_overcommit: The memory_overcommit of this V1DeveloperConfiguration.
        :type: int
        """

        self._memory_overcommit = memory_overcommit

    @property
    def node_selectors(self):
        """
        Gets the node_selectors of this V1DeveloperConfiguration.

        :return: The node_selectors of this V1DeveloperConfiguration.
        :rtype: dict(str, str)
        """
        return self._node_selectors

    @node_selectors.setter
    def node_selectors(self, node_selectors):
        """
        Sets the node_selectors of this V1DeveloperConfiguration.

        :param node_selectors: The node_selectors of this V1DeveloperConfiguration.
        :type: dict(str, str)
        """

        self._node_selectors = node_selectors

    @property
    def pvc_tolerate_less_space_up_to_percent(self):
        """
        Gets the pvc_tolerate_less_space_up_to_percent of this V1DeveloperConfiguration.

        :return: The pvc_tolerate_less_space_up_to_percent of this V1DeveloperConfiguration.
        :rtype: int
        """
        return self._pvc_tolerate_less_space_up_to_percent

    @pvc_tolerate_less_space_up_to_percent.setter
    def pvc_tolerate_less_space_up_to_percent(self, pvc_tolerate_less_space_up_to_percent):
        """
        Sets the pvc_tolerate_less_space_up_to_percent of this V1DeveloperConfiguration.

        :param pvc_tolerate_less_space_up_to_percent: The pvc_tolerate_less_space_up_to_percent of this V1DeveloperConfiguration.
        :type: int
        """

        self._pvc_tolerate_less_space_up_to_percent = pvc_tolerate_less_space_up_to_percent

    @property
    def use_emulation(self):
        """
        Gets the use_emulation of this V1DeveloperConfiguration.

        :return: The use_emulation of this V1DeveloperConfiguration.
        :rtype: bool
        """
        return self._use_emulation

    @use_emulation.setter
    def use_emulation(self, use_emulation):
        """
        Sets the use_emulation of this V1DeveloperConfiguration.

        :param use_emulation: The use_emulation of this V1DeveloperConfiguration.
        :type: bool
        """

        self._use_emulation = use_emulation

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
        if not isinstance(other, V1DeveloperConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
