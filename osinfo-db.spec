%global debug_package %{nil}

Name: osinfo-db
BuildArch: noarch
Epoch: 100
Version: 2021.12.16
Release: 1%{?dist}
Summary: osinfo database files
License:  GPL-2.0-or-later
URL: https://gitlab.com/libosinfo/osinfo-db/-/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: intltool
BuildRequires: osinfo-db-tools
Requires: hwdata

%description
The osinfo database provides information about operating systems and
hypervisor platforms to facilitate the automated configuration and
provisioning of new virtual machines

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%install
osinfo-db-import  --root %{buildroot} --dir %{_datadir}/osinfo osinfo-db.tar.xz

%files
%dir %{_datadir}/osinfo
%{_datadir}/osinfo/VERSION
%{_datadir}/osinfo/LICENSE
%{_datadir}/osinfo/datamap
%{_datadir}/osinfo/device
%{_datadir}/osinfo/os
%{_datadir}/osinfo/platform
%{_datadir}/osinfo/install-script
%{_datadir}/osinfo/schema

%changelog
