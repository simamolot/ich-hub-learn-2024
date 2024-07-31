#!/bin/bash

mkdir -p /opt/310524-ptm/Serafima/hw13
for i in {1..10}
do
    touch "/opt/310524-ptm/Serafima/hw13/${i}_$(date +%d.%m.%y)"
done
