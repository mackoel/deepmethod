Name:		deepmethod
Version:	2.2.0
Release:	0%{?dist}
Summary:	Differential Evolution Entirely Parallel method

Group:		Science
License:	GPLv3
URL:		http://sourceforge.net/projects/deepmethod/
Source0:	http://sourceforge.net/projects/deepmethod/files/%{name}-%{version}.tar.gz
#BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:	glib2
BuildRequires:	glib2-devel
BuildRequires:	intltool

%description
Differential Evolution Entirely Parallel method

%package openmpi
Summary:        DEEP openmpi
Group:          Science
Requires:	openmpi
BuildRequires:	python-libs
BuildRequires:	infinipath-psm
#BuildRequires:	libpsm2-compat
BuildRequires:	openmpi-devel
BuildRequires:	environment-modules

%description openmpi
Differential Evolution Entirely Parallel method with openmpi

%package devel
Summary:        DEEP development
Group:          Science
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for DEEP.

%package openmpi-devel
Summary:        DEEP development with OpenMPI
Group:          Science
Requires:       %{name} = %{version}-%{release}

%description openmpi-devel
Development files for DEEP with OpenMPI.

%prep
%setup -q

%build
%configure --enable-mpi-build-target --with-mpi="%{_libdir}/openmpi"
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%make_install

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc %{_docdir}
%{_bindir}/deepmethod
%{_libdir}/libdeep.so
%{_libdir}/libdeep.so.*
%{_libdir}/libxmod.so
%{_libdir}/libxmod.so.*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files openmpi
%defattr(-,root,root,-)
%{_bindir}/deepmethod_openmpi
%{_libdir}/libdeep_openmpi.so
%{_libdir}/libdeep_openmpi.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libdeep
%{_includedir}/libxmod
%{_libdir}/pkgconfig/libdeep-1.0.pc
%{_libdir}/pkgconfig/libxmod-1.0.pc
%{_libdir}/libdeep.a
%{_libdir}/libdeep.la
%{_libdir}/libxmod.a
%{_libdir}/libxmod.la

%files openmpi-devel
%defattr(-,root,root,-)
%{_libdir}/libdeep_openmpi.a
%{_libdir}/libdeep_openmpi.la
%{_libdir}/pkgconfig/libdeep_openmpi-1.0.pc

%changelog
* Tue Jul 26 2017 Kozlov Konstantin <mackoel@gmail.com> - 2.2.0-0
- Next version and fix for infinipath

* Tue Feb 17 2017 Kozlov Konstantin <mackoel@gmail.com> - 2.1.0-0
- Next version

* Sat Jul 23 2016 Kozlov Konstantin <mackoel@gmail.com> - 2.0.2-1
- Added environment-modules for F24

* Tue Jul 06 2016 Kozlov Konstantin <mackoel@gmail.com> - 2.0.2-0
- Next version

* Tue Jun 06 2016 Kozlov Konstantin <mackoel@gmail.com> - 2.0.1-0
- May restart form logged params as the best

* Tue May 17 2016 Kozlov Konstantin <mackoel@gmail.com> - 2.0.0-0
- Next release

* Wed Jun 24 2015 Kozlov Konstantin <mackoel@gmail.com> - 1.2.0-0
- Third release

* Mon Jun 01 2015 Kozlov Konstantin <mackoel@gmail.com> - 1.1.0-0
- Second release

* Mon Feb 16 2015 Kozlov Konstantin <mackoel@gmail.com> - 1.0.0-0
- First release

