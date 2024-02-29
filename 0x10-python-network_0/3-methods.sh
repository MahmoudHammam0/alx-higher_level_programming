#!/bin/bash
#displays all HTTP methods the server will accept.
curl -sI "$1" | grep Allow | cut -d ":" -f2 | cut -d" " -f2,3,4,5,6,7,8,9,10,11,12
