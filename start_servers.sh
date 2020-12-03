#!/bin/bash

if [[ $# -lt 2 ]] ; then
    echo 'Usage: start_servers.sh MIKE_PORT JASON_PORT'
    exit 0
fi


./stop_servers.sh
python3 server/mikeserver.py $1 &
python3 server/jasonserver.py $1 $2 &