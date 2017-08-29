#
# spec file for package libreoffice-icon-theme-papirus
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           papirus-libreoffice-theme
Version:        20170228
Release:        1%{?dist}
Summary:        Papirus theme for Libreoffice
License:        GPL-3.0
Group:          System/GUI/Other
Url:            https://github.com/PapirusDevelopmentTeam/papirus-libreoffice-theme
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  automake
Requires:       libreoffice-share-linker
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Papirus theme for LibreOffice is available in three variants:

ePapirus
Papirus
Ppirus Dark

%prep
%setup -n papirus-libreoffice-theme-%{version}

%install
make DESTDIR=%{buildroot} install

%posttrans
rpm -ql %{name} > %{_datadir}/libreoffice/%{name}_list.txt || true
if [ -f %{_datadir}/libreoffice/%{name}_list.txt ] ; then
    %{_bindir}/libreoffice-share-linker %{_datadir}/libreoffice/%{name}_list.txt || true
fi

%postun
if [ "$1" = "0" -a -f %{_datadir}/libreoffice/%{name}_list.txt -a -x %{_bindir}/libreoffice-share-linker ]; then
%{_bindir}/libreoffice-share-linker --unlink %{_datadir}/libreoffice/%{name}_list.txt || true
rm -f %{_datadir}/libreoffice/%{name}_list.txt 2> /dev/null || true
fi


%files
%defattr(-,root,root)
%doc AUTHORS LICENSE README.md
%dir %{_datadir}/libreoffice
%dir %{_datadir}/libreoffice/share
%dir %{_datadir}/libreoffice/share/config

%{_datadir}/libreoffice/share/config/images_papirus.zip
%{_datadir}/libreoffice/share/config/images_epapirus.zip
%{_datadir}/libreoffice/share/config/images_papirus_dark.zip

%changelog
