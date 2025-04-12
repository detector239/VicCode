#!/bin/bash

g++ ./main.cpp
if [ $? == 0 ]; then
  ./a.out
fi

