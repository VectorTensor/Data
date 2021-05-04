#!/bin/bash

data1=(1000 2000)
data2=(10 20``)
a=${#data1[@]}
var1=0
while [ $var1 -lt $a ]
do
	./send.sh ${data1[$var1]} ${data2[$var1]}
	var1=$[ var1 + 1 ]


done

