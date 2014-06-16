#
# spec file for package google+-qtcurve-theme
#
# Copyright (c) 2014 Kamarada Project, Aracaju, Brazil.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://github.com/kamarada
#


%define zipfile kde4___qtcurve_google__by_half_left-d67en0j
Name:           google-plus-qtcurve-theme
Version:        1.0
Release:        1
Summary:        Google+ QtCurve widget theme and colour scheme for KDE4 designed by Sean Wilson
License:        GPL-2.0+
Group:          System/GUI/KDE
Source0:        %{zipfile}.zip
Source1:        LICENSE
Url:            http://half-left.deviantart.com/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  unzip
Requires:       qtcurve-kde4


%description
This is a widget theme and window decoration based on the look of Google+ social network website.

http://half-left.deviantart.com/art/KDE4-QtCurve-Google-375237379


%prep
%setup -q -c
rm COPYING
cp -a %{SOURCE1} COPYING


%build


%install
echo %{_kde4_appsdir}
mkdir -p %{buildroot}%{_kde4_appsdir}/color-schemes
cp Google.colors %{buildroot}%{_kde4_appsdir}/color-schemes
mkdir -p %{buildroot}%{_kde4_appsdir}/QtCurve
cp Google+.qtcurve %{buildroot}%{_kde4_appsdir}/QtCurve


%files
%defattr(-,root,root)
%doc COPYING
%dir %{_kde4_sharedir}
%dir %{_kde4_appsdir}
%dir %{_kde4_appsdir}/color-schemes
%{_kde4_appsdir}/color-schemes/Google.colors
%dir %{_kde4_appsdir}/QtCurve
%{_kde4_appsdir}/QtCurve/Google+.qtcurve


%changelog
* Mon Jun 16 2014 kamaradalinux@gmail.com
- Initial draft