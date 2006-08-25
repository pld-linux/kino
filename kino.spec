# TODO
# - fix build on big-endians
Summary:	DV editing utility
Summary(pl):	Narzêdzie do edycji DV
Name:		kino
Version:	0.9.0
Release:	2
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/kino/%{name}-%{version}.tar.gz
# Source0-md5:	95c6a550f1f3462efac639132ab6f990
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-segfault_empty_chapter.patch
Patch2:		%{name}-fix_avi_packing.patch
Patch3:		%{name}-fix_no_mplex.patch
Patch4:		%{name}-fix_bigendian_warning.patch
Patch5:		%{name}-externc.patch
URL:		http://www.kinodv.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libavc1394-devel >= 0.4.1
BuildRequires:	libdv-devel >= 0.102
BuildRequires:	libglade2-devel >= 2.5
BuildRequires:	libsamplerate-devel >= 0.0.14
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.315
Requires(post,postun):	shared-mime-info
Requires:	gtk+2 >= 2:2.6.0
Requires:	libavc1394 >= 0.4.1
Requires:	libdv >= 0.102
Requires:	libglade2 >= 2.5
Requires:	libsamplerate >= 0.0.14
Requires:	shared-mime-info
ExcludeArch:	ppc sparc sparcv9 sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define                filterout_ld    -Wl,--as-needed

%description
Kino is an DV non-linear editing utility.

%description -l pl
Kino to narzêdzie do nieliniowej edycji DV.

%package devel
Summary:	Development files for Kino plugins
Summary(pl):	Pliki dla programistów wtyczek Kina
Group:		Applications/Multimedia
Requires:	libstdc++-devel

%description devel
Development files for Kino plugins.

%description devel -l pl
Pliki dla programistów tworz±cych wtyczki Kina.

%package jogshuttle
Summary:	Kino support for jogshuttle input devices
Summary(pl):	Obs³uga urz±dzeñ jogshuttle dla Kino
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	hotplug

%description jogshuttle
Jog/Shuttles are devices made especially for working with streams of
data, such as Video or Audio. In theory, Kino should work with any
(usb) Jog/Shuttle devices that supports the USB HID v1.10 Pointer
profile.

%description jogshuttle -l pl
Urz±dzenia Jog/Shuttle s± specjalnie przystosowane do pracy ze
strumieniami danych takimi jak d¼wiêk lub wideo. Teoretycznie, program
Kino powinien pracowaæ z dowolnym urz±dzeniem Jog/Shuttle wspieraj±cym
standard USB HID v1.10.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# use lib64 when needed
sed -i -e 's|lib/kino-gtk2|%{_lib}/kino-gtk2|' src/*/Makefile.am

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-hotplug-script-dir=%{_sysconfdir}/hotplug/usb \
	--with-hotplug-usermap-dir=%{_libdir}/hotplug/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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

%post jogshuttle
hotplug-update-usb.usermap

%postun jogshuttle
hotplug-update-usb.usermap

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
%{_desktopdir}/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/kino

%files jogshuttle
%defattr(644,root,root,755)
%doc README_jogshuttle
%attr(755,root,root) %{_sysconfdir}/hotplug/usb/*
%{_libdir}/hotplug/kino
