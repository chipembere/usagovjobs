#!/bin/bash

if [ $1 = "report" ]; then
    export PATH="/root/.local/bin:$PATH"
    echo "$PWD" "Runner"
    cd ../app
    poetry run python3 usagovjobs/main.py -r
else
    export PATH="/root/.local/bin:$PATH"
    echo "$PWD" "Runner"
    cd ../app
    poetry run python3 usagovjobs/main.py -e
fi
