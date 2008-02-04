Summary:	telepathy-qt
Summary(pl.UTF-8):   telepathy-qt
Name:		telepathy-qt
Version:	0.14.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://mesh.dl.sourceforge.net/sourceforge/tapioca-voip/%{name}-%{version}.tar.gz
# Source0-md5:	476e3fbd68b3eaf5354559be7de99333
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
telepathy-qt

%description -l pl.UTF-8
telepathy-qt

%package devel
Summary:	Header files for telepathy-qt libraries
Summary(pl.UTF-8):   Pliki nagłówkowe bibliotek telepathy-qt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for telepathy-qt libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek telepathy-qt

%prep
%setup -q

%build
export QTDIR=%{_prefix}
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

#%find_lang juk		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%ghost %attr(755,root,root) %{_libdir}/libQtTelepathyClient.so.?
%attr(755,root,root) %{_libdir}/libQtTelepathyClient.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/libQtTelepathyCommon.so.?
%attr(755,root,root) %{_libdir}/libQtTelepathyCommon.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/libQtTelepathyCore.so.?
%attr(755,root,root) %{_libdir}/libQtTelepathyCore.so.*.*.*
%attr(755,root,root) %{_libdir}/pkgconfig/QtTelepathyClient.pc
%attr(755,root,root) %{_libdir}/pkgconfig/QtTelepathyCommon.pc
%attr(755,root,root) %{_libdir}/pkgconfig/QtTelepathyCore.pc
                                    

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQtTelepathyClient.so
%attr(755,root,root) %{_libdir}/libQtTelepathyCommon.so
%attr(755,root,root) %{_libdir}/libQtTelepathyCore.so
%dir %{_includedir}/QtTelepathy
%{_includedir}/QtTelepathy/Common
%{_includedir}/QtTelepathy/Core
%{_includedir}/QtTelepathy/Client
