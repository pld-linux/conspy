Summary:	Conspy - remote control of Linux virtual consoles
Summary(pl):	Conspy - zdalne sterowanie wirtualnymi konsolami Linuksa
Name:		conspy
Version:	1.3
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://ace-host.stuart.id.au/russell/files/conspy/%{name}-%{version}.tar.bz2
# Source0-md5:	3d018e911452850ceb08899add5adacc
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

%description -l pl
Conspy pozwala (tak¿e zdalnemu) u¿ytkownikowi patrzeæ, co jest
wy¶wietlane na wirtualnej konsoli Linuksa i wysy³aæ na ni± wci¶niêcia
klawiszy. Jak na razie dzia³a tylko z Linuksem.

Przypomina nieco VNC, ale o ile VNC przejmuje kontrolê nad
¶rodowiskiem graficznym, conspy przejmuje kontrolê nad wirtualn±
konsol± w trybie tekstowym. W przeciwieñstwie do VNC conspy nie wymaga
zainstalowania serwera przed u¿ywaniem.

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
