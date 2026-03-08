#!/bin/bash
set -e

BASE="/opt/ipintel/geoip"
TMP="/tmp/geoip_update"

mkdir -p "$BASE"
mkdir -p "$TMP"

cd "$TMP"

echo "Downloading GeoLite2 City..."
curl -L -o GeoLite2-City.mmdb \
https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-City.mmdb

echo "Downloading GeoLite2 ASN..."
curl -L -o GeoLite2-ASN.mmdb \
https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-ASN.mmdb

mv GeoLite2-City.mmdb "$BASE/"
mv GeoLite2-ASN.mmdb "$BASE/"

rm -rf "$TMP"

echo "GeoIP database updated"