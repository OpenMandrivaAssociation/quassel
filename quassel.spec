# Tarball from Git daily
%define git_day 20090128

Name: quassel
Version: 0.3.1.%{git_day}
Release: %mkrel 3
Summary: A modern, cross-platform, distributed IRC client - This is the monolithic client
Source: http://quassel-irc.org/pub/quassel-%{version}.tar.bz2
Group: Networking/IRC
License: GPLv3
URL: http://quassel-irc.org/
BuildRequires: qt4-devel 
BuildRequires: qt4-linguist 
BuildRequires: cmake
BuildRequires: kdelibs4-devel
Requires: qt4-database-plugin-sqlite
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
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_kde_appsdir}/quassel
%{_kde_applicationsdir}/quassel.desktop
%doc AUTHORS ChangeLog README

#-------------------------------------------------------------------------------

%package client
Group: Networking/IRC
Summary: A modern, cross-platform, distributed IRC client - This is client only, depends on a core server
Requires: quassel = %version

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
Requires: quassel = %version

%description core
A modern, cross-platform, distributed IRC client - This is quassel core server for clients.

%files core
%defattr(-,root,root)
%{_bindir}/quasselcore

#-------------------------------------------------------------------------------

%prep
%setup -q -n quassel

%build
%cmake_kde4 \
    -DWANT_MONO=ON \
    -DWITH_KDE=ON \
    -DEMBED_DATA=OFF
%make

%install
rm -Rf %{buildroot}
%makeinstall_std -C build

%clean
rm -Rf %{buildroot}

