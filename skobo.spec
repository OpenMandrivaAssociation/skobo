Summary:	Kobo Deluxe is an SDL port of Akira Higuchi's game XKobo 
Name:		skobo
Version:	0.4.1
%define release %mkrel 2
Release:	%{release}
License:	GPL
Group:		Games/Arcade
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.olofson.net/kobodl/
Source0:	http://olofson.net/kobodl/download/KoboDeluxe-%{version}.tar.bz2
Source5:	%{name}-16.png
Source6:	%{name}-32.png
Source7:	%{name}-48.png
Patch0:		skobo-0.4pre10-gcc4.patch.bz2
Patch1:		KoboDeluxe-0.4.1-various-from-debian.patch
Patch2:		KoboDeluxe-0.4pre10-fix-segfault-in-midi.patch.bz2
BuildRequires: SDL_image-devel
BuildRequires: libmesaglu-devel

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
%patch1 -p1
%patch2 -p1

%build
%configure2_5x	--bindir=%{_gamesbindir}
%make kobo_scoredir=%{_localstatedir}/games/%{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_localstatedir}/games/%{name}
%makeinstall_std kobo_scoredir=%{_localstatedir}/games/%{name}


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

%post 
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc COPYING* ChangeLog README* TODO
%attr(2755, root, games) %{_gamesbindir}/kobodl
%attr(775, root, games) %{_localstatedir}/games/%{name}
%{_datadir}/kobo-deluxe
%{_mandir}/man6/*
%{_datadir}/applications/*
%{_iconsdir}/*.png
%{_miconsdir}/*
%{_liconsdir}/*
