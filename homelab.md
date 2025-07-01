# Homelab
Updated 07/01/2025

## Equipment
- 18U StarTech server rack ([Amazon](https://a.co/d/7RQkPYP))
- [1U Ubiquity Dream Machine Pro](#1u-ubiquity-dream-machine-pro) ([UniFi](https://store.ui.com/us/en/products/udm-pro))
- 1U ADJ 8 Outlet Toggle Switch PDU ([Amazon](https://a.co/d/dcRt736))
- 1U 8 Outlet Startech PDU ([Amazon](https://a.co/d/hr3ytrX))  
- [4U Silverstone RM44 Chassis](#4u-silverstone-rm44-chassis) ([Amazon](https://a.co/d/aNcRnCz))  
- [2U Dell PowerEdge R730XD](#2u-dell-poweredge-r730xd) ([New Server Life](https://newserverlife.com/configure/dell_poweredge_r730xd_12lff_2sff/))
- [1U Supermicro SYS-6016T-NTF](#1u-supermicro-sys-6016t-ntf) ([Newegg](https://www.newegg.com/supermicro-sys-6016t-ntrf-supports-up-to-two-intel-64-bit-xeon-processor-of-the-same-type-below-in/p/N82E16816101261))
- 2U CyberPower PSU ([Amazon](https://a.co/d/4aGn8KZ)) 

---

## 1U Ubiquity Dream Machine Pro

Entrypoint into my network. I have teleport setup so I can access my network from anywhere. DNS server, adblocker, region blocking, firewall, network analytics, and future NVR for cameras.

---

## 4U Silverstone RM44 Chassis

Gaming PC with Windows 11 as my daily driver.

Specs:
- Ryzen 7 5800X
- RTX 3080Ti
- 128GB DDR4

---

## 2U Dell PowerEdge R730XD

My most recent addition that has already turned into my work horse running TrueNAS.

Specs:
- 2x Xeon E5-2660 v4 @ 2.00GHz (56 total cores)
- 128GB DDR4 (ECC)
- 32TB Usable (RaidZ2)

Current Docker Apps:
- [Nginx Proxy Manager](https://nginxproxymanager.com/)
    - Local reverse proxy to route all traffic to proper destinations. Combined with my Dream Machine Pro, its super easy for me to add local subdomains that point to a local IP and port.
- [Jenkins](https://www.jenkins.io/)
    - Just started getting into this as my automation for app builds. Replacing my old VM method on my Supermicro Proxmox. I have a LOT of different projects in Rust/Python that have multiple target releases. MacOS, Windows, Debian/Fedora...
- [WeTTY](https://butlerx.github.io/wetty/#/)
    - Web terminal in a stripped down clean environment for a universal NeoVim setup. Has access to my project files for remote programming wherever I am with whatever hardware I'm on. Simple startup.sh script that rebuild the clean environment on container restarts.
- [Linkding](https://linkding.link/)
    - Fantastic bookmark service. Allows me to easily sort and search my ever growing list of bookmarks. It is also super customizable via CSS.
- [Plex](https://www.plex.tv/)
    - Local "streaming service" of my local media. Currently I don't have a GPU in this machine, but CPU is handling the traffic just fine for 1080p.
- [MakeMKV](https://www.makemkv.com/)
    - Web interface of MakeMKV for ripping local media such as DVDs. Took a while to land on a solution that I could use with this machine and am happing with this [image](https://github.com/jlesage/docker-makemkv)
- [FileBrowser](https://filebrowser.org/)
    - Easy web interface for multi-user dropbox style file storage. Create a TrueNAS user, send them a Teleport link and the local address - BOOM, easy!
- [Dell Fan Controller](https://github.com/tigerblue77/Dell_iDRAC_fan_controller_Docker)
    - The R730XD does not play well with my non Dell NIC, so this allows me to customize the fan speed / desired temp. Without this running the machine absolutely RIPS and is way to loud for being near my desk.

Future:
- [Immich](https://immich.app/)
    - I don't feel 100% confident using this app yet, but when it gets closer to stable I absolutely will. This will further help me decouple from paying for another service. (Google Photos alternative)

---

## 1U Supermicro SYS-6016T-NTF

My Supermicro 1U is getting pretty outdated so I use it for a Proxmox setup with VMs of things that I don't need to run all the time, or im okay with running "slow". A lot of its main use was as a build machine for projects, but as im migrating to Jenkins, this might just get used as my local AI machine.

Current VMs:
- Ubuntu 
    - Mainly for playing around but also acts as a build machine for Debian based apps.
- Windows 11
    - For my Editor/Game im building in Rust this acts as a client so I can test multiplayer with.
- Fedora
    - For building apps on non Debian linux. 
- Ubuntu
    - Minecraft server.
- Open Mandriva
    - Playing around.
- Ubuntu
    - Ollama and Open WebUI.
- TrueNAS
    - Testing purposes that isn't my main deployment (R730XD).
- MacOS
    - Building apps for Mac.

---

![18UU Rack Setup](./assets/rack.jpg "Rack Image")
