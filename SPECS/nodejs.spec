Name:          nodejs
Version:       0.5.0
Release:       1%{?dist}
Summary:       Evented I/O for V8 JavaScript
Group:         Development/Libraries
Vendor:        Xceptance Inc.
Packager:      Steffen Roegner <steffen@sroegner.org>
URL:           http://nodejs.org/
Source:        http://nodejs.org/dist/node-v%{version}.tar.gz
License:       MIT
BuildRequires: glibc-devel
BuildRequires: libgcc
BuildRequires: openssl-devel
BuildRequires: libstdc++-devel
Provides:      /usr/bin/node

%description
Evented I/O for V8 JavaScript.

%package	devel
Summary:	Development files for nodjs
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for node.js

%prep
%setup -q -n node-v%{version}

%build
./configure --prefix=%{_prefix} --dest-cpu=x64
make %{?_smp_mflags}

%install
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"
make DESTDIR=%{buildroot} install
for e in $(find %{buildroot} -exec grep -l '/usr/bin/env' {} \;)
do 
  chmod 755 ${e}
done

%clean
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%{_bindir}/node
%{_bindir}/node-waf
%dir /usr/lib/node
%dir /usr/lib/node/wafadmin
/usr/lib/node/wafadmin/*
%{_mandir}/man1/node.1*
%doc AUTHORS ChangeLog LICENSE TODO

%files devel
%defattr(-, root, root)
%dir %{_includedir}/node
%{_includedir}/node/*.h
%dir %{_includedir}/node/c-ares
%dir %{_includedir}/node/ev
%{_includedir}/node/c-ares/*.h
%{_includedir}/node/ev/*.h

/usr/lib/pkgconfig/nodejs.pc

%changelog
* Wed Jul 06 2011 Steffen Roegner <steffen@sroegner.org> 0.5.0-1%{?dist}
- bumping up to unstable 0.5.0

* Sat Jun 25 2011 Steffen Roegner <steffen@sroegner.org> 0.4.8-1%{?dist}
- initial rpm build

