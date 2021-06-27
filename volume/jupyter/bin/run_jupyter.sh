#!/bin/bash
# Pyenv
echo "PYENV_ROOT=$PYENV_ROOT"
echo "PATH=$PATH"
echo "PYENV_PYVER=$PYENV_PYVER"
echo "PYENV_VERSION=$PYENV_VERSION"

eval "$(pyenv init --path)"
python3 --version

# PIP Install
PATH_REQUIREMENTS_CPU="/home/$SKP_USER/jupyter/etc/requirements_cpu.txt"
PATH_REQUIREMENTS_GPU="/home/$SKP_USER/jupyter/etc/requirements_gpu.txt"
if [[ "$GPU" = *TRUE* ]] 
then
  echo PATH_REQUIREMENTS_GPU="${PATH_REQUIREMENTS_GPU}"
  pip install -r $PATH_REQUIREMENTS_GPU
else
  echo PATH_REQUIREMENTS_CPU="${PATH_REQUIREMENTS_CPU}"
  pip install -r $PATH_REQUIREMENTS_CPU
fi

# Jupyter
PATH_JUPYTERCONF="/home/$SKP_USER/jupyter/etc/jupyter_lab_config.py"
echo PATH_JUPYTERCONF="${PATH_JUPYTERCONF}"
jupyter lab --config $PATH_JUPYTERCONF

# for container test
# while true; do
#   echo hello-`date +%s`
#   sleep 3
# done