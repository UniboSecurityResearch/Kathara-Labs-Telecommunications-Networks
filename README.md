# Kathara Labs Telecommunications Networks 
This repository contains a collection of Kathará network scenarios used in the courses of Telecommunications Networks by professor Franco Callegati at the University of Bologna.

## Pre-Requisites
To run the network scenarios you need to install the Kathará network emulator (support for all the OSes). 
You can follow the official [installation guide](https://github.com/KatharaFramework/Kathara/wiki/Installation-Guides).

## Overlay Networks labs
The `labs_Overlay_Networks` directory contains network scenarios that explain overlay networks, in particular for testing the tunnel GRE, IPSec implemented with [strongSwan](https://www.strongswan.org/) and [OpenVPN](https://openvpn.net/):
- [Base scenario](labs_Overlay_Networks/0_base_topology): a simple network scenario composed by two hosts and two routers with static routing configured and with wireshark GUI available at [http://localhost:3000/](http://localhost:3000/). All the following labs are built on top the base scenario.
- [Tunnel GRE](labs_Overlay_Networks/1_tunnel_GRE): a network scenario to test a tunnel GRE in which IP packets are encapsulated within IP directly.
- [IPSec Host-Host ESP transport mode](labs_Overlay_Networks/2_IPSec_Host-Host_transport): a network scenario to test IPSec Encapsulating Security Payload (ESP) protocol in transport mode in which the Security Association is created between two end hosts.
- [IPSec Host-Host ESP tunnel mode](labs_Overlay_Networks/3_IPSec_Host-Host_tunnel): a network scenario to test IPSec Encapsulating Security Payload (ESP) protocol in tunnel mode in which the Security Association is created between two end hosts.
- [IPSec Net-Host ESP tunnel mode](labs_Overlay_Networks/4_IPSec_roadwarrior_tunnel): a network scenario to test IPSec Encapsulating Security Payload (ESP) protocol in tunnel mode in which the Security Association is created between a gateway and a host.
- [IPSec Net-Net ESP tunnel mode](labs_Overlay_Networks/5_IPSec_Net-Net_tunnel): a network scenario to test IPSec Encapsulating Security Payload (ESP) protocol in tunnel mode in which the Security Association is created between two gateways.
- [OpenVPN](labs_Overlay_Networks/6_OpenVPN_Roadwarrior): a network scenario to test OpenVPN client/server (Road warrior).

## VLAN labs
The `labs_VLAN` directory contains network scenarios that explain how VLAN and VLAN tagging 802.1Q​ works:
- [ TODO ]

## Resources
In the following you can find some links to useful resources:
- [Kathará Official Website](https://www.kathara.org/)
- [Kathará Repository](https://github.com/KatharaFramework/Kathara)
- [strongSwan Official Website](https://www.strongswan.org/)
- [strongSwan KVM Tests](https://www.strongswan.org/testing/testresults/index.html)
- [OpenVPN Official Website](https://openvpn.net/)