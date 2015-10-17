#!/usr/bin/env bash

CUSTOM_PYTHON="yes"
[[ -z $PYTHON ]] && CUSTOM_PYTHON="no"
PYTHON=${PYTHON-python}

echo "Testing with $(which $PYTHON) ($($PYTHON --version 2>&1))"
if [[ $CUSTOM_PYTHON == "no" ]]
then
	echo "  Note: Set PYTHON to the executable to use to overwrite the default"
fi
echo
$PYTHON -m CLIApp.__init__ $@
