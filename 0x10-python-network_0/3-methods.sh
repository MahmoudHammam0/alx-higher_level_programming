#!/bin/bash
#takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI "$1" | grep Allow | cut -d ":" -f2 | cut -d" " -f2,3,4,5,6,7,8,9,10,11,12
