#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Format
Summary:	String::Format - sprintf-like string formatting capabilities
Summary(pl):	String::Format - mo¿liwo¶ci formatowania podobne do sprintf
Name:		perl-String-Format
Version:	1.13
Release:	2
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
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
Modu³ String::Format pozwala na definiowanie dowolnych sekwencji
formatuj±cych w stylu printf. Jest najbardziej u¿yteczny w plikach
konfiguracyjnych i narzêdziach raportuj±cych, gdzie wyniki zapytañ
musz± byæ sformatowane w okre¶lony sposób. Jest zainspirowany
index_format z mutta i powi±zanymi dyrektywami (wiêcej pod adresem
<http://www.mutt.org/doc/manual/manual-6.html#index_format>).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
