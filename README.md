# Kathara-Labs-Network-Virtualization
This repository contains a collection of Kathará network scenarios for testing the tunnel GRE, IPSec implemented with [strongSwan](https://www.strongswan.org/) and [OpenVPN](https://openvpn.net/).

## Pre-Requisites

1. To run the network scenarios you need to install the Kathará network emulator (support for all the OSes). 
You can follow the official [installation guide](https://github.com/KatharaFramework/Kathara/wiki/Installation-Guides).
2. You need to build the Docker strongSwan image or pull it from Docker Hub.
```shell
docker build -t loriringhio97/strongswan:latest dockerfile/
```

## Network Virtualization Scenarios
The `labs` directory contains network scenarios that explain overlay networks:
- [Base scenario](labs/0_base_topology): a simple network scenario composed by two hosts and two routers with static routing configured and with wireshark GUI available at [http://localhost:3000/](http://localhost:3000/). All the following labs are built on top the base scenario.
- [Tunnel GRE](labs/1_tunnel_GRE): a network scenario to test a tunnel GRE in which IP packets are encapsulated within IP directly.
- [IPSec Host-Host ESP transport mode](labs/2_IPSec_Host-Host_transport): a network scenario to test IPSec Encapsulating Security Payload (ESP) protocol in transport mode in which the Security Association is created between two end hosts.
- [IPSec Host-Host ESP tunnel mode](labs/3_IPSec_Host-Host_tunnel): a network scenario to test IPSec Encapsulating Security Payload (ESP) protocol in tunnel mode in which the Security Association is created between two end hosts.
- [IPSec Net-Host ESP tunnel mode](labs/4_IPSec_roadwarrior_tunnel): a network scenario to test IPSec Encapsulating Security Payload (ESP) protocol in tunnel mode in which the Security Association is created between a gateway and a host.
- [IPSec Net-Net ESP tunnel mode](labs/5_IPSec_Net-Net_tunnel): a network scenario to test IPSec Encapsulating Security Payload (ESP) protocol in tunnel mode in which the Security Association is created between two gateways.
- [OpenVPN](labs/6_OpenVPN_Roadwarrior): a network scenario to test OpenVPN client/server (Road warrior).

## Resources
In the following you can find some links to useful resources:
- [Kathará Official Website](https://www.kathara.org/)
- [Kathará Repository](https://github.com/KatharaFramework/Kathara)
- [strongSwan Official Website](https://www.strongswan.org/)
- [strongSwan KVM Tests](https://www.strongswan.org/testing/testresults/index.html)
- [OpenVPN Official Website](https://openvpn.net/)