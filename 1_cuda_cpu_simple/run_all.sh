#!/bin/bash

dev="cpu cuda"


for d in $dev; do

export DEVICE=$d
DYN_LIST="True False"

   for DYN in $DYN_LIST; do
    export DYNAMIC=$DYN
    python dump_backend.py
   done

done

./convert.sh
