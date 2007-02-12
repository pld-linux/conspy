Summary:	Conspy - remote control of Linux virtual consoles
Summary(pl.UTF-8):   Conspy - zdalne sterowanie wirtualnymi konsolami Linuksa
Name:		conspy
Version:	1.4
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://ace-host.stuart.id.au/russell/files/conspy/%{name}-%{version}.tar.bz2
# Source0-md5:	73dfe14d5eb8f6351f115efbbbc4ed06
URL:		http://ace-host.stuart.id.au/russell/files/conspy/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conspy allows a (possibly remote) user to see what is displayed on a
Linux virtual console, and send keystrokes to it. It only works with
Linux, as far as I know.

It is rather like VNC, but where VNC takes control of a GUI conspy
takes control of a text mode virtual console. Unlike VNC, conspy does
not require a server to be installed prior to being used.

%description -l pl.UTF-8
Conspy pozwala (także zdalnemu) użytkownikowi patrzeć, co jest
wyświetlane na wirtualnej konsoli Linuksa i wysyłać na nią wciśnięcia
klawiszy. Jak na razie działa tylko z Linuksem.

Przypomina nieco VNC, ale o ile VNC przejmuje kontrolę nad
środowiskiem graficznym, conspy przejmuje kontrolę nad wirtualną
konsolą w trybie tekstowym. W przeciwieństwie do VNC conspy nie wymaga
zainstalowania serwera przed używaniem.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	 CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/conspy
%{_mandir}/man1/*
