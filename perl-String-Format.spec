#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	String
%define		pnam	Format
Summary:	String::Format - sprintf-like string formatting capabilities
Summary(pl.UTF-8):	String::Format - możliwości formatowania podobne do sprintf
Name:		perl-String-Format
Version:	1.18
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/String/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	64174b4fac230228cadfa2be4410ef1a
URL:		http://search.cpan.org/dist/String-Format/
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Moduł String::Format pozwala na definiowanie dowolnych sekwencji
formatujących w stylu printf. Jest najbardziej użyteczny w plikach
konfiguracyjnych i narzędziach raportujących, gdzie wyniki zapytań
muszą być sformatowane w określony sposób. Jest zainspirowany
index_format z mutta i powiązanymi dyrektywami (więcej pod adresem
<http://www.mutt.org/doc/manual/manual-6.html#index_format>).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/String/Format.pm
%{_mandir}/man3/String::Format.3pm*
