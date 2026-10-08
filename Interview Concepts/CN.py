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


'''Switch vs Hub'''
# Switch forwards intelligently using MAC address(Layer 2) Using Mac lookup table(MAC->Port No)
# Hub broadcasts incoming data to all ports(Physical layer) Dumb way to send

# Our computer gets the Ip address of the home router when it is connected to that and when it wants to send some data it check whether the dest ip is within the network or outside. If outside then our computer asks who has this ip then 
#- our home router answers with its mac address, Now our computer packs teh data with a frame and place the dest mac to our home router default gateway.
# Our computer uses ARP(Address Resolution Protocol) to covert the IP->MAC. ANd it also has the arp cache so that it can use it when needed for the next time, without performing arp again.

### Note: ARP only works for IPv4. IPv6 uses the NDP(Neighbor Discovery Protocol) for this task.
# We do not need any to know the final destination's mac address. We only need to know Final dest IP and also next HOP's MAC address(Found by IP by ARP)
# Each router has 2 tables one is What should be next HOP Ip address to reach final IP add(Routing table) and then it sees the MAC address related to the IP to send next(ARP cache)

'''IP(Internet Protocol): IPv4, IPv6'''
# IP primary responsibilities are: logical addressing, packet forwarding and routing through network
# Ip is connectionless, best effort, does not gurantee delivery or ordering of packets or any retransmit of lost packets
# So, thats's why we have TCP up on the IP to look after all the remaining  needs.

# Therefore, IP-> addressing + routing, TCP-> reliability

'''IPv4(32bits addresses)'''
# Ex: 192.168.1.10 ->4 decimal Octets(Each octet is from 0-255) Decimal notations 
# Address structure:  ->Divided in to 2 portions
# Network portion | Host portion  -> The boundary is determined by the Subnet mask/prefix length(New style)
# Ex: 192.168.1.10/24 ->24bits is given to Network and 8 bits to host

# The process of dividing by the number /24(Prefix length) is new architectue. FOr old one there are 5 classes and each class has already predefined network and host bits.see in dox

'''Private IPv4 Address'''
# This is one of the way which we can use to counter less number of IP's.
# Idea is like there will be some private addresses and are only intended for internal networks and are not directly routable acorss public
#  10.0.0.0/8   172.16.0.0/12   192.168.0.0/16->For home addresses
# These are present in many homes identical but upon these there will be a public IP which is routed in public instead of it. It maps to many devices with the private IP's

# Note: the conversion of private and the public is done by the default gateway router by using the NAt(Network Addressing Translator)
# Private devices(Many devices and many private IP's)
#       ↓             ->Private Ip used inside the private network
#    Router/NAT
#       ↓
#  Public IP          ->These are used globally for communication
#       ↓
#    Internet


'''IPv6(128bits addresses)'''
# Ex: 2001:db8::1 (Hexadecimal notation)

'''# | IPv4 | IPv6 |
# | 32-bit | 128-bit |
# | Decimal notation | Hexadecimal notation |
# | Limited address space | Extremely large address space |
# | ARP(Address resolution protocol) | NDP(Neighbor Discovery Protocol) |
# | Broadcast exists | No traditional broadcast(Anycast is there) |'''



'''Subnetting'''
# Subnetting divides an IP network into smaller logical networks by taking the host bits and convert to the Network bits
# The hosts per network decreases but he no. of networks increases thats why its called subnetting.

# Total addresses = 2^(32 - prefix)=256 ->The prefix is 24 (in /24)
# if we take 2 bits and add them to network then the total network bit becomes 26 so,
# 2^(32-26)=64 See the 256 is divided in to 4 parts with 64 hosts each.
# Usable hosts = total addresses - 2  -> as 1 for network IP(first bit is 0) and other for broadcating IP(last bit is 1)
# Now, for /26=> 64 - 2 = 62 usable hosts ->Here /24 is bigger network and /26 is smaller network


'''CIDR(class less Inter-Domain Routing)'''
# The process of using the prefix Notations /24 or /26 is this thing instead of using fixed classes this is better because:
#1. SOlves less Ip addresses things
#2. give exact amount of ips for users when asked instead of giving many additional ip's (in classes)


