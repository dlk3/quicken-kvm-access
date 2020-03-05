# Quicken KVM Access

A script that establishes a session on my laptop with a Quicken/Windows 10 KVM
that's running remotely on my main desktop computer.  I use this when I'm travelling and
need secure access back to my Quicken application.

Variables mush be set properly at the top of the /usr/local/bin/quicken file
in order for this to work properly.

Installation packages are available in this project's Fedora COPR repository:
```
$ sudo dnf copr enable dlk/quicken
$ sudo dnf install quicken
```
Configuration Notes:

* The Windoes system running in the KVM needs to have an IP address on a
network you can access.  My firewall router supports OpenVPN which allows
me to establish a VPN connection from the public network to my home network
behind the firewall.  

* The Windows KVM is configured with bridged networking so that it has its
own IP address on my home network.  

* The Windows system running in the KBM is configured to accept Remote Desktop
sessions.  See https://support.microsoft.com/en-us/help/4028379/windows-10-how-to-use-remote-desktop

