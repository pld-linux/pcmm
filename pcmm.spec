Summary:	Portos Commander - a Qt file manager for Linux
Summary(pl.UTF-8):   Portos Commander - oparty na Qt zarządca plików pod Linuksa
Name:		pcmm
Version:	1.0
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/pcmm/%{name}-%{version}.tar.gz
# Source0-md5:	54e185bd5c250404409dd19ef0df628c
Source1:	%{name}.png
Source2:        %{name}-po.pl
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-gcc3.patch
Patch2:		%{name}-desktop_dir.patch
Patch3:         %{name}-po_makefile.patch
URL:		http://pcmm.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portos Commander (Pcmm) is a linux file manager for KDE 3.x. It is
patterned after old-school managers like Midnight Commander and Norton
Commander. It features basically all your file-management needs, file
searcher, internal viewer, URL database, FTP.

%description -l pl.UTF-8
Portos Commander (Pcmm) jest zarządcą plików przeznaczonym dla KDE
3.x. Jest wzorowany na takich programach jak Midnight Commander i
Norton Commander. W obsłudze jest bardzo prosty i zapewnia dostęp
podstawowych funkcji zarządcy plików, które obejmują m. in.:
wyszukiwanie plików, wbudowaną przeglądarkę, FTP.

%prep
%setup -q
install %{SOURCE2} po/pl.po
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp -f /usr/share/automake/config.sub admin
kde_appsdir="%{_desktopdir}"; export kde_appsdir
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure \
	--disable-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog TODO AUTHORS
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/pcmm.desktop
%{_datadir}/apps/pcmm
%{_pixmapsdir}/*.png
%{_iconsdir}/hicolor/*/apps/*
