# mininet_topo
adventures in mininet simulated network topology land with testing

Testing tools we used:

iperf 
ping
wireshark 
ovs-ofctl

Tests: 
0. mininet>iperf
1. Ideal window size with low congestion (50%)
   -Default: 85.3
   -130k
   -200k
   -300k
   -500k
2. Ideal window size high congestion (100%)
   (see above/below)
3. Actual bandwidth at each layer w/ IDEAL WINDOW SIZE TUNING 
   - h1: iperf -s
   - h2: iperf -c 10.0.0.2
   - h1: iperf -s -w 130k (buffer size--default 85.3)
   - h2: iperf -c 10.0.0.2 -w 130k
4. RTT h1 ping -c3 h2 //send 3 packets
5. Transfer time h1 ping -c3 h2 
6. MTU

