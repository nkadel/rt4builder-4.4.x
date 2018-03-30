Name:           perl-HTTP-CookieJar
Version:        0.006
#Release:        4%{?dist}
Release:        0.1%{?dist}
Summary:        Minimalist HTTP user agent cookie jar
License:        ASL 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTTP-CookieJar/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/HTTP-CookieJar-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl >= 5.10
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mozilla::PublicSuffix)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Time::Local) >= 1.1901
BuildRequires:  perl(Time::Mock)
BuildRequires:  perl(URI)
BuildRequires:  perl(strict), perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module implements a minimalist HTTP user agent cookie jar in
conformance with RFC 6265.

%prep
%setup -q -n HTTP-CookieJar-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if ! 0%{?rhel}
make test
%endif

%files
%doc Changes CONTRIBUTING LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 28 2018 Nico Kadel-Garcia <nkadel@gmail.com> - 0.006=0.1
- Disable checks on RHEL

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-3
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-2
- Perl 5.20 rebuild

* Tue Jul 15 2014 Yanko Kaneti <yaneti@declera.com> 0.006-1
- Update to 0.006

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 26 2013 Yanko Kaneti <yaneti@declera.com> 0.005-1
- Update to 0.005

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.004-3
- Perl 5.18 rebuild

* Fri May 17 2013 Yanko Kaneti <yaneti@declera.com> 0.004-2
- Address review comments. (#963213#c1)

* Tue May 14 2013 Yanko Kaneti <yaneti@declera.com> 0.004-1
- Specfile autogenerated by cpanspec 1.78 and tweaked for submission
