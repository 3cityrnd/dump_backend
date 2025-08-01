#!/bin/bash

mkdir -p backend_out

find ./backend_logs -name '*.log' | while read item; do
  dir="backend_out/$(dirname "${item#./backend_logs/}")"
#   mkdir -p "$dir"
  tlparse "$item" -o "$dir"
done
