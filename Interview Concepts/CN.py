# This conatains some of the important questions that can be asked in the interviews

'''1. What layer of OSI handles routing?'''
# Routing of packets in the network is taken care by network layer. It also does the logical addressing.

'''Important Notes(OSI model):'''
# 1.Application Layer: User Interface
# 2.Presentation Layer: Encryption/data format
# 3.Session Layer: Session management by connecting to the server
# 4.Transport Layer: End-to-end Delivery, ports allocation for communication,etc

# 5.Network Layer: Routing the data pakets and also logical IP addressing and path determination for packets are decided here
# Path determination algorithms are:
# a.Link state routing(uses Dijstras Algorithm)Ex:Open-short-path-first
# b.Distance vector routing(Bellman-Ford)Ex:Routing Information Protocol

# 6.DataLink Layer: MAC Addressing takes place here
# 7.Physical Layer: Bits manipulation and low level taks takes place here on wire



'''Computer Network(1/7)'''
# It is collection of devices which communicate with each other with some agreed upon rules called protocols

# Your Laptop--Wi-Fi-->Router--ISP-->Internet->Google Server
# When we open the google.com then there are many things happening inside it like searching google.com, resolving ip address, how to transport securely, where to send data.
# So in order to make all these functionalities we implement entire internet in 7 layers (OSI) instead of single layer as it could get big and hard to manage.

##Note:
# Network types:
#a.PAN(Personal Area Network): Very small range(Bluetooth)
#b.LAN(Local Area Network): Network covering small geographical area.(College lab, Home network)
#c.MAN(Metropolitan Area Network): Larger than LAN and coverse more regions(Like Whole city)
#d.WAN(Wide Area Network): Network over large geographical areas.(Internet)

# ->Network: Collection of connected devices
# ->Internet: Interconnected of large network of Networks(Internet=Network+Network+Internet)


'''OSI(Open system Interconnection)'''
# Here each layer takes care of one fucntionality and execute it perfectly.
# It is a theoritical/conceptual model just to learn how the internet works. The rea working looks like the TCP/IP model.
## Layers:
# 7. Application    ->HTTP,DNS,SMTP,FTP,websockets (Application level networking protocols)
# 6. Presentation   ->Data encryption, encoding,compression, (how it presents)
# 5. Session        ->Establishing, maintaining, terminating sessions (Manages sessions)
# 4. Transport      ->TCP,UDP (Provides communication between processes/applications)
# 3. Network        ->IP(IPv4-32bits/IPv6-128bits), routing(routers), packet forwarding(It's job is to deliver the packets between networks)
# 2. Data Link      ->Ethernet, ARP, RARP. IT uses addresses such as MAC to send packets between routers. Switches operate here more
# 1. Physical       ->Here everything is tranferred in the form of electrical signals in copper or radio waves in wifi in 0 and 1 formats

'''Each Layer cooperate with each other and make the use of services provide by layers below it and it provides services to the layers above it'''

# Step-by-Step Delivery Pipeline
# Incoming Packet at Router:(Intelligent Router)
# Router reads the Destination IP (10.0.2.3).
# Checks its Routing Table to see which physical LAN Interface leads to 10.0.2.0/24.
# Checks its ARP Table for 10.0.2.3 to find its MAC address (CC:CC:CC:CC:CC:CC).
# Rewrites the Layer 2 header: Sets Destination MAC = CC:CC:CC:CC:CC:CC and Source MAC = Router's LAN MAC.
# Sends the frame out of its LAN port down the cable to the switch.

# Incoming Frame at Switch:(Dumb switch)
# Switch receives the frame on Port 1.
# Reads ONLY the Destination MAC (CC:CC:CC:CC:CC:CC) at the start of the frame.
# Looks up its MAC Address Table: CC:CC:CC:CC:CC:CC is on Port 3.
# Delivers the frame directly out of Port 3 to the target device without touching or reading the IP header inside.

# ->Switches: Sit inside local networks (LANs), connecting local devices through wifi while 
# ->Routers: Sit at the borders between networks, connecting your local LAN to your Internet Service Provider (ISP) and routing data across different subnets worldwide.

'''TCP/IP model'''
#It is the practical model which is used outside for the Internet(4 layers)
# OSI                         TCP/IP

# Application ─┐
# Presentation ├──→ Application
# Session ─────┘

# Transport ─────────→ Transport

# Network ───────────→ Internet

# Data Link ──┐
# Physical ───┴──────→ Network Access

# The Encapsulation is done so that each work on their own data and give services to others

