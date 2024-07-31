#!/bin/bash
#
#for i in {1..10}
#do
    #current_time=$(date +"%H:%M:%S")
    #process_count=$(ps -e --no-headers | wc -l)
    #echo "$current_time $process_count" >> /opt/310524-ptm/Serafima/file_hm15.txt
    #sleep 5
#done 

#echo "$(lscpu)" >> /opt/310524-ptm/Serafima/file_hm15.txt
#echo "$(uname -0)" >> /opt/310524-ptm/Serafima/file_hm15.txt

for i in {50..100}
    do
        touch "${i}.txt"
done
