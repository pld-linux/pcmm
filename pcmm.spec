Summary:	Portos Commander is a QT file manager for Linux
Summary(pl):	Portos Commander jest opartym na QT zarz±dc± plików pod Linuksa
Name:		pcmm
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/pcmm/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Patch0:		%{name}-desktop.patch
URL:		http://pcmm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Portos Commander (Pcmm) is a linux file manager for KDE 3.x. It is
patterned after old-school managers like Midnight Commander and Norton
Commander. It features basically all your file-management needs, file
searcher, internal viewer, URL database, ftp.

%description -l pl
Portos Commander (Pcmm) jest zarz±dc± plików przeznaczonym dla KDE
3.x. Jest wzorowany na takich programach jak Midnight Commander i
Norton Commander. W obs³udze jest bardzo prosty i zapewnia dostêp
podstawowych funkcji zarz±dcy plików, które obejmuj± m. in.:
wyszukiwanie plików, wbudowan± przegl±darkê, ftp.

%prep
%setup -q
%patch -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure \
	--disable-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir} \
	kde_icondir=%{_pixmapsdir}

mv -f $RPM_BUILD_ROOT%{_applnkdir}/{Applications,Utilities}/pcmm.desktop
rm -rf $RPM_BUILD_ROOT%{_applnkdir}/Applications
install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog TODO AUTHORS
%attr(755,root,root) %{_bindir}/%{name}
%{_applnkdir}/Utilities/pcmm.desktop
%dir %{_datadir}/apps/pcmm
%{_datadir}/apps/pcmm/pcmmui.rc
%{_pixmapsdir}/*.png
%{_pixmapsdir}/*color/*/*
