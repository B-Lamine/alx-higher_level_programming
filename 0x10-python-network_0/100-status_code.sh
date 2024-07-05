#!/bin/bash
# get status code of HTTP request of given URL.
curl -sI "$1" -w "%{http_code}\n" -o /dev/null
