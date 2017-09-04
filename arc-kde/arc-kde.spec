#
# spec file for package arc-kde
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

Name:           arc-kde
Version:        20170423
Release:        1
License:        GPL-3.0
Summary:        Arc KDE customization 
Url:            https://github.com/PapirusDevelopmentTeam/
Group:          System/GUI/Other
Source:         %{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Arc KDE - This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few additions and extras.

%package style
Summary: Arc theme for KDE
Group:   System/GUI/KDE
BuildArch: noarch

%description style
Arc KDE - This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few additions and extras.
This package contains:

Plasma Desktop Themes
Color Schemes

%package kvantum
Summary: Arc theme for KDE
Group:   System/GUI/KDE
BuildArch: noarch

%description kvantum
Arc KDE - This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few additions and extras.
This package contains:

Kvantum Themes

%package decoration
Summary: Arc theme for KDE
Group:   System/GUI/KDE
BuildArch: noarch

%description decoration
Arc KDE - This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few additions and extras.
This package contains:

Aurorae Window Decorations

%package konsole
Summary: Arc theme for KDE
Group:   System/GUI/KDE
BuildArch: noarch

%description konsole
Arc KDE - This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few additions and extras.
This package contains:

Konsole Themes

%package konversation
Summary: Arc theme for KDE
Group:   System/GUI/KDE
BuildArch: noarch

%description konversation
Arc KDE - This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few additions and extras.
This package contains:

Konversation Themes

%package wallpapers
Summary: Arc theme for KDE
Group:   System/GUI/KDE
BuildArch: noarch

%description wallpapers
Arc KDE - This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few additions and extras.
This package contains:

Wallpapers

%package yakuake
Summary: Arc theme for KDE
Group:   System/GUI/KDE
BuildArch: noarch

%description yakuake
Arc KDE - This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few additions and extras.
This package contains:

Yakuake Skins

%prep
%setup

%install                                                                                                                                                                                                       make install DESTDIR=%{buildroot} %{?_smp_mflags}
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%files style
%defattr(-,root,root)
%doc AUTHORS LICENSE README.md
%{_datadir}/color-schemes
%{_datadir}/plasma
%files decoration
%defattr(-,root,root)
%{_datadir}/aurorae
%files konsole
%defattr(-,root,root)
%{_datadir}/konsole
%files konversation
%defattr(-,root,root)
%{_datadir}/konversation
%files kvantum
%defattr(-,root,root)
%{_datadir}/Kvantum
%files wallpapers
%defattr(-,root,root)
%{_datadir}/wallpapers
%files yakuake
%defattr(-,root,root)
%dir %{_datadir}/yakuake
%dir %{_datadir}/yakuake/skins
%{_datadir}/yakuake/skins/arc
%{_datadir}/yakuake/skins/arc-dark

