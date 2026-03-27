#!/bin/bash
# Takes a URL, sends a request and displays the size of the body in bytes
curl -s "$1" | wc -c
