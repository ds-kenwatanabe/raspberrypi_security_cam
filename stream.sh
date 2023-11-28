# 8080 -> HTTP port to stream video
# Open VLC media player (network stream) or console and insert:
# http://<Raspberry Pi IP>:8080/
# eg. http://192.168.1.10:8080/
# To run as TCP do:
# raspivid -a 12 -t 0 -w 1280 -h 720 -vf -ih -fps 30 -l -o tc://0.0.0.0:5000
# and in VLC tcp/h264://192.168.1.10:5000
raspivid -o - -t 0 -hf -w 1280 -h 720 -fps 30 | cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8080}' :demux=h264