''' Key Concepts Learned'''
# IP Address (Layer 3 - Network): Logical address that routes data across different networks toward a destination host.
# MAC Address (Layer 2 - Data Link): Permanent, 48-bit hardware identifier (281+ trillion global combinations) that directs physical signals (radio/electricity/light) locally between adjacent hardware interfaces.
# 5-Tuple: Unique connection identity: (Source IP, Source Port, Destination IP, Destination Port, Protocol).
# Ports: Transport-layer endpoints. Common/well-known ports (80, 443) listen on servers, while client OS kernels dynamically assign Ephemeral Ports (49152–65535) from an internal socket table to keep concurrent app streams separate.
# WebSockets: Upgrades an existing HTTP/HTTPS connection into a persistent, full-duplex bi-directional channel with low header overhead (2–10 bytes).
# Flow Control: Receiver-driven protection mechanism preventing a fast sender from flooding a slow receiving host buffer using the Receive Window (rwnd).
# Congestion Control: Network-driven protection mechanism preventing a sender from overloading intermediate router queues using the Congestion Window (cwnd).


# [ Incoming Data Stream ] What happens when the packets are being lost by the device or by the network routers due to excess buffers overload
#           |
#           +---> Receives `rwnd = 0` in ACK Header? 
#           |       └─> [PAUSE TRANSMISSION] (Flow Control: Wait for receiver buffer to open)
#           |
#           +---> Receives 3 Duplicate ACKs (e.g., `ACK 11`)?
#           |       └─> [SCENARIO A: MODERATE CONGESTION] (1-2 packets lost in queue)
#           |             1. Fast Retransmit missing packet immediately.
#           |             2. Cut `cwnd` in HALF (Multiplicative Decrease).
#           |             3. Switch to Linear Growth (`cwnd + 1` per RTT).
#           |
#           +---> Retransmission Timer Expires (Timeout)?
#                   └─> [SCENARIO B: SEVERE CONGESTION] (Router queue full, mass drop)
#                         1. Retransmit missing packet.
#                         2. Drop `cwnd` back to 1 (Multiplicative Cut).
#                         3. Restart Slow Start (Exponential Growth: double `cwnd` per RTT).

# Note: rwnd is receive window buffer and the cwnd is the congestion window buffer.

'''Segment vs Packet vs Frame'''
# The data which comes from application is encapsulated with other header by Transport layer and the whole portion is called a segment
# Segment = TCP Header + Application Data

# The data which comes from TCP layer is encapuslated with other header by Network layer and the whole portion is called the packet
# Packet = IP Header + TCP Segment

# The data which comes from the Network layer is encapsulated with other 2 headers by Data link layer and the whole portion is called ethernet frames
# Frame = Ethernet Header + IP Packet + Trailer

# +------------------+------------------+---------------+----------------+-----------------+
# | Destination MAC  |    Source MAC    |   EtherType   | Payload / Data | Frame Check     |
# |   (6 Bytes)      |    (6 Bytes)     |   (2 Bytes)   | (IP Packet)    | Sequence (FCS)  |
# +------------------+------------------+---------------+----------------+-----------------+
# |<---------------------- FRAME HEADER ----------------->|                | FRAME TRAILER  |

# Trailer is for checking whether the bits were corrupted during transmission.
# The EtherType is for knowing whether the IP is IPv4 or IPv6


'''While Moving from one router to other router removes the data frame and see the dest ip and then packs it with its own frame and send to other router(Hop)'''
# So, the MAC changes when travelling and the IP's remain same from start to end
# The Ip address changes every time we connect to the internet but the MAC addresses are permanent


'''Ports: It identifies a transport layer endpoint associated with a process/service'''
# If there are many applications and there are all connected to google then when google want to send data to a particular application then it sends to the port to which it is connected
# Some dedicated ports are : 80:http, 443: https, 22:ssh

'''Web sockets vs Persistent TCP'''
# Persistent HTTP (Keep-Alive):
# Client  --- [HTTP GET Request] --->  Server
# Client  <--- [HTTP Response]  ---  Server
# (Connection stays open, but Server CANNOT send data until Client asks again!)

# WebSocket:
# Client  --- [HTTP Upgrade Handshake] --->  Server
# Client  <--- [101 Switching Protocols] --- Server
#    ||                                       ||
#    || <== Real-time Full-Duplex Tunnel ==>  ||
# Client  <======== [Data Frame] =========>  Server (Server can push ANY time!)


# ****Note Very Important****:
# See when our computer want to sends a request it generally sends through our ip only but it chooses a unique port which is available in system given by os. As the receiver while sending back responce must identify which port it belongs to.
# Connection = (Source IP, Source Port, Destination IP, Destination Port, Protocol)
# So, always the any one of these will be different for different connections

# MAC address: Used primarily for local network delivery.(Switches uses this)
# IP address: Used for logical addressing and routing between networks.(Routers uses this)

