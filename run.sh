#!/bin/bash

[[ $2 == *"e"* ]] && INPUT=example.txt || INPUT=input.txt
[[ $2 == *"g"* ]] && BINARY=golf.py || BINARY=solve.py

RUNNER=python3

try() {
    [ -f $1/$BINARY ] && $RUNNER $1/$BINARY < $1/$INPUT
}

try $1 || try day$1 $2