''' 1.Default Gateway: A host needs to know where to send traffic destined outside its local subnet.That device is called default gateway. This is immediately the first router(home router) to send data to.'''
# How our device or host decide the dest ip is inside the network or outside?
# => We take the subnet mask and then perform bitwise and on both the local ip address(host one) and the dest ip. If both are same then same network otherwise differnt.
# Subnet mask is got like: for /26: 11111111 11111111 11111111 11000000 ->see 26 1's and other 0's
# Now if we calculate it will be 255.255.255.192 ->Subnet mask

# If the dest ip is same as that of device then it sends packet through the switch otherwise it sends to default router by adding a frame around it by the routers mac address as dest mac.


'''Routing'''
# Which path/next hop should a packet take toward its destination network?
# Routers maintain routing tables. => (dest-IP ->next hop Ip/Interface)


### Some Important points:
# -> Longest prefix match: A router may have multiple matching routes. It chooses the route with the longest matching prefix. max digits must match
# If no such matches then he default route is commonly represented as: (0.0.0.0/0)
# -> NAT(Netwrok Address Translation): Converts the Ip address to the mac addres by asking the neighbours by broadcating the Ip and getting the response
# Laptop(192.168.1.10:50000) -> NAT -> Public IP(203.x.x.x:40001)
# -> PAT / NAT Overloading: Port Address translation: In private networks there are many devices so, they share the same IPv4, so the router must distinguish all devices by using the ports.
# SO, private ip <=> public ip  ->NAT
# and private ip <=> port no  ->PAT
# NAT is very useful because it brings the concepts of private networks and make more and more devices use same public ip. So, it solves less ip problem and all devices do not require seperate public ipv4
#*****  NAT!=Firewall  ->The NAT may also implement firewall rules, but NAT itself is address/port translation


'''| Switch | Router |
|---|---|
| Primarily Layer 2 | Primarily Layer 3 |
| Uses MAC addresses | Uses IP addresses |
| Connects devices/networks within local topology | Connects different IP networks |
| Maintains MAC table | Maintains routing table |
| Forwards frames | Forwards packets |'''


'''How routing of packets and frames happen(Journey):'''
# 1. If MAC matches Router:
#    Strip Layer 2 -> Read Layer 3 IP -> Routing Table -> ARP Cache -> Rewrite MACs -> Forward out.
# 2. If MAC DOES NOT match Router:
#    The router drops the packet immediately.
# 3. If a Switch gets a frame:
#    It reads the Destination MAC, checks its MAC Address Table, and forwards the frame out the matching port.


"""
[ LAPTOP ]
  │
  ├─► Builds IP Packet: [Src IP: 192.168.1.10 | Dest IP: 10.0.2.5]
  ├─► Bitwise AND check shows Dest IP is outside local subnet.
  ├─► Checks *****ARP Cache for Gateway IP (192.168.1.1) -> MAC: R1-MAC
  └─► Wraps frame: [Src MAC: Laptop-MAC | Dest MAC: R1-MAC]
        │
        ▼
[ SWITCH 1 (Layer 2) ]
  │
  ├─► Reads ONLY Destination MAC (R1-MAC).
  ├─► Checks ****MAC Address Table: R1-MAC is on Port 4.
  └─► Forwards frame OUT Port 4 untouched (Does NOT read IP header or change MACs).
        │
        ▼
[ ROUTER (Layer 3) ]
  │
  ├─► Destination MAC matches Router MAC?
  │     ├── NO  ──► [ DROP PACKET IMMEDIATELY ]
  │     └── YES ──► Strips Layer 2 header.
  │
  ├─► Reads Destination IP (10.0.2.5).
  ├─► Searches *****Routing Table -> Next-Hop IP: 10.0.2.5 on Interface LAN-2.
  ├─► Searches ARP Cache for 10.0.2.5 -> MAC: Server-MAC.
  ├─► Rewrites Layer 2 header: [Src MAC: Router-LAN2-MAC | Dest MAC: Server-MAC].
  └─► Forwards new frame out Interface LAN-2.
        │
        ▼
[ SWITCH 2 (Layer 2) ]
  │
  ├─► Reads Destination MAC (Server-MAC).
  ├─► Checks MAC Address Table: Server-MAC is on Port 2.
  └─► Forwards frame OUT Port 2 untouched.
        │
        ▼
[ SERVER ]
  │
  └─► Destination MAC matches Server MAC -> Strips Layer 2 -> Processes IP Packet!"""