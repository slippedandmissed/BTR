#!/bin/bash

if [[ $# -lt 4 ]] ; then
    echo 'Usage: run_client.sh APPLICATION_HOST APPLICATION_PORT MIKE_HOST MIKE_PORT'
    exit 0
fi

python3 client/mikeclient $1 $2 $3 $4