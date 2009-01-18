Name: quassel
Version: 0.3.1
Release: %mkrel 2
Source: http://quassel-irc.org/pub/quassel-%{version}.tar.bz2
Patch0:         quassel-0.3.1-fix-string-error.patch
Group: Networking/IRC
License: GPLv3
URL: http://quassel-irc.org/
Summary: A modern, cross-platform, distributed IRC client
BuildRequires: qt4-devel qt4-linguist cmake
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

%prep
%setup -q
%patch0 -p1

%build

cmake -D CMAKE_INSTALL_PREFIX=%{_prefix} .
%make

%install
rm -Rf %{buildroot}
%makeinstall_std

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%doc AUTHORS ChangeLog README
