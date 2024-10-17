%define major	0
%define libname	%mklibname %{name} %{major}

Name:		eventlog
Version:	0.2.12
Release:	3
Summary:	Replacement for syslog API
License:	GPL
Group:		System/Libraries
URL:		https://www.balabit.com/products/syslog_ng/
Source:     http://www.balabit.com/downloads/files/eventlog/0.2/%{name}_%{version}.tar.gz

%description
The EventLog library aims to be a replacement of the simple syslog() API
provided on UNIX systems. The major difference between EventLog and syslog
is that EventLog tries to add structure to messages.

Where you had a simple non-structrured string in syslog() you have a
combination of description and tag/value pairs.

EventLog provides an interface to build, format and output an event record.
The exact format and output method can be customized by the administrator
via a configuration file.

%package -n	%{libname}
Group:		Development/Other
Summary:	Replacement for syslog API

%description -n	%{libname}
The EventLog library aims to be a replacement of the simple syslog() API
provided on UNIX systems. The major difference between EventLog and syslog
is that EventLog tries to add structure to messages.

Where you had a simple non-structrured string in syslog() you have a
combination of description and tag/value pairs.

EventLog provides an interface to build, format and output an event record.
The exact format and output method can be customized by the administrator
via a configuration file.

%package -n	%{libname}-devel
Group:		Development/Other
Summary:	Replacement for syslog API
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libname}-devel
The EventLog library aims to be a replacement of the simple syslog() API
provided on UNIX systems. The major difference between EventLog and syslog
is that EventLog tries to add structure to messages.

Where you had a simple non-structrured string in syslog() you have a
combination of description and tag/value pairs.

EventLog provides an interface to build, format and output an event record.
The exact format and output method can be customized by the administrator
via a configuration file.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall

%files -n %{libname}
%{_libdir}/libevtlog*so.*

%files -n %{libname}-devel
%{_includedir}/eventlog
%{_libdir}/libevtlog.a
%{_libdir}/libevtlog.so
%{_libdir}/pkgconfig/eventlog.pc

