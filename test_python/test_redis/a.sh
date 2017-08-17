#!/bin/bash

for i in `seq 5`
do
    ./sub.py &>sub-$i.log &
    echo $!
done
