#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Format
Summary:	String::Format - sprintf-like string formatting capabilities
Summary(pl):	String::Format - mo�liwo�ci formatowania podobne do sprintf
Name:		perl-String-Format
Version:	1.13
Release:	3
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7a01414e59bc40c44652c921b4793f6f
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::Format lets you define arbitrary printf-like format
sequences to be expanded.  This module would be most useful
in configuration files and reporting tools, where the results
of a query need to be formatted in a particular way.  It was
inspired by mutt's index_format and related directives (see
<http://www.mutt.org/doc/manual/manual-6.html#index_format>).

%description -l pl
Modu� String::Format pozwala na definiowanie dowolnych sekwencji
formatuj�cych w stylu printf. Jest najbardziej u�yteczny w plikach
konfiguracyjnych i narz�dziach raportuj�cych, gdzie wyniki zapyta�
musz� by� sformatowane w okre�lony spos�b. Jest zainspirowany
index_format z mutta i powi�zanymi dyrektywami (wi�cej pod adresem
<http://www.mutt.org/doc/manual/manual-6.html#index_format>).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
