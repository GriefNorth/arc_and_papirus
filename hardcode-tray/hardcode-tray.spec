#
# spec file for package hardcode-tray
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

Name:           Hardcode-Tray
Version:        4.1
Release:        1%{?dist}
License:        GPL-3.0
Summary:        Fixes Hardcoded tray icons in Linux
Url:            https://github.com/bil-elmoussaoui/Hardcode-Tray
Source:         %{name}-%{version}.tar.gz
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  python3
BuildRequires:  ninja
BuildRequires:  meson >= 0.40
Requires:       ImageMagick
Requires:       sni-qt-patched
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The script will automatically detect your default theme, the correct icon size, the hard-coded applications, the correct icons for each indicator and fix them. All that with the possibility to revert to the original icons.

%prep
%setup -q
rm -rf builddir && mkdir builddir

%build
pushd builddir
meson ..
ninja -v
popd

%install
pushd builddir
DESTDIR=%{buildroot} ninja -v install
popd

%files
%defattr(-,root,root)
%doc README.md
%{_bindir}/*
%{_datadir}/hardcode-tray
%{_datadir}/locale/*
%{_datadir}/man/man1/*
%{python3_sitelib}/HardcodeTray

%changelog

