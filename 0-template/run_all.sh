#!/bin/bash

dev="cpu cuda"



export TORCHINDUCTOR_CACHE_DIR=`pwd`/tmp_inductor_cache


RM_LIST="tmp_inductor_cache backend_logs backend_out"
#RM_LIST="backend_logs backend_out"

for d in $RM_LIST; do
  
	if [ -d $d ]; then
           rm -rf $d
	   echo "$d has been removed"
	fi
done



for d in $dev; do

export DEVICE=$d
DYN_LIST="True False"

   for DYN in $DYN_LIST; do
    export DYNAMIC=$DYN
    python dump_backend.py
   done

done

./convert.sh
