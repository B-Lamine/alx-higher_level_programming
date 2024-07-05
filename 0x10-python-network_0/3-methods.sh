#!/bin/bash
# list http methods accepted by the given url.
curl -sI "$1" -X OPTIONS | grep Allow | sed 's/Allow: //'
