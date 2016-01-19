#!/bin/sh

CUSTOM_PYTHON="yes"
[[ -z $PYTHON ]] && CUSTOM_PYTHON="no"
PYTHON=${PYTHON-python}

## Test 1: Module App; Feature Global options

echo -n "Running Test #1... "

TEST0=$($PYTHON -m CLIApp.app --this-is-a-test | grep "^Global options")
if [[ $TEST0 == "Global options: ['--this-is-a-test']" ]]
then
	echo "Passed"
else
	echo "Failed!"
	exit 1
fi

## Test 2: Module App; Feature Actions
echo -n "Running Test #2... "

TEST1=$($PYTHON -m CLIApp.app test --this-is-a-test | grep "^Action" | tr "\n" "+")
TEST1_1=$(echo $TEST1 | tr "+" "\n" | grep -v "options" | cut -c10-)
TEST1_2=$(echo $TEST1 | tr "+" "\n" | grep "options" | cut -c19-34)

if [[ $TEST1_1 == "test" ]] 
then
	echo -n "[1/2] "
else
	echo "Failed!"
	exit 1
fi

if [[ $TEST1_2 == "--this-is-a-test" ]]
then
	echo -n "[2/2] "
else
	echo " Failed! == $TEST1_2"
	exit 1
fi
echo "Passed"

## Test 3: Module App; Feature Arguments

echo -n "Running Test #3... "

TEST3=$($PYTHON -m CLIApp.app test --foo this is "a test" | grep "Arguments" | cut -c19-38 | sed "s/', '/+/g")
if [[ $TEST3 == "this+is+a test" ]]
then
	echo "Passed"
else
	echo "Failed!"
	exit 1
fi

echo "All tests passed :)"

