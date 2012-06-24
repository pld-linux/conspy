Summary:	Conspy - remote control of Linux virtual consoles
Name:		conspy
Version:	1.2
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://ace-host.stuart.id.au/russell/files/conspy/%{name}-%{version}.tar.bz2
# Source0-md5:	dffa52755840187958adba42915a57d6
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
