#!/bin/bash
while true; do date +%I:%M | osd_cat -d 60 -l 2 -A center -p bottom -f "lucidasanstypewriter-bold-12"; sleep 60;done
