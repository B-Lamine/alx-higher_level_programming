#!/bin/bash
# sends a get request to given URL and sets header variable.
curl -s "$1" -H "X-School-User-Id: 98"
