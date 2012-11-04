Name:           libdatrie
Version:        0.2.4
Release:        0
License:        LGPL-2.1
Summary:        Double-Array Trie Library
Url:            http://linux.thai.net/~thep/datrie/datrie.html
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
Source99:       baselibs.conf
BuildRequires:  doxygen
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is an implementation of double-array structure for representing
trie, as proposed by Junichi Aoe.

Summary:        Double-Array Trie Library
Group:          Development/Libraries/C and C++

%package devel
Summary:        Double-Array Trie Library (development)
Group:          Development/Libraries/C and C++
Requires:       libdatrie = %{version}

%description devel
This is an implementation of double-array structure for representing
trie, as proposed by Junichi Aoe.

This package contains the development files for libdatrie.

%prep
%setup -q

%build
%configure \
        --disable-static --with-pic \
        --with-html-docdir=%{_docdir}/libdatrie/html
make %{?_smp_mflags}

%install
%make_install
# This is not installed where it should
mv %{buildroot}%{_datadir}/doc/libdatrie/README.migration %{buildroot}%{_docdir}/libdatrie/

%post  -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libdatrie.so.1*

%files devel
%defattr(-,root,root)
%{_bindir}/trietool-0.2
%doc %{_mandir}/man*/trietool-0.2.*
%{_includedir}/datrie/
%{_libdir}/libdatrie.so
%{_libdir}/pkgconfig/datrie-0.2.pc
%doc %{_docdir}/libdatrie/
