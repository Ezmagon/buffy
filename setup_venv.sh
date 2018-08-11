#!/bin/bash
# Setup virtualenvironment on unix system
# With correct dependencies as described by the package
# Updates dependencies if venv already exists


if [ ! -d ./venv/ ]
then
    which virtualenv
    if [[ $? -ne 0 ]]
    then
        pip install virtualenv
        if [[ $? -ne 0 ]]
        then
            echo "Please install pip"
            exit 1
        fi
    fi
    virtualenv ./venv/
fi

function get_deps(){
    echo $(grep "install_requires" setup.py | sed -n "s/install_requires =\[\(.*\)\]/\1/g;s/[\',]//g;p")
}
DEPS=($(get_deps))

source ./venv/bin/activate
pip install ${DEPS[@]}
deactivate