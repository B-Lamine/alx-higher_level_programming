#!/bin/bash
# sends a POST request to given URL with data from given json file.
curl -s "$1" -X POST -d @"$2" 
