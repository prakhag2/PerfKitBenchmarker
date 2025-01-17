# Copyright 2021 PerfKitBenchmarker Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Module containing OpenFOAM installation and cleanup functions.

OpenFOAM is a C++ toolbox for the development of customized numerical solvers,
and pre-/post-processing utilities for the solution of continuum mechanics
problems, most prominently including computational fluid dynamics.
OpenFOAM foundation: https://openfoam.org/.

Instructions for installing OpenFOAM: https://openfoam.org/download/7-ubuntu/.

NOTE -
"""

import posixpath


PACKAGE_NAME = 'openfoam'


OPENFOAM_ROOT = '/opt/openfoam7'


"""Needed for downloading OpenFOAM."""
_OPENFOAM_REPOSITORY_URL = 'http://dl.openfoam.org/ubuntu'
_OPENFOAM_REPOSITORY_KEY = 'openfoam.key'


def YumInstall(vm):
  del vm
  raise NotImplementedError()


def AptInstall(vm):
  """Install OpenFOAM https://openfoam.org/download/7-ubuntu/."""
  remote_key_file = '/tmp/openfoam.key'
  vm.PushDataFile(_OPENFOAM_REPOSITORY_KEY, remote_key_file)
  vm.RemoteCommand(f'sudo apt-key add {remote_key_file}; rm {remote_key_file}')
  vm.RemoteCommand(f'sudo add-apt-repository {_OPENFOAM_REPOSITORY_URL}')
  vm.RemoteCommand('sudo apt-get -y update')
  vm.Install('build_tools')
  vm.InstallPackages('openfoam7')
  openfoam_bash_path = posixpath.join(OPENFOAM_ROOT, 'etc/bashrc')

  # Separate commands since $WM_PROJECT_DIR comes from the OpenFOAM bashrc.
  vm.RemoteCommand(f'cat {openfoam_bash_path} | tee $HOME/.bashrc')
  vm.RemoteCommand('cat $WM_PROJECT_DIR/bin/tools/RunFunctions | '
                   'tee -a $HOME/.bashrc')
