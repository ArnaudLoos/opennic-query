import requests
import json
import subprocess

# Uses Opennic API to trim the list of servers returned
# https://wiki.opennic.org/api/geoip
# Uses geoIP by default to determine servers closest to your present location
# res=10 returns 10 servers, ipv=4 only returns IPv4 addresses, anon=true returns servers with no logs or anonymized logs
opennic = 'https://api.opennicproject.org/geoip/?json&res=10&ipv=4&anon=true'

# namebench base command
# q=100 is 100 queries per server, j=4 uses 4 processor threads, O is to only check the following server IPs. This command ignores your current DNS servers and only tests the downloaded list.
namebench_base = "namebench -q 100 -j 4 -O "

print("*** Attempting downlaod of server list ***")

try:
    hosts = requests.get(opennic).json()    # returns a list of dictionaries in json
except requests.ConnectionError:
    print("Unable to connect to Opennic website")
    exit()
except requests.ConnectionTimeout:
    print("Connection timed out")
    exit()

print("*** Server list successfully downloaded ***")

ipList = []
# Loops through list extracting the IP of each server
for i in range(0,10):
    ipList.append(hosts[i]['ip'] + " ")

# Converts list of IPs to string to pass to command
ipString = ''.join(ipList)

cmd = namebench_base + ipString
#print(cmd)

print("*** Starting Namebench ***")

# subprocess.run() requires python 3.5 or later
subprocess.run([cmd], shell=True)


"""
Namebench Options:
-h, --help show this help message and exit
-r RUN_COUNT, --runs=RUN_COUNT Number of test runs to perform on each nameserver.
-z CONFIG, --config=CONFIG Config file to use.
-o OUTPUT_FILE, --output=OUTPUT_FILE Filename to write output to
-t TEMPLATE, --template=TEMPLATE Template to use for output generation (ascii, html, resolv.conf)
-c CSV_FILE, --csv_output=CSV_FILE Filename to write query details to (CSV)
-j HEALTH_THREAD_COUNT, --health_threads=HEALTH_THREAD_COUNT # of health check threads to use
-J BENCHMARK_THREAD_COUNT, --benchmark_threads=BENCHMARK_THREAD_COUNT # of benchmark threads to use
-P PING_TIMEOUT, --ping_timeout=PING_TIMEOUT # of seconds ping requests timeout in.
-y TIMEOUT, --timeout=TIMEOUT # of seconds general requests timeout in.
-Y HEALTH_TIMEOUT, --health_timeout=HEALTH_TIMEOUT health check timeout (in seconds)
-i INPUT_SOURCE, --input=INPUT_SOURCE Import hostnames from an filename or application (alexa, cachehit, cachemiss, cachemix, camino, chrome, chromium, epiphany, firefox, flock, galeon, icab, internet_explorer, konqueror, midori, omniweb, opera, safari, seamonkey, squid, sunrise)
-I, --invalidate_cache Force health cache to be invalidated
-q QUERY_COUNT, --query_count=QUERY_COUNT Number of queries per run.
-m SELECT_MODE, --select_mode=SELECT_MODE Selection algorithm to use (weighted, random, chunk)
-s NUM_SERVERS, --num_servers=NUM_SERVERS Number of nameservers to include in test
-S, --system_only Only test current system nameservers.
-w, --open_webbrowser Opens the final report in your browser
-u, --upload_results Upload anonymized results to SITE_URL (False)
-U SITE_URL, --site_url=SITE_URL URL to upload results to (http://namebench.appspot.com/)
-H, --hide_results Upload results, but keep them hidden from indexes.
-x, --no_gui Disable GUI
-C, --enable-censorship-checks Enable censorship checks
-6, --ipv6_only Only include IPv6 name servers
-O, --only Only test nameservers passed as arguments
"""

