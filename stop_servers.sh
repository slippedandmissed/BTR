#!/bin/bash

ps aux | grep -ie mikeserver | awk '{print "kill -9 " $2}' | sh -x
ps aux | grep -ie jasonserver | awk '{print "kill -9 " $2}' | sh -x