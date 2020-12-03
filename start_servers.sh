#!/bin/bash

./stop_servers.sh
python3 server/mikeserver.py &
python3 server/jasonserver.py &