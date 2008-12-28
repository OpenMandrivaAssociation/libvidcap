%define major		1
%define libname		%mklibname vidcap %{major}
%define develname	%mklibname vidcap -d

Name:		libvidcap
Version:	0.2.1
Release:	%{mkrel 2}
Summary:	Video capture library
Group:		System/Libraries
URL:		http://sourceforge.net/projects/%{name}
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
License:	LGPLv2+
BuildRoot:	%{_tmppath}/%{name}-root

%description
libvidcap is a cross-platform library for capturing video from webcams
and other video capture devices. 

%package -n %{libname}
Summary:	Video capture library
Group:		System/Libraries

%description -n %{libname}
libvidcap is a cross-platform library for capturing video from webcams
and other video capture devices. 

%package -n %{develname}
Summary:	Development headers and libraries for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
libvidcap is a cross-platform library for capturing video from webcams
and other video capture devices. 

%prep
%setup -q

%build
# or else it doesn't link right against libpthread...
export PTHREAD_LIBS="-lpthread"
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.*a
%{_includedir}/vidcap
%{_libdir}/pkgconfig/*.pc

