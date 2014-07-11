Summary:	A modern cross-platform distributed IRC client (monolythic)
Name:		quassel
Version:	0.10.0
Release:	3
Group:		Networking/IRC
License:	GPLv3
Url:		http://quassel-irc.org/
Source0:	http://quassel-irc.org/pub/quassel-%{version}.tar.bz2
Source1:	networks.ini
BuildRequires:	qt4-linguist >= 4:4.6.0
BuildRequires:	kdelibs4-devel
Requires:	quassel-common = %{version}
Provides:	kde4-irc-client

%description
Quassel IRC is a modern, cross-platform, distributed IRC client,
meaning that one (or multiple) client(s) can attach to and detach
from a central core -- much like the popular combination of screen
and a text-based IRC client such as WeeChat, but graphical. In
addition to this unique feature, we aim to bring a pleasurable,
comfortable chatting experience to all major platforms (including
Linux®, Windows®, and MacOS X® as well as Qtopia-based cell phones
and PDAs), making communication with your peers not only convenient,
but also ubiquitous available.

%files
%{_bindir}/quassel
%{_kde_applicationsdir}/quassel.desktop

#-----------------------------------------------------------------------

%package common
Group:		Networking/IRC
Summary:	A modern cross-platform distributed IRC client - Common files
Requires:	qt4-database-plugin-sqlite
Conflicts:	quassel < 0.3.1.20090128-4

%description common
A modern, cross-platform, distributed IRC client
- This is client only, depends on a core server.

%files common
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/pixmaps/%{name}.png
%{_kde_appsdir}/quassel
%doc AUTHORS ChangeLog README

#-----------------------------------------------------------------------

%package client
Group:		Networking/IRC
Summary:	A modern cross-platform distributed IRC client - Client only
Requires:	quassel-common = %{version}

%description client
A modern, cross-platform, distributed IRC client - Client only

%files client
%{_bindir}/quasselclient
%{_kde_applicationsdir}/quasselclient.desktop

#-----------------------------------------------------------------------

%package core
Group:		Networking/IRC
Summary:	A modern cross-platform distributed IRC client - Core server
Requires:	quassel-common = %{version}

%description core
A modern, cross-platform, distributed IRC client - This is the quassel
core server for clients.

%files core
%{_bindir}/quasselcore

#-----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
    -DWANT_MONO=ON \
    -DWITH_KDE=ON \
    -DEMBED_DATA=OFF
%make

%install
%makeinstall_std -C build

# Our own defined networks
rm -f %buildroot/%_datadir/apps/quassel/networks.ini
install -m 644 %{SOURCE1} %buildroot/%_datadir/apps/quassel/

