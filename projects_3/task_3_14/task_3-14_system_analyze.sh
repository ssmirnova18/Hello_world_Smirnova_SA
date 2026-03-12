#!/bin/bash

df -h | awk 'NR>1 {
    print $1, $5
    gsub("%","",$5)
    if ($5 > 90)
        print "WARNING: High disk usage on", $1
}'
