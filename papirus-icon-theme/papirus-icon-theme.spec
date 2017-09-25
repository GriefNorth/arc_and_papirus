#
# spec file for package papirus-icon-theme
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

Name:           papirus-icon-theme
Version:        20170219
Release:        1%{?dist}
License:        LGPL-3.0
Summary:        Papirus icon theme for Linux
Url:            https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
Group:          System/GUI/Other
Source:         %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk3-devel
BuildRequires:  fdupes
Requires(post): gtk3-tools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Papirus - A free and open source SVG icon theme for Linux systems, based on Paper with a few extras like
hardcode-tray support, kde-color-scheme support, libreoffice icon theme, filezilla theme, smplayer themes ...)
and other modifications. The theme is available for GTK and KDE.

This package contains the following icon themes:

ePapirus
Papirus
Papirus-Dark
Papirus-Light
Papirus-Adapta
Papirus-Adapta-Nokto

%prep
%setup -q

%build

%install
make DESTDIR=%{buildroot} install
%fdupes %{buildroot}

%post
%icon_theme_cache_post ePapirus
%icon_theme_cache_post Papirus
%icon_theme_cache_post Papirus-Light
%icon_theme_cache_post Papirus-Dark
%icon_theme_cache_post Papirus-Adapta
%icon_theme_cache_post Papirus-Adapta-Nokto

%files
%defattr(-,root,root)
%doc LICENSE README.md
%{_datadir}/icons/ePapirus
%{_datadir}/icons/Papirus
%{_datadir}/icons/Papirus-Light
%{_datadir}/icons/Papirus-Dark
%{_datadir}/icons/Papirus-Adapta
%{_datadir}/icons/Papirus-Adapta-Nokto
%ghost %{_datadir}/icons/ePapirus/icon-theme.cache
%ghost %{_datadir}/icons/Papirus/icon-theme.cache
%ghost %{_datadir}/icons/Papirus-Light/icon-theme.cache
%ghost %{_datadir}/icons/Papirus-Dark/icon-theme.cache
%ghost %{_datadir}/icons/Papirus-Adapta/icon-theme.cache
%ghost %{_datadir}/icons/Papirus-Adapta-Nokto/icon-theme.cache

%pretrans
if [ -d %{_datadir}/icons/Papirus-Dark/22x22/panel ] && [ -d %{_datadir}/icons/Papirus-Dark/24x24/panel ]; then
       rm -rf %{_datadir}/icons/Papirus-Dark/22x22/panel
       rm -rf %{_datadir}/icons/Papirus-Dark/24x24/panel
fi

%changelog
