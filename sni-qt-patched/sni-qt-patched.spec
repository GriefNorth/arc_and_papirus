#
# spec file for package sni-qt-patched
#
# Copyright (c) 2017 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           sni-qt-patched
Version:        20170904
Release:        1%{?dist}
License:        LGPL-3.0
Summary:        Library that turns Qt tray icons into appindicators, patched for custom icons
Url:            https://github.com/bil-elmoussaoui/sni-qt
Group:          System/Libraries
Source0:        %{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kde4-filesystem
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(dbusmenu-qt)
Conflicts:      sni-qt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains a Qt plugin which turns all QSystemTrayIcon into
StatusNotifierItems (appindicators). This version is patched for inserting custom icons.

%prep
%setup -q

%build
%cmake_kde4 -d build
%make_jobs

%install
%kde4_makeinstall -C build
install -D -m 0644 debian/sni-qt.conf %{buildroot}%{_sysconfdir}/xdg/sni-qt.conf

%files
%defattr(-,root,root)
%doc README.md COPYING* LGPL*
%dir %{_kde4_libdir}/qt4/plugins/systemtrayicon/
%{_kde4_libdir}/qt4/plugins/systemtrayicon/libsni-qt.so
%config %{_sysconfdir}/xdg/sni-qt.conf

%changelog
