Summary:	DV editing utility
Summary(pl):	Narzêdzie do edycji DV
Name:		kino
Version:	0.7.1
Release:	0.5
License:	GPL
Group:		Applications/Multimedia
Source0:	http://kino.schirmacher.de/filemanager/download/31/%{name}-%{version}.tar.gz
# Source0-md5:	0980dd4ccf2d2282578f6bcb51d768e8
#Patch0:		%{name}-system-samplerate.patch
URL:		http://kino.schirmacher.de/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libavc1394-devel >= 0.4.1
BuildRequires:	libdv-devel >= 0.98
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libsamplerate-devel >= 0.0.14
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
Requires:	libavc1394 >= 0.4.1
Requires:	libdv >= 0.98
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

%prep
%setup -q
#%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.xpm
%{_datadir}/%{name}/*.glade
%attr(755,root,root) %{_datadir}/%{name}/scripts

%files devel
%defattr(644,root,root,755)
%{_includedir}/kino
