%define  debug_package %{nil}

Name:		quicken-kvm-access
Version:	1.0.0
Release:	1%{?dist}
Summary:	Remote access to my KVM domain that's running Quicken
Source0:	%{name}-%{version}.tar.gz
License:	MPL
URL:		https://github.com/dlk3/quicken-kvm-access
BuildArch:	noarch

Requires: 	libvirt-client
Requires: 	rdesktop
Requires:	gtk-update-icon-cache
Requires:	libnotify

%description
Connect to the desktop of the KVM on my home network where Quicken runs

%prep
%setup

%install
umask 0022
mkdir -p %{buildroot}%{_bindir}
install -m 755 -t %{buildroot}%{_bindir} quicken-kvm-access
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 -t %{buildroot}%{_datadir}/applications quicken-kvm-access.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 644 -t %{buildroot}%{_datadir}/icons/hicolor/256x256/apps quicken-kvm-access.png
mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 quicken-kvm-access.conf.sample %{buildroot}%{_sysconfdir}/quicken-kvm-access.conf

%files
%license LICENSE
%{_bindir}/quicken-kvm-access
%{_datadir}/applications/quicken-kvm-access.desktop
%{_datadir}/icons/hicolor/256x256/apps/quicken-kvm-access.png
%config %{_sysconfdir}/quicken-kvm-access.conf

%post
[ -f %{_datadir}/icons/hicolor/icon-theme.cache ] && %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor -q
exit 0

%postun
[ -f %{_datadir}/icons/hicolor/icon-theme.cache ] && %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor -q
exit 0

%changelog
* Thu Mar 5 2020 David King <dave@daveking.com> - 1.0.0-1
	Initial Version
