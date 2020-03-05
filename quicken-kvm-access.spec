%define  debug_package %{nil}

Name:		quicken-kvm-access
Version:	1.0.0
Release:	1%{?dist}
Summary:	Remote access to my KVM domain that's running Quicken
Source0:	%{name}-%{version}.tar.gz
License:	MPL
URL:		https://github.com/dlk3/quicken-kvm-access
BuildArch:	x86_64

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
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -m 644 -t %{buildroot}%{_datadir}/icons/hicolor/48x48/apps quicken-kvm-access.png

%files
%license LICENSE
%{_bindir}/quicken-kvm-access
%{_datadir}/applications/quicken-kvm-access.desktop
%{_datadir}/icons/hicolor/48x48/apps/quicken-kvm-access.png

%changelog
* Thu Mar 5 2020 David King <dave@daveking.com> - 1.0.0-1
	Initial Version
