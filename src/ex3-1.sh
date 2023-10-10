#!/bin/sh
if [ -n "$1" ]; then
    i='1'
    while [ $i -le $1 ]
    do
        echo "hello world"
        i=`expr $i + 1`
    done
else
    while [ 1 ]
    do
        echo "hello world"
    done
fi

exit 0