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

Name:           arc-xfce4-terminal-theme
Version:        1.2
Release:        1%{dist}
License:        GPL-3.0
Summary:        Arc theme for xfce4-terminal
Url:            https://aur.archlinux.org/packages/arc-dark-xfce4-terminal/

Group:          System/GUI/Other
Source:         %{name}-%{version}.tar.gz
Requires:       xfce4-terminal
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Arc theme for color profile xfce4-terminal

%prep
%setup -q

%install
install -d -m 644 arc-dark.theme %{buildroot}/xfce4/terminal/colorschemes/arc-dark.theme

%files
%defattr(-,root,root)

%changelog
