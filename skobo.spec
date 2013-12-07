Summary:	SDL port of Akira Higuchis game XKobo 
Name:		skobo
Version:	0.5.1
Release:	7
License:	GPL
Group:		Games/Arcade
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.olofson.net/kobodl/
Source0:	http://olofson.net/kobodl/download/KoboDeluxe-%{version}.tar.bz2
Source5:	%{name}-16.png
Source6:	%{name}-32.png
Source7:	%{name}-48.png
Patch0:		skobo-0.4pre10-gcc4.patch
# Patch1:		KoboDeluxe-0.4.1-various-from-debian.patch
Patch2:		KoboDeluxe-0.4pre10-fix-segfault-in-midi.patch
Patch3:		04_enemies-pipe-decl.patch
Patch4:		skobo-0.5.1-gcc44.patch
BuildRequires: SDL_image-devel
BuildRequires: libmesaglu-devel
Provides:	KoboDeluxe = %version
Provides:	kobodeluxe = %version

%description
Kobo Deluxe is an SDL port of Akira Higuchi's game XKobo. It adds sound,
smoother animation, filtered high resolution support, a more intuitive menu
driven user interface, joystick support and other features, and runs on most
of the major operating systems. Kobo Deluxe uses the Free/Open Source
libraries SDL and SDL_image, which can be downloaded (source as well as
binaries for various platforms) from http://www.libsdl.org.

%prep
%setup -q -n KoboDeluxe-%{version}
%patch0 -p0 -b .gcc4
# %patch1 -p1
%patch2 -p1
%patch3 -p1 -b .debian
%patch4 -p0 -b .gcc44

%build
%configure2_5x	--bindir=%{_gamesbindir}
%make kobo_scoredir=%{_localstatedir}/lib/games/%{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_localstatedir}/lib/games/%{name}
%makeinstall_std kobo_scoredir=%{_localstatedir}/lib/games/%{name}


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Kobo Deluxe
Comment=Arcade video game
Exec=%_gamesbindir/kobodl
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

install -D -m644 %SOURCE6 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -D -m644 %SOURCE5 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -D -m644 %SOURCE7 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post 
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc COPYING* ChangeLog README* TODO
%attr(2755, root, games) %{_gamesbindir}/kobodl
%attr(775, root, games) %{_localstatedir}/lib/games/%{name}
%{_datadir}/kobo-deluxe
%{_mandir}/man6/*
%{_datadir}/applications/*
%{_iconsdir}/*.png
%{_miconsdir}/*
%{_liconsdir}/*


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-5mdv2011.0
+ Revision: 669983
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-4mdv2011.0
+ Revision: 607540
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-3mdv2010.1
+ Revision: 524104
- rebuilt for 2010.1

* Sun Oct 04 2009 Funda Wang <fwang@mandriva.org> 0.5.1-2mdv2010.0
+ Revision: 453292
- fix build with gcc 44
- bunzip2 patches

  + Christophe Fergeau <cfergeau@mandriva.com>
    - Import debian patch to fix compilation

* Sun Dec 28 2008 Zombie Ryushu <ryushu@mandriva.org> 0.5.1-1mdv2009.1
+ Revision: 320092
- New Version
- Bump to Version 0.5.1

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.4.1-3mdv2009.0
+ Revision: 218430
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
- adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.4.1-3mdv2008.1
+ Revision: 171108
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix no-buildroot-tag
- drop old menu
- kill re-definition of %%buildroot on Pixel's request

* Fri Nov 30 2007 Pixel <pixel@mandriva.com> 0.4.1-2mdv2008.1
+ Revision: 114132
- build with opengl support
  (nb: program doesn't build correctly without opengl support)
- new release
- rediff patch

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Fri Aug 10 2007 Pixel <pixel@mandriva.com> 0.4-0.pre10.8mdv2008.0
+ Revision: 61312
- rebuild
- Import skobo



* Fri Jul  7 2006 Pixel <pixel@mandriva.com> 0.4-0.pre10.7mdv2007.0
- switch to XDG menu
- fix some more segfaulting in midi code (but still segfaulting on exit...)

* Fri May 26 2006 Pixel <pixel@mandriva.com> 0.4-0.pre10.6mdv2007.0
- use std mkrel

* Fri May 26 2006 Pixel <pixel@mandriva.com> 0.4-0.pre10.5mdv
- fix segfaulting in midi code (but still segfaulting on exit...)
- add patches from debian

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.4-0.pre10.4mdk
- Rebuild

* Tue Aug 02 2005 Guillaume Bedot <littletux@mandriva.org> 0.4-0.pre10.3mdk
- Patch0: to build with gcc4
- use mkrel

* Sat Jul 30 2005 Guillaume Bedot <littletux@mandriva.org> 0.4-0.pre10.2mdk
- Fixed previous changelog versions
- Dropped Patch0 (applied upstream, well that was in 1mdk too) 

* Sat Jul 30 2005 Guillaume Bedot <littletux@mandriva.org> 0.4-0.pre10.1mdk
- New version
- Added man page
- Build with gcc3.3

* Fri Jun  4 2004  <lmontel@n2.mandrakesoft.com> 0.4-0.pre8.13mdk
- Rebuild

* Tue Oct 21 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.4-0.8.12mdk
- varargs fixes

* Tue Jul 15 2003 Götz Waschk <waschk@linux-mandrake.com> 0.4-0.pre8.11mdk
- fix url
- revert patch change from 8mdk, caused a segfault

* Tue Jul 15 2003 Götz Waschk <waschk@linux-mandrake.com> 0.4-0.pre8.10mdk
- don't remove the .h file, it's needed!!!

* Tue Jul 15 2003 Götz Waschk <waschk@linux-mandrake.com> 0.4-0.pre8.9mdk
- use the right icon in the menu

* Tue Jul 15 2003 Götz Waschk <waschk@linux-mandrake.com> 0.4-0.pre8.8mdk
- remove included devel file (for rpmlint)
- always apply the patch (for rpmlint)
- move menu to the spec file
- fix menu entry
- remove empty dir
- don't obsolete xkobo (by request of rrowan@dandy.net)
- configure2_5x macro

* Mon Jul 14 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.4-0.pre8.7mdk
- don't rm -rf $RPM_BUILD_ROOT in %%prep
- use %%{_gamesbindir}

* Wed Oct 30 2002 Stew Benedict <sbenedict@mandrakesoft.com> 0.4-0.pre8.6mdk
- Patch getargs on PPC build (patch0)

* Tue Oct 29 2002 Stefan van der Eijk <stefan@eijk.nu> 0.4-0.pre8.5mdk
- BuildRequires: SDL_image-devel

* Tue Aug 27 2002 David BAUDENS <baudens@mandrakesoft.com> 0.4-0.pre8.4mdk
- Fix icon (menu)

* Fri Aug 16 2002 Pixel <pixel@mandrakesoft.com> 0.4-0.pre8.3mdk
- fix permissions for scores dir (thanks to Goetz Waschk)

* Thu Aug 15 2002 Pixel <pixel@mandrakesoft.com> 0.4-0.pre8.2mdk
- rebuild for new libstdc++

* Wed Aug 14 2002 Pixel <pixel@mandrakesoft.com> 0.4-0.pre8.1mdk
- initial spec
