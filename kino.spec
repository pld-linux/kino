Summary:	DV editing utility
Summary(pl):	Narzędzie do edycji DV
Name:		kino
Version:	0.7.0
Release:	1
License:	GPL
Group:		Applications/Multimedia
URL:		http://kino.schirmacher.de/
Source0:	http://kino.schirmacher.de/filemanager/download/17/%{name}-%{version}.tar.gz
# Source0-md5:	7caac99c0ebe1d76b835d76137c1e7d7
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libavc1394-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libdv-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kino is an DV non-linear editing utility.

%description -l pl
Kino to narzędzie do nieliniowej edycji DV.

%package devel
Summary:	Development files
Summary(pl):	Pliki dla programistów
Group:		Applications/Multimedia

%description devel
Development files for kino.

%description devel -l pl
Pliki dla programistów używających kina.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
cd libsamplerate
%{__aclocal}
%{__autoconf}
%{__automake}
cd ..
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
%attr(755,root,root) %{_datadir}/%{name}/scripts/exports/*.sh
#%{_pixmapsdir}/kino
%{_mandir}/man1/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/*.xpm
%dir %{_datadir}/%{name}/*.glade
%dir %{_datadir}/%{name}/scripts
%dir %{_datadir}/%{name}/scripts/exports

%files devel
%defattr(644,root,root,755)
%attr(655,root,root) %{_includedir}/kino
