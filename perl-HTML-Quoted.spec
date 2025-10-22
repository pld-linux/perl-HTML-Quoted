#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	Quoted
Summary:	HTML::Quoted - extract structure of quoted HTML mail message
#Summary(pl.UTF-8):	
Name:		perl-HTML-Quoted
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	524dd880e6b1b50f77a0d0a295d021a8
# generic URL, check or change before uncommenting
URL:		http://search.cpan.org/dist/HTML-Quoted/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Parser >= 3.0
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parses and extracts quotation structure out of a HTML message.
Purpose and returned structures are very similar to
Text::Quoted.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/*.pm
%{_mandir}/man3/*
