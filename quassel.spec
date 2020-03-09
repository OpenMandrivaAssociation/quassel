Summary:	A modern cross-platform distributed IRC client (monolythic)
Name:		quassel
Version:	0.13.1
Release:	6
Group:		Networking/IRC
License:	GPLv3
Url:		http://quassel-irc.org/
Source0:	http://quassel-irc.org/pub/quassel-%{version}.tar.bz2
Patch0:		quassel-0.13.1-qt-5.14.patch
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	qt5-linguist-tools
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(qca2-qt5)
BuildRequires:	pkgconfig(dbusmenu-qt5)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)

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
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/quassel
%{_datadir}/knotifications5/quassel.notifyrc

%doc AUTHORS ChangeLog README.md

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
%autopatch -p1

# Join our channels by default
sed -i "s/^DefaultChannels=.*/DefaultChannels=#openmandriva,#openmandriva-cooker/g" data/networks.ini

%build
%cmake_qt5 \
	-DUSE_QT5=ON \
	-DWANT_MONO=ON \
	-DWITH_KDE=ON \
	-DEMBED_DATA=OFF \
	-G Ninja

%ninja_build

%install
%ninja_install -C build
