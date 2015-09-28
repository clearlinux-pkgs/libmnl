#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libmnl
Version  : 1.0.3
Release  : 6
URL      : http://ftp.netfilter.org/pub/libmnl/libmnl-1.0.3.tar.bz2
Source0  : http://ftp.netfilter.org/pub/libmnl/libmnl-1.0.3.tar.bz2
Summary  : Minimalistic Netlink communication library
Group    : Development/Tools
License  : LGPL-2.1
Requires: libmnl-lib

%description
= What is libmnl? =
libmnl is a minimalistic user-space library oriented to Netlink developers.
There are a lot of common tasks in parsing, validating, constructing of
both the Netlink header and TLVs that are repetitive and easy to get wrong.
This library aims to provide simple helpers that allows you to re-use code
and to avoid re-inventing the wheel. The main features of this library are:

%package dev
Summary: dev components for the libmnl package.
Group: Development
Requires: libmnl-lib

%description dev
dev components for the libmnl package.


%package lib
Summary: lib components for the libmnl package.
Group: Libraries

%description lib
lib components for the libmnl package.


%prep
%setup -q -n libmnl-1.0.3

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libmnl/libmnl.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
