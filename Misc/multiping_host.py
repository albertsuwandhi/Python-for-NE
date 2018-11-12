from multiping import multi_ping
address = ["10.8.32.10","10.8.32.200","8.8.8.8","www.detik.cm"]
responses, no_responses=multi_ping(address, timeout=2, retry=3)
print(responses)
print(no_responses)
