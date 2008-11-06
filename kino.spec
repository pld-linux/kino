# TODO
# - fix as-needed
#
Summary:	DV editing utility
Summary(pl.UTF-8):	Narzędzie do edycji DV
Name:		kino
Version:	1.3.2
Release:	3
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/kino/%{name}-%{version}.tar.gz
# Source0-md5:	c534c666ed0312c75c877eb1580b985c
Patch0:		%{name}-desktop.patch
URL:		http://www.kinodv.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool
BuildRequires:	libavc1394-devel >= 0.4.1
BuildRequires:	libdv-devel >= 0.102
BuildRequires:	libiec61883-devel
BuildRequires:	libglade2-devel >= 1:2.5
BuildRequires:	libsamplerate-devel >= 0.0.14
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.315
BuildRequires:	xorg-lib-libXv-devel
Requires(post,postun):	shared-mime-info
Requires:	gtk+2 >= 2:2.6.0
Requires:	libavc1394 >= 0.4.1
Requires:	libdv >= 0.102
Requires:	libglade2 >= 1:2.5
Requires:	libsamplerate >= 0.0.14
Requires:	shared-mime-info
Suggests:	dvdauthor
Suggests:	ffmpeg
Suggests:	qdvdauthor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_ld	-Wl,--as-needed

%description
Kino is an DV non-linear editing utility.

%description -l pl.UTF-8
Kino to narzędzie do nieliniowej edycji DV.

%package devel
Summary:	Development files for Kino plugins
Summary(pl.UTF-8):	Pliki dla programistów wtyczek Kina
Group:		Applications/Multimedia
Requires:	libstdc++-devel

%description devel
Development files for Kino plugins.

%description devel -l pl.UTF-8
Pliki dla programistów tworzących wtyczki Kina.

%package jogshuttle
Summary:	Kino support for jogshuttle input devices
Summary(pl.UTF-8):	Obsługa urządzeń jogshuttle dla Kino
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	udev-core

%description jogshuttle
Jog/Shuttles are devices made especially for working with streams of
data, such as Video or Audio. In theory, Kino should work with any
(usb) Jog/Shuttle devices that supports the USB HID v1.10 Pointer
profile.

%description jogshuttle -l pl.UTF-8
Urządzenia Jog/Shuttle są specjalnie przystosowane do pracy ze
strumieniami danych takimi jak dźwięk lub wideo. Teoretycznie, program
Kino powinien pracować z dowolnym urządzeniem Jog/Shuttle wspierającym
standard USB HID v1.10.

%prep
%setup -q
%patch0 -p0

# use lib64 when needed
sed -i -e 's|lib/kino-gtk2|%{_lib}/kino-gtk2|' src/*/Makefile.am

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-x \
	--with-libdv-only \
	--disable-local-ffmpeg \
	--enable-udev-rules-dir=%{_sysconfdir}/udev/rules.d
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# broken symlink, create it manually:
ln -sf kino $RPM_BUILD_ROOT%{_bindir}/kino2raw
# it seems to be more Danish than Norwegian; current Norwegian is in nb
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/no
rm -f $RPM_BUILD_ROOT%{_libdir}/kino-gtk2/*.{a,la}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
update-mime-database %{_datadir}/mime >/dev/null 2>&1 ||:
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
if [ $1 = 0 ]; then
	umask 022
	update-mime-database %{_datadir}/mime >/dev/null 2>&1
	[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/kino-gtk2
%attr(755,root,root) %{_libdir}/kino-gtk2/lib*.so*
%{_mandir}/man1/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/lumas
%{_datadir}/%{name}/*.xpm
%{_datadir}/%{name}/*.glade
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.jpeg
%{_datadir}/%{name}/help
%attr(755,root,root) %{_datadir}/%{name}/scripts
%{_datadir}/mime/packages/*.xml
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/kino

%files jogshuttle
%defattr(644,root,root,755)
%doc README_jogshuttle
%attr(755,root,root) /etc/udev/rules.d/kino.rules
