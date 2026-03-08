# /opt/ipintel/update/update_tor.sh

#!/bin/bash
set -e

DEST="/opt/ipintel/tor/exit_nodes.txt"

curl -s https://check.torproject.org/torbulkexitlist > $DEST