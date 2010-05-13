Summary:	Common modules for GNOME JavaScript bindings
Summary(pl.UTF-8):	Wspólne moduły dla wiązań JavaScript do GNOME
Name:		gnome-js-common
Version:	0.1.2
Release:	1
License:	GPL v3
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-js-common/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	a4147d24622ab0f1d01e9921a3bf501b
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides common modules for GNOME JavaScript bindings.

%description -l pl.UTF-8
Ten pakiet dostarcza wspólne moduły dla wiązań JavaScript do GNOME.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/gnome_js_common

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/gnome-js
%{_pkgconfigdir}/gnome-js-common.pc
