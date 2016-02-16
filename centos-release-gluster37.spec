Summary: GlusterFS 3.7 packages from the CentOS Storage SIG repository
Name: centos-release-gluster37
Version: 1.0
Release: 6%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-Gluster-3.7.repo

BuildArch: noarch

# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

# Users can install centos-release-gluster to get the latest
Provides: centos-release-gluster = 3.7
Conflicts: centos-release-gluster < 3.7
Obsoletes: centos-release-gluster < 3.7

%description
yum configuration for GlusterFS 3.7 packages as delivered via the CentOS
Storage SIG.

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-3.7.repo

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Gluster-3.7.repo

%changelog
* Tue Feb 16 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 1.0-6
- Add -debuginfo and -source repos, post tag permission

* Tue Feb 16 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 1.0-5
- Add -debuginfo and -source repos

* Fri Nov 13 2015 Niels de Vos <ndevos@redhat.com> - 1.0-4
- Disable "gpgcheck" for testing repo, packages are not signed

* Thu Nov 12 2015 Niels de Vos <ndevos@redhat.com> - 1.0-3
- Drop the license file, it does not seem to be needed for -release packages

* Thu Nov 12 2015 Niels de Vos <ndevos@redhat.com> - 1.0-2
- Rebuild for CentOS Extras

* Thu Nov 12 2015 Niels de Vos <ndevos@redhat.com> - 1.0-1
- Initial version based on centos-release-ovirt36
- Add provides for "centos-release-gluster = 3.7"
