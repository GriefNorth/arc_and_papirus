#
# spec file for package arc-theme
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

Name:           arc-theme
Version:        20150605
Release:        1%{?dist}
License:        GPL-3
Summary:        Arc is a theme for GTK 3, GTK 2 and Gnome-Shell.
Url:            https://github.com/horst3180/Arc-theme
Group:          User Interface/Desktops
Source:         %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk3-devel
Requires:       gtk2-engine-murrine
Requires:       gtk2-theming-engine-adwaita
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Arc is a flat theme with transparent elements for GTK 3, GTK 2 and Gnome-Shell. It supports GTK 3 and GTK 2 based desktop environments like Gnome, Unity, Budgie, Pantheon, etc.

%prep
%setup -q

%build
./autogen.sh --prefix=/usr

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name "*.sh" -exec chmod -x {} \;

%files
%defattr(-,root,root)
%doc
%{_datadir}/themes/Arc
%{_datadir}/themes/Arc-Darker
%{_datadir}/themes/Arc-Dark

%changelog
