%define	name	eventlog
%define	version	0.2.7
%define	release	%mkrel 1
%define major	0
%define libname	%mklibname %{name} %{major}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Replacement for syslog API
URL:		http://www.balabit.com/products/syslog_ng/
Source:     http://www.balabit.com/downloads/files/syslog-ng/sources/stable/src/%{name}-%{version}.tar.gz
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
License:	GPL
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
License:	GPL
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
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc README AUTHORS ChangeLog COPYING CREDITS NEWS PORTS VERSION
%{_libdir}/libevtlog*so.*

%files -n %{libname}-devel
%defattr (-,root,root)
%{_includedir}/eventlog
%{_libdir}/libevtlog.a
%{_libdir}/libevtlog.la
%{_libdir}/libevtlog.so
%{_libdir}/pkgconfig/eventlog.pc


