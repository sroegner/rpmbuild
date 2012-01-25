%define node_version %(echo "${NODE_VERSION}")
# building this inside jenkins will assign the CI build number as the rpm build number
%define bld_num %(if [ -z "$BUILD_NUMBER" ]; then echo 1; else echo $BUILD_NUMBER; fi)

Name:          nodejs
Version:       %{node_version}
Release:       %{bld_num}%{?dist}
Summary:       Evented I/O for V8 JavaScript
Group:         Development/Libraries
Vendor:        Xceptance Inc.
Packager:      Steffen Roegner <steffen@sroegner.org>
URL:           http://nodejs.org/
Source:        http://nodejs.org/dist/node-v%{version}.tar.gz
Patch0:         node-v%{version}-doc.patch
License:       MIT
BuildRequires: glibc-devel libgcc openssl-devel libstdc++-devel
Provides:      /usr/bin/node

%description
Evented I/O for V8 JavaScript.

%package	devel
Summary:	Development files for nodejs
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for nodejs

%package	npm
Summary:	Package Manager for nodejs
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description npm
Node Package Manager

%prep
%setup -q -n node-v%{version}
./configure --prefix=%{_prefix} --dest-cpu=x64

%patch0

%build
make -j2

%install
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"
make DESTDIR=%{buildroot} install
for e in $(find %{buildroot} -exec grep -l '/usr/bin/env' {} \;)
do 
  chmod 755 ${e}
done
make DESTDIR=%{buildroot} doc
gzip -9 %{buildroot}/usr/lib/node_modules/npm/man/man?/*
chmod 755 %{buildroot}/usr/lib/node_modules/npm/scripts/*

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
%doc AUTHORS ChangeLog LICENSE

%files npm
%{_bindir}/npm
%dir /usr/lib/node_modules
/usr/lib/node_modules/*

%files devel
%defattr(-, root, root)
%dir %{_includedir}/node
%{_includedir}/node/*
# /usr/lib/pkgconfig/nodejs.pc
%doc doc/api/api/*

%changelog
* Fri Dec 01 2011 Steffen Roegner <steffen@sroegner.org> 0.6.4-1%{?dist}
- bumping version to 0.6.4
- added npm package

* Wed Oct 27 2011 Steffen Roegner <steffen@sroegner.org> 0.4.12-1%{?dist}
- bumping up to 0.4.12
- added api doc to devel package

* Sat Jun 25 2011 Steffen Roegner <steffen@sroegner.org> 0.4.8-1%{?dist}
- initial rpm build

