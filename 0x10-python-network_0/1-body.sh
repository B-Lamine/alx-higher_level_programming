#!/bin/bash
# display body of a successful http request
status_code=$(curl -so /dev/null -w "%{http_code}" "$1")
if [ "$status_code" -eq 200 ]
then
	curl -s "$1"
fi
