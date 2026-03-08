# /opt/ipintel/update/update_proxy.sh

#!/bin/bash
set -e

DEST="/opt/ipintel/proxy/proxy_list.txt"

curl -s https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt > $DEST