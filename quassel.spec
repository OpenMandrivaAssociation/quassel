Summary:	A modern cross-platform distributed IRC client (monolythic)
Name:		quassel
Version:	0.12.2
Release:	5
Group:		Networking/IRC
License:	GPLv3
Url:		http://quassel-irc.org/
Source0:	http://quassel-irc.org/pub/quassel-%{version}.tar.bz2
Source1:	networks.ini
BuildRequires:	cmake
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	qt5-linguist-tools
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(qca2-qt5)
BuildRequires:	pkgconfig(dbusmenu-qt5)
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
%{_datadir}/applications/quassel.desktop
#%{_kde_applicationsdir}/quassel.desktop

#-----------------------------------------------------------------------

%package common
Group:		Networking/IRC
Summary:	A modern cross-platform distributed IRC client - Common files
Requires:	qt5-database-plugin-sqlite
Conflicts:	quassel < 0.3.1.20090128-4

%description common
A modern, cross-platform, distributed IRC client
- This is client only, depends on a core server.

%files common
%dir %{_datadir}/apps/quassel
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/apps/quassel/*
#%{_kde_appsdir}/quassel
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
%{_datadir}/applications/quasselclient.desktop
#%{_kde_applicationsdir}/quasselclient.desktop

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
%cmake_qt5 \
	-DUSE_QT5=ON \
    -DWANT_MONO=ON \
    -DWITH_KDE=OFF \
    -DEMBED_DATA=OFF

%make

%install
%makeinstall_std -C build

# Our own defined networks
rm -f %buildroot/%_datadir/apps/quassel/networks.ini
install -m 644 %{SOURCE1} %buildroot/%_datadir/apps/quassel/
sed -i "s/<distro>/%{product_product}/" %buildroot/%_datadir/apps/quassel/networks.ini

