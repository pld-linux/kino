Summary:	DV editing utility
Name:		kino
Version:	0.6.4
Release:	0.1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://kino.schirmacher.de/filemanager/download/6/%{name}-%{version}.tar.gz
BuildRequires:	libavc1394-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kino is an DV non-linear editing utility.

%package devel
Summary:	Development files
Group:		Applications/Multimedia

%description devel
Development files for kino.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_pixmapsdir}/kino/*
%doc %{_datadir}/gnome/help/kino/C/*
%doc %{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(655,root,root) %{_includedir}/kino/*
