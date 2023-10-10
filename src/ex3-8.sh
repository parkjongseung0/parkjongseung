#!/bin/sh

if [ ! -d "DB.txt" ]; then
    touch "DB.txt"
fi
echo "$1,$2" >> DB.txt

exit 0