# /opt/ipintel/update/update_datacenter.sh

#!/bin/bash
set -e

DEST="/opt/ipintel/datacenter/datacenter_asn.txt"

cat <<EOF > $DEST
16509
15169
8075
14618
14061
EOF