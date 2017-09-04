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

Name:           papirus-amule-theme
Version:        20170903
Release:        1%{?dist}
License:        GPL-3.0
Summary:        Papirus theme for aMule
Url:            https://github.com/PapirusDevelopmentTeam/papirus-filezilla-themes
Group:          System/GUI/Other
Source:         %{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  rsvg-view
BuildRequires:  zip
Requires:  aMule
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Papirus theme for aMule

%prep
%setup -q

%build
make build

%install
install -Dm 644 ePapirus.zip %{buildroot}%{_datadir}/amule/skins/ePapirus.zip
install -Dm 644 Papirus-Dark.zip %{buildroot}%{_datadir}/amule/skins/Papirus-Dark.zip
install -Dm 644 Papirus.zip %{buildroot}%{_datadir}/amule/skins/Papirus.zip

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE README.md
%dir %{_datadir}/amule
%dir %{_datadir}/amule/skins
%{_datadir}/amule
%{_datadir}/amule/skins
%{_datadir}/amule/skins/ePapirus.zip
%{_datadir}/amule/skins/Papirus-Dark.zip
%{_datadir}/amule/skins/Papirus.zip

%changelog
