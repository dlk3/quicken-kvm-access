# Quicken KVM Access

A script that establishes a session on my laptop with a Quicken/Windows 10 KVM
that's running remotely on my main desktop computer.  I use this when I'm travelling and
need secure access back to my Quicken application.

Variables must be configured properly in /etc/quicken-kvm-access.conf in order for
this script to function.

Installation packages are available in this project's Fedora COPR repository:
```
$ sudo dnf copr enable dlk/rpms
$ sudo dnf install quicken-kvm-access
```
Configuration Notes:

* The Windoes system running in the KVM needs to have an IP address on a
network you can access.  My firewall router supports OpenVPN which allows
me to establish a VPN connection from the public internet where my laptop
is to my home network behind the firewall.  

* The Windows KVM is configured with bridged networking instead of the
default NAT configuration so that it has its own IP address on my home
network.

* The Windows system running in the KVM is configured to accept Remote Desktop
sessions.  See https://support.microsoft.com/en-us/help/4028379/windows-10-how-to-use-remote-desktop
