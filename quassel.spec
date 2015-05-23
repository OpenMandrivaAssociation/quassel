Name:       quassel
Version:    0.12.2
Release:    0.2
Summary:    A modern cross-platform distributed IRC client (monolythic)
Source0:    http://quassel-irc.org/pub/quassel-%{version}.tar.bz2
Source1:    networks.ini
Group:      Networking/IRC
License:    GPLv3
URL:        http://quassel-irc.org/
BuildRequires:  qt4-linguist >= 4:4.6.0
BuildRequires:  kdelibs4-devel
Requires:   quassel-common = %{version}
Provides:   kde4-irc-client

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
%defattr(-,root,root)
%{_bindir}/quassel
%{_kde_applicationsdir}/quassel.desktop

#-----------------------------------------------------------------------

%package common
Group: Networking/IRC
Summary: A modern cross-platform distributed IRC client - Common files
Requires: qt4-database-plugin-sqlite
Conflicts: quassel < 0.3.1.20090128-4

%description common
A modern, cross-platform, distributed IRC client
- This is client only, depends on a core server.

%files common
%defattr(-,root,root)
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/%{name}.png
%{_kde_appsdir}/quassel
%doc AUTHORS ChangeLog README

#-----------------------------------------------------------------------

%package client
Group: Networking/IRC
Summary: A modern cross-platform distributed IRC client - Client only
Requires: quassel-common = %version

%description client
A modern, cross-platform, distributed IRC client - Client only

%files client
%defattr(-,root,root)
%{_bindir}/quasselclient
%{_kde_applicationsdir}/quasselclient.desktop

#-----------------------------------------------------------------------

%package core
Group: Networking/IRC
Summary: A modern cross-platform distributed IRC client - Core server
Requires: quassel-common = %version

%description core
A modern, cross-platform, distributed IRC client - This is the quassel
core server for clients.

%files core
%defattr(-,root,root)
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
sed -i "s/<distro>/%{product_product}/" %buildroot/%_datadir/apps/quassel/networks.ini

%changelog
* Fri Apr 27 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.8.0-1
+ Revision: 793865
- update to 0.8.0

  + Frank Kober <emuse@mandriva.org>
    - fix some lint errors: descr/summary format, tabs/spcs

* Sun Dec 04 2011 Frank Kober <emuse@mandriva.org> 0.7.3-1
+ Revision: 737604
- new version (containing a critical security fix)

* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 0.7.2-1
+ Revision: 661606
- update to new version 0.7.2

* Sun Oct 03 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.7.1-1mdv2011.0
+ Revision: 582638
- update to 0.7.1

* Sat Sep 18 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.7.0-1mdv2011.0
+ Revision: 579438
- update to 0.7.0

* Tue Aug 17 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.7-0.beta1.1mdv2011.0
+ Revision: 571089
- update to 0.7-beta1
- bump qt4-linguist BR to 4.6.0, quassel client now depends on qt4 >= 4.6.0

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 0.6.1-1mdv2010.1
+ Revision: 537634
- new version 0.6.1

* Thu Mar 04 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6-0.rc1.1mdv2010.1
+ Revision: 514054
- new upstream release 0.6 rc1

* Tue Mar 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6-0.beta1.1mdv2010.1
+ Revision: 513672
- really update
- update to 0.6beta1
- fix file list

* Sun Jan 31 2010 Funda Wang <fwang@mandriva.org> 0.5.2-1mdv2010.1
+ Revision: 498812
- New version 0.5.2

* Sun Nov 22 2009 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.1-1mdv2010.1
+ Revision: 468659
- Clean spec file
- Update to new version 0.5.1

* Fri Oct 16 2009 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.0-1mdv2010.0
+ Revision: 457899
- 0.5.0 final

* Tue Sep 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.5-0.rc1.3mdv2010.0
+ Revision: 451048
- Remove old source
  Use #mandriva channel as default

* Tue Sep 29 2009 Helio Chissini de Castro <helio@mandriva.com> 0.5-0.rc1.2mdv2010.0
+ Revision: 451001
- Provides kde4-irc-client

* Mon Sep 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.5-0.rc1.1mdv2010.0
+ Revision: 432855
- fix version
- Update to 0.5.0Rc1

* Wed Aug 26 2009 Frederik Himpe <fhimpe@mandriva.org> 0.4.3-1mdv2010.0
+ Revision: 421587
- update to new version 0.4.3

* Sun May 31 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.4.2-2mdv2010.0
+ Revision: 381738
- Rebuild against new kde4

* Thu May 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.4.2-1mdv2010.0
+ Revision: 380634
- Update to 0.4.2

* Sun May 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.4.1-3mdv2010.0
+ Revision: 379176
- Use #mandriva-cooker for cooker

* Sun May 24 2009 Funda Wang <fwang@mandriva.org> 0.4.1-2mdv2010.0
+ Revision: 379162
- fix default channel (bug#51158)

* Tue Apr 14 2009 Helio Chissini de Castro <helio@mandriva.com> 0.4.1-1mdv2009.1
+ Revision: 367244
- Update for upstream bugfix release

* Fri Feb 20 2009 Helio Chissini de Castro <helio@mandriva.com> 0.4.0-1mdv2009.1
+ Revision: 343319
- New upstream version

* Thu Feb 12 2009 Helio Chissini de Castro <helio@mandriva.com> 0.3.1.20090212-1mdv2009.1
+ Revision: 339758
- Update with daily git

* Fri Jan 30 2009 Funda Wang <fwang@mandriva.org> 0.3.1.20090128-5mdv2009.1
+ Revision: 335540
- rebuild

* Thu Jan 29 2009 Helio Chissini de Castro <helio@mandriva.com> 0.3.1.20090128-4mdv2009.1
+ Revision: 335290
- Add our default channels
- Separate common components
- Separate monolithic and client/core packages, to avoid confuse users in which one should use
- Added missing requires for sqlite qt4 plugin

* Wed Jan 28 2009 Helio Chissini de Castro <helio@mandriva.com> 0.3.1.20090128-2mdv2009.1
+ Revision: 334926
- Updating with current quassel git HEAD. Quassel is now the official candidate for kde4 / qt client.

* Sun Jan 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.3.1-2mdv2009.1
+ Revision: 331053
- Fix string format error

* Fri Jan 09 2009 Buchan Milne <bgmilne@mandriva.org> 0.3.1-1mdv2009.1
+ Revision: 327394
- New version 0.3.1

* Tue Sep 30 2008 Buchan Milne <bgmilne@mandriva.org> 0.3.0.1-1mdv2009.0
+ Revision: 290173
- import quassel


