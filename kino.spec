Summary:	DV editing utility
Summary(pl):	Narzêdzie do edycji DV
Name:		kino
Version:	0.6.4
Release:	0.1
License:	GPL
Group:		Applications/Multimedia
URL:		http://kino.schirmacher.de/
Source0:	http://kino.schirmacher.de/filemanager/download/6/%{name}-%{version}.tar.gz
# Source0-md5:	f7e504c5f44a16bee106428690c860f2
BuildRequires:	libavc1394-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kino is an DV non-linear editing utility.

%description -l pl
Kino to narzêdzie do nieliniowej edycji DV.

%package devel
Summary:	Development files
Summary(pl):	Pliki dla programistów
Group:		Applications/Multimedia

%description devel
Development files for kino.

%description devel -l pl
Pliki dla programistów u¿ywaj±cych kina.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/kino
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(655,root,root) %{_includedir}/kino
