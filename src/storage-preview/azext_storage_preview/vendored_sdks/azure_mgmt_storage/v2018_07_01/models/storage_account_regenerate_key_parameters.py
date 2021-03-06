# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class StorageAccountRegenerateKeyParameters(Model):
    """The parameters used to regenerate the storage account key.

    All required parameters must be populated in order to send to Azure.

    :param key_name: Required. The name of storage keys that want to be
     regenerated, possible vaules are key1, key2.
    :type key_name: str
    """

    _validation = {
        'key_name': {'required': True},
    }

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StorageAccountRegenerateKeyParameters, self).__init__(**kwargs)
        self.key_name = kwargs.get('key_name', None)
