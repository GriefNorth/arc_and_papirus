#
# spec file for package papirus-filezilla-theme
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

Name:           papirus-smplayer-theme
Version:        20170119
Release:        1%{?dist}
License:        GPL-3.0
Summary:        Papirus theme for SMPlayer
Url:            https://github.com/PapirusDevelopmentTeam/papirus-smplayer-theme

Group:          System/GUI/Other
Source:         %{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  autoconf
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Papirus theme for SMPlayer

%prep
%setup -q

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name "*.sh" -exec chmod -x {} \;

%files
%defattr(-,root,root)
%doc LICENSE
%dir %{_datadir}/smplayer
%dir %{_datadir}/smplayer/themes
%{_datadir}/smplayer/themes/Papirus
%{_datadir}/smplayer/themes/ePapirus
%{_datadir}/smplayer/themes/PapirusDark

%changelog
