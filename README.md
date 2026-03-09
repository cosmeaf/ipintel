# IPINTEL

IPINTEL is a modular IP investigation and threat intelligence engine designed to analyze and classify IP addresses in real time.

The system aggregates multiple intelligence sources including GeoIP data, ASN information, TOR exit node detection, proxy identification, datacenter classification, reverse DNS lookup and risk scoring to provide a comprehensive view of any IP address.

IPINTEL is designed to be lightweight, extensible and suitable for integration with security platforms, APIs and monitoring systems.

---

## Features

- IP address investigation engine
- GeoIP geolocation lookup
- ASN detection and organization lookup
- TOR exit node detection
- Proxy detection
- Datacenter network identification
- Reverse DNS lookup
- Risk scoring system
- Modular architecture
- Local intelligence data sources
- Test framework included

---

## Architecture

IPINTEL is built with a modular architecture where each intelligence component operates independently.

ipintel/
│
├── engine/          # Core investigation engine
├── geoip/           # GeoIP lookup module
├── tor/             # TOR detection
├── proxy/           # Proxy detection
├── datacenter/      # Datacenter ASN detection
├── asn/             # ASN lookup
├── dns/             # Reverse DNS engine
├── risk/            # Risk scoring system
├── cache/           # Cache layer
├── stats/           # Statistics utilities
├── update/          # Intelligence data update scripts
└── tests/           # Test suite

Each module contributes intelligence signals that are combined into a final investigation result.

---

## Example Output

Example investigation result:

{
  "ip": "8.8.8.8",
  "country": "United States",
  "city": "Mountain View",
  "latitude": 37.4056,
  "longitude": -122.0775,
  "asn": 15169,
  "asn_org": "Google LLC",
  "tor": false,
  "proxy": false,
  "datacenter": true,
  "rdns": "dns.google",
  "risk_score": 20,
  "risk_reasons": [
    "Datacenter ASN"
  ]
}

---

## Installation

Clone the repository:

git clone https://github.com/yourusername/ipintel.git
cd ipintel

Create virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

---

## Usage

Basic usage example:

from engine.investigation_engine import investigate_ip

result = investigate_ip("8.8.8.8")

print(result)

---

## Running Tests

Run all tests:

python run_all_tests.py

Or run individual tests:

python tests/test_geoip.py
python tests/test_dns.py
python tests/test_proxy.py
python tests/test_tor.py

---

## Use Cases

IPINTEL can be used in multiple security and network intelligence scenarios:

- Security monitoring
- Fraud detection
- Abuse investigation
- Threat intelligence enrichment
- Network analysis
- Incident response
- Web security systems

---

## Design Goals

The project was designed with the following principles:

- Simplicity
- Modularity
- Transparency
- Extensibility
- Local intelligence processing

---

## Future Improvements

Potential improvements for future versions:

- REST API interface
- Redis caching
- Async investigation engine
- Integration with external threat feeds
- Shodan integration
- AbuseIPDB integration
- Dashboard and monitoring interface

---

## License

MIT License

---

## Author

Developed for security research and IP intelligence analysis.
