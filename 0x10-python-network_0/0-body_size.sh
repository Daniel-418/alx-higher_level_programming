#!/bin/bash
# downloads a file
curl -s "$1" | wc -c
