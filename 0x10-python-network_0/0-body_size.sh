#!/bin/bash
#takes in a URL, sends request to that URL, and displays the size of the body of the response
curl -sI "$1" | grep Content-Length | cut -d ":" -f2 | cut -d " " -f2
