%define osname centos
%define arch noarch 

Summary: Virtualmin release file and package configuration for Virtualmin Pro
Name: virtualmin-release
Version: 6.0
Release: 3.%{osname}
License: Copyright 2005-2017 Virtualmin, Inc.
Group: System Environment/Base
Source0: RPM-GPG-KEY-webmin
Source1: RPM-GPG-KEY-virtualmin
Source2: RPM-GPG-KEY-virtualmin-6
Source10: virtualmin.repo-%{osname}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Virtualmin release file. This package also contains yum configuration to
use the virtualmin.com provided rpm packages, as well as the public gpg key
used to sign them.  It also installs the Webmin public key, so automatic
upgrades of Webmin from webmin.com will have valid keys.


%prep


%build


%install
%{__rm} -rf %{buildroot}
%{__cp} -a %{SOURCE0} %{SOURCE1} .
# Install gpg public keys
%{__install} -D -p -m 0644 %{SOURCE0} \
    %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-webmin
%{__install} -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-virtualmin
%{__install} -D -p -m 0644 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-virtualmin-6
# Install yum repo file
%{__install} -D -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/yum.repos.d/virtualmin.repo


%clean
%{__rm} -rf %{buildroot}


%post
# Hopefully, only run this if this is our first installation
if [ "$1" -eq 1 ]; then
  # Import Jamie's gpg key if needed
  rpm -q gpg-pubkey-11f63c51-3c7dc11d >/dev/null 2>&1 || \
    rpm --import %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-webmin
  # Import the Virtualmin official gpg key if needed
  rpm -q gpg-pubkey-a0bdbcf9-42d1d837 >/dev/null 2>&1 || \
    rpm --import %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-virtualmin
  # Import the Virtualmin 6.0 official gpg key if needed
  rpm -q gpg-pubkey-9d3152d3-895093ac >/dev/null 2>&1 || \
    rpm --import %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-virtualmin-6

  # Get the serial/key from the /etc/virtualmin-license file
  . /etc/virtualmin-license

  # Fix up the paths in the repo to include serial and key
  sed -i "s/SERIALNUMBER/$SerialNumber/" %{_sysconfdir}/yum.repos.d/virtualmin.repo
  sed -i "s/LICENSEKEY/$LicenseKey/" %{_sysconfdir}/yum.repos.d/virtualmin.repo

fi

# We don't want a possible error to leave the previous package installed
exit 0


%files
%defattr(-, root, root, 0755)
%pubkey RPM-GPG-KEY-webmin
%pubkey RPM-GPG-KEY-virtualmin
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-webmin
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-virtualmin
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-virtualmin-6
%attr(6750,root,root) %config(noreplace) %{_sysconfdir}/yum.repos.d/virtualmin.repo


%changelog
* Wed Apr 19 2017 Joe Cooper <joe@virtualmin.com>
- New GPG key for Virtualmin 6 packages and new installer
* Sat Jul 27 2013 Joe Cooper <joe@virtualmin.com>
- Remove locate and updatedb stuff; was more trouble than it was worth
- Rebuilding for Fedora, among others
* Thu Jun 02 2011 Joe Cooper <joe@virtualmin.com>
- Remove legacy cruft for dealing with old yum and up2date
- Remove key importation of system keys...this is probably understood by users today, where it used to confuse and alarm users during install.
* Wed Oct 25 2006 Joe Cooper <joe@virtualmin.com>
- Fixed syntax errors in post script
* Wed Sep 06 2006 Joe Cooper <joe@virtualmin.com>
- Fixed permissions on repo file
- Made post only run on first install
* Wed Sep 07 2005 Joe Cooper <joe@virtualmin.com>
- yum version detection to add to yum.conf in old yums
* Tue Sep 06 2005 Joe Cooper <joe@virtualmin.com>
- Removed the up2date stuff...we have to use yum
- Added import of the system RPM-GPG-KEY files, as it causes errors during
  install if we don't have them.
* Wed Aug 10 2005 Joe Cooper <joe@virtualmin.com>
- Moved all distro neutral files into "universal" repo, which should
  save a lot of maintenance time
* Sun Jul 10 2005 Joe Cooper <joe@virtualmin.com>
- First release
- New Virtualmin, Inc. GPG key for package signing
