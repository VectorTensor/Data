#!/bin/bash
#Enter data for X
data1=(1000 2000)
#Enter data for Y Elements are separated by space
data2=(10 20)
a=${#data1[@]}
var1=0
curl 'http://127.0.0.1:8000/api/del' -X DELETE
while [ $var1 -lt $a ]
do
	./send.sh ${data1[$var1]} ${data2[$var1]}
	var1=$[ var1 + 1 ]


done


