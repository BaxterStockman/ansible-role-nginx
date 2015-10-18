# (c) 2015, Matt Schreiber <schreibah@gmail.com>,
# 2012, Michael DeHaan <michael.dehaan@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

import os

import ansible.constants as C

from ansible import utils
from ansible import errors
from ansible.callbacks import vvvv
from ansible.runner.return_data import ReturnData


class ActionModule(object):

    TRANSFERS_FILES = True

    # Paths, relative to files/, of required Python libraries
    required_sources = [dict(src='utils', dirname='files')]

    def __init__(self, runner):
        self.runner = runner
        # Instantiate the action_plugin for the 'bootstrap' module
        self.bootstrap_handler = utils.plugins.action_loader.get('bootstrap', runner)

    def _get_source_abspaths(self, sources):
        return map(lambda x: dict(src=utils.path_dwim_relative(__file__, x.get('dirname', None), x.get('src', None), self.runner.basedir)), sources)

    def run(self, conn, tmp, module_name, module_args, inject, complex_args=None, **kwargs):
        sources = self._get_source_abspaths(self.required_sources)

        nginx_options = None
        if module_args:
            nginx_options = module_args
        else:
            nginx_options = complex_args

        bootstrap_complex_args = dict(sources=sources, skip_action_plugin=True, nginx_config=nginx_options)
        return self.bootstrap_handler.run(conn, tmp, 'bootstrap', '', inject, complex_args=bootstrap_complex_args, **kwargs)
