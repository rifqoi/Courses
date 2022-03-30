#!/bin/bash

files=$(grep ' jane ' ~/data/list.txt | cut -d' ' -f3-)

for file in $files; do
    if [ -e ..$file ]; then
        echo ..$file >> oldFiles.txt
    fi
done
