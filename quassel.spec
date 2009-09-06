Name: quassel
Version: 0.5.0
Release: %mkrel 0.rc1.1
Summary: A modern, cross-platform, distributed IRC client - This is the monolithic client
Source0: http://quassel-irc.org/pub/quassel-%{version}-rc1.tar.bz2
Source1: networks.ini
Group: Networking/IRC
License: GPLv3
URL: http://quassel-irc.org/
BuildRequires: qt4-linguist 
BuildRequires: kdelibs4-devel
Requires: quassel-common = %version
BuildRoot: %{_tmppath}/%{name}-root

%description
Quassel IRC is a modern, cross-platform, distributed IRC client, meaning that
one (or multiple) client(s) can attach to and detach from a central core --
much like the popular combination of screen and a text-based IRC client such as
WeeChat, but graphical. In addition to this uniqe feature, we aim to bring a
pleasurable, comfortable chatting experience to all major platforms (including
Linux®, Windows®, and MacOS X® as well as Qtopia-based cell phones and PDAs),
making communication with your peers not only convenient, but also ubiquitous
available.

%files
%defattr(-,root,root)
%{_bindir}/quassel
%{_kde_applicationsdir}/quassel.desktop

#-------------------------------------------------------------------------------

%package common
Group: Networking/IRC
Summary: A modern, cross-platform, distributed IRC client - Common files
Requires: qt4-database-plugin-sqlite
Conflicts: quassel < 0.3.1.20090128-4

%description common
A modern, cross-platform, distributed IRC client - This is client only, depends on a core server.

%files common
%defattr(-,root,root)
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_kde_appsdir}/quassel
%doc AUTHORS ChangeLog README

#-------------------------------------------------------------------------------

%package client
Group: Networking/IRC
Summary: A modern, cross-platform, distributed IRC client - This is client only, depends on a core server
Requires: quassel-common = %version

%description client
A modern, cross-platform, distributed IRC client - This is client only, depends on a core server.

%files client
%defattr(-,root,root)
%{_bindir}/quasselclient
%{_kde_applicationsdir}/quasselclient.desktop

#-------------------------------------------------------------------------------

%package core
Group: Networking/IRC
Summary: A modern, cross-platform, distributed IRC client - This is quassel core server for clients
Requires: quassel-common = %version

%description core
A modern, cross-platform, distributed IRC client - This is quassel core server for clients.

%files core
%defattr(-,root,root)
%{_bindir}/quasselcore

#-------------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-rc1

%build
%cmake_kde4 \
    -DWANT_MONO=ON \
    -DWITH_KDE=ON \
    -DEMBED_DATA=OFF
%make

%install
rm -Rf %{buildroot}
%makeinstall_std -C build

# Our own defined networks
rm -f %buildroot/%_datadir/apps/quassel/networks.ini
install -m 644 %{SOURCE1} %buildroot/%_datadir/apps/quassel/

%clean
rm -Rf %{buildroot}

