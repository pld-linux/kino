Summary:	DV editing utility
Summary(pl):	Narzêdzie do edycji DV
Name:		kino
Version:	0.7.5
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://kino.schirmacher.de/filemanager/download/42/%{name}-%{version}.tar.gz
# Source0-md5:	592f90be63feb7e63940cedd68edcf79
Patch0:		%{name}-desktop.patch
URL:		http://kino.schirmacher.de/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libavc1394-devel >= 0.4.1
BuildRequires:	libdv-devel >= 0.102
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libsamplerate-devel >= 0.0.14
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
Requires:	libavc1394 >= 0.4.1
Requires:	libdv >= 0.102
Requires:	libglade2 >= 2.0
Requires:	libgnomeui >= 2.0
Requires:	libsamplerate >= 0.0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	hotplug
Requires:	%{name} = %{version}

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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post jogshuttle 
hotplug-update-usb.usermap

%postun jogshuttle 
hotplug-update-usb.usermap

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}/*.xpm
%{_datadir}/%{name}/*.glade
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.jpeg
%{_datadir}/%{name}/help
%attr(755,root,root) %{_datadir}/%{name}/scripts
%{_desktopdir}/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/kino

%files jogshuttle
%defattr(644,root,root,755)
%attr(755,root,root) %{_sysconfdir}/hotplug/usb/*
%{_libdir}/hotplug/kino
