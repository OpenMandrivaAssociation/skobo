Summary:	SDL port of Akira Higuchis game XKobo 
Name:		skobo
Version:	0.5.1
Release:	16
License:	GPL
Group:		Games/Arcade
URL:		https://www.olofson.net/kobodl/
Source0:	http://olofson.net/kobodl/download/KoboDeluxe-%{version}.tar.bz2
Source5:	%{name}-16.png
Source6:	%{name}-32.png
Source7:	%{name}-48.png
Patch0:		skobo-0.4pre10-gcc4.patch
Patch2:		KoboDeluxe-0.4pre10-fix-segfault-in-midi.patch
Patch3:		04_enemies-pipe-decl.patch
Patch4:		skobo-0.5.1-gcc44.patch
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(glu)
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

# I doubt we need a -devel...
rm -f %{buildroot}%{_datadir}/kobo-deluxe/sfx/kobosfx.h

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
