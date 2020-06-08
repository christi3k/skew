# Copyright 2015 Mitch Garnaat
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from skew.exception import ConfigNotFoundError

LOG = logging.getLogger(__name__)

_config = None


def get_config():
    global _config
    if _config is None:
        raise ConfigNotFoundError('Unable to find skew config file')
    return _config


def set_config(config_dict):
    global _config
    _config = config_dict
