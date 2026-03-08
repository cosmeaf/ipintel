#!/bin/bash

LOG="/opt/ipintel/logs/ipintel.log"

timestamp() {
    date "+%Y-%m-%d %H:%M:%S"
}

log() {
    echo "$(timestamp) | $1" >> "$LOG"
}

run_update() {
    SCRIPT=$1
    NAME=$2

    log "START: $NAME"

    if bash "$SCRIPT" >> "$LOG" 2>&1; then
        log "SUCCESS: $NAME"
    else
        log "ERROR: $NAME FAILED"
    fi
}

log "=========================================="
log "IPINTEL UPDATE START"

run_update "/opt/ipintel/update/update_geoip.sh" "GEOIP"
run_update "/opt/ipintel/update/update_tor.sh" "TOR"
run_update "/opt/ipintel/update/update_proxy.sh" "PROXY"
run_update "/opt/ipintel/update/update_datacenter.sh" "DATACENTER"

log "IPINTEL UPDATE FINISHED"
log "=========================================="