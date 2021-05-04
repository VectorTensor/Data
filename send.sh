url='http://127.0.0.1:8000/api/'
data="{
\"X\":$1,
\"Y\":$2
}"
curl $url -X POST -d  "$data" -H 'content-type:application/json'

