========
Homelab
========

*Last updated: November 21, 2025*

I started my homelab about 2 years ago with a Raspberry Pi 5 running Ubuntu and 2 external 5TB drives. From there I bought an 8U StarTech rack and Dream Machine Pro. The 8U rack was quickly filled and about a year later I upgraded to an 18U rack which is currently what I'm running with.

**Quick Links:** `PDU Toggle Switch Layout <https://docs.google.com/spreadsheets/d/1-5ZaVzM2TA5GnljXQbx04h1sIoWHmQHqI64W5m31yuI/edit?usp=sharing>`_

----

Hardware Overview
==================

**Infrastructure**

- 18U StarTech Server Rack (`Amazon <https://a.co/d/7RQkPYP>`__)
- ADJ 8 Outlet Toggle Switch PDU (`Amazon <https://a.co/d/dcRt736>`__)
- 8 Outlet StarTech PDU (`Amazon <https://a.co/d/hr3ytrX>`__)
- CyberPower UPS (`Amazon <https://a.co/d/4aGn8KZ>`__)

**Network**

- `Ubiquiti Dream Machine Pro`_ (`UniFi <https://store.ui.com/us/en/products/udm-pro>`__)

**Compute**

- `Dell PowerEdge R730XD`_ - TrueNAS server
- `Supermicro SYS-6016T-NTF`_ - Proxmox VM host
- `Silverstone RM44 Chassis`_ - Gaming PC/Daily driver

----


Ubiquiti Dream Machine Pro
===============================

Network gateway with Teleport for remote access. Handles DNS, ad-blocking, region filtering, firewall, and network analytics. Planning to add NVR for security cameras.


Silverstone RM44 Chassis
=============================

**Windows 11 Gaming PC & Daily Driver**

.. admonition:: Components

  - AMD Ryzen 7 5800X
  - NVIDIA RTX 3080Ti
  - 128GB DDR4


Dell PowerEdge R730XD
=========================

**Primary TrueNAS Server**

My workhorse running TrueNAS for storage and Docker app deployment.

.. admonition:: Components

   - 2x Xeon E5-2660 v4 @ 2.00GHz (56 cores total)
   - 128GB DDR4 ECC
   - 32TB usable (RaidZ2)

.. raw:: html

   <details>
      <summary>Docker Apps</summary>

**Deployed**

- `Excalidraw <https://excalidraw.com/>`_ - Whiteboard for brainstorming
- `WeTTY <https://butlerx.github.io/wetty/#/>`_ - Web-based terminal with NeoVim for remote development
- `Linkding <https://linkding.link/>`_ - Bookmark manager with custom CSS support
- `FileBrowser <https://filebrowser.org/>`_ - Multi-user web-based file storage
- `Ollama <https://ollama.com/>`_ - Local LLM hosting
- `Open WebUI <https://openwebui.com/>`_ - Interface for Ollama models
- `Meshtastic <https://client.meshtastic.org/>`_ - Meshtastic device client
- `Plex <https://www.plex.tv/>`_ - Local media streaming
- `MakeMKV <https://www.makemkv.com/>`_ - Media ripping (`docker image <https://github.com/jlesage/docker-makemkv>`__)
- `Nginx Proxy Manager <https://nginxproxymanager.com/>`_ - Reverse proxy for local subdomain routing
- `Dell Fan Controller <https://github.com/tigerblue77/Dell_iDRAC_fan_controller_Docker>`_ - Custom fan curves for non-Dell hardware compatibility

**Planned Additions**

- `Jenkins <https://www.jenkins.io/>`__ - Build automation for Rust/Python projects across multiple platforms (MacOS, Windows, Debian, Fedora)
- `Immich <https://immich.app/>`__ - Google Photos alternative (waiting for stable release)

.. raw:: html

   </details>


Supermicro SYS-6016T-NTF
=============================

**Proxmox VM Host**

Older 1U server running Proxmox for virtualization. Handles development VMs and services that don't need to run 24/7.

.. raw:: html

   <details>
      <summary>️Virtual Machines</summary>

- **Ubuntu** - General testing & Debian-based app builds
- **Fedora** - Non-Debian Linux builds
- **Windows 11** - Multiplayer client testing for Rust game/editor
- **MacOS Sierra** - Mac app builds
- **Ubuntu** - Minecraft server
- **TrueNAS** - Testing deployment
- **OpenMandriva** - Experimentation

.. raw:: html

   </details>

----

Media
=====

.. raw:: html

   <details>
      <summary>Rack Photos</summary>

**Current 18U Setup**

.. image:: ./static/rack.jpg
   :alt: Current 18U Rack Setup
   :align: center
   :width: 80%

**Original 8U Setup**

.. image:: ./static/rack_old.jpg
   :alt: Old 8U Rack Setup
   :align: center
   :width: 80%
  
.. raw:: html

   </details>