#!/bin/bash
# display content-length of http response
curl -sI "$1" | grep Content-Length | awk '{print $2}'
