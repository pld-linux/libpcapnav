#
# Conditional build
%bcond_without	static_libs	# don't build static library
#
Summary:	A libpcap wrapper library
Summary(pl.UTF-8):	Wrapper dla biblioteki libpcap
Name:		libpcapnav
Version:	0.8
Release:	1
License:	Distributable
Group:		Libraries
Source0:	http://dl.sourceforge.net/netdude/libpcapnav/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	005a0a2d6f1164f1212a7c10ab950b36
URL:		http://netdude.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	libpcap-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpcapnav is a libpcap wrapper library that allows navigation to
arbitrary locations in a tcpdump trace file between reads. The API is
intentionally much like that of the pcap library. You can navigate in
trace files both in time and space. You can jump to a packet which is
at approximately 2/3 of the trace, or you can jump as closely as
possible to a packet with a given timestamp, and then read packets
from there. In addition, the API provides convenience functions for
manipulating timeval structures.

%description -l pl.UTF-8
libpcapnav to wrapper dla biblioteki libpcap, który umożliwia
nawigację do arbitralnych lokacji w pliku trace tcpdumpa pomiędzy
odczytami. API z założenia ma wyglądać jak API biblioteki libpcap.
Użytkownik może nawigować w plikach trace zarówno w czasie i
miejscu. Można przeskoczyć bezpośrednio do pakietu, który znajduje
się w przybliżeniu w 2/3 pliku trace lub też tak blisko, jak to
możliwe do pakietu określonego stemplem czasu i odczytać stamtąd
pakiety. Dodatkowo API umożliwia wygodne funkcje do manipulacji
strukturami timeval.

%package devel
Summary:	Header files for libpcapnav library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libpcapnav
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libpcapnav library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libpcapnav.

%package static
Summary:	Static libpcapnav library
Summary(pl.UTF-8):	Statyczna biblioteka libpcapnav
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libpcapnav library.

%description static -l pl.UTF-8
Statyczna biblioteka libpcapnav.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir="%{_gtkdocdir}" \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/pcapnav-config
%attr(755,root,root) %{_libdir}/libpcapnav.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpcapnav.so.0
%{_gtkdocdir}/pcapnav

%files devel
%defattr(644,root,root,755)
%{_libdir}/libpcapnav.so
%{_libdir}/libpcapnav.la
%{_includedir}/pcapnav.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpcapnav.a
%endif
