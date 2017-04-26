Summary: The OCILIB is an open source and cross platform Oracle Driver that delivers efficient access to Oracle databases.
Name: ocilib
Version: %{package_version}
Release: %{pack_rel}%{?dist}
License: BSD
Group: Applications/Internet
Source0: https://github.com/HSchill/ocilib/archive/%{name}-%{version}-%{pack_rel}.tar.gz

URL: http://orclib.sourceforge.net
Requires: glibc
Requires(post): /sbin/service
Requires(postun): /sbin/service
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The CILIB is an open source and cross platform Oracle Driver
that delivers efficient access to Oracle databases.

The OCILIB library :
 - offers a rich, full featured and easy to use API
 - runs on all Oracle platforms
 - is written in pure ISO C code with native ISO C Unicode support
 - Enables high productivity
 - encapsulates OCI (Oracle Call Interface)
 - is the most complete available OCI wrapper


%prep
%setup -n %{name}-%{version}

%build
%define oracle_dev /opt/stage/oracle/instantclient_11_2
#autoreconf -fi
./configure --prefix=/usr --libdir=/usr/lib64 --sysconfdir=/etc --enable-silent-rules \
 --with-oracle-headers-path=%{oracle_dev}/sdk/include --with-oracle-lib-path=%{oracle_dev}
make

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} install
rm -f ${RPM_BUILD_ROOT}/usr/lib64/*.la
rm -f ${RPM_BUILD_ROOT}/usr/lib64/*.a
rm -rf ${RPM_BUILD_ROOT}/usr/share

#
# Before install
#
%pre

#
# After install / Upgrade
#
%post

#
# Before uninstall
#
%preun

#
# After uninstall
#
%postun

#
# Cleanup build
#
%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
%{_libdir}/libocilib.so*
%{_libdir}/pkgconfig/*
%{_includedir}/ocilib.h
%{_includedir}/ocilib.hpp
%{_includedir}/ocilib_core.hpp
%{_includedir}/ocilib_impl.hpp

%changelog
* Tue Mar 25 2014 Hans Schillstrom <hans.schillstrom.com>
- Created

