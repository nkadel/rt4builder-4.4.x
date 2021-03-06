Name:           perl-Module-Mask
Version:        0.04
Release:        0.1%{?dist}
Summary:        Pretend certain modules are not installed
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Mask/
Source0:        http://www.cpan.org/authors/id/M/MA/MATTLAW/Module-Mask-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:5.8.0
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Compat) >= 0.02
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(Module::Util) >= 1.00
BuildRequires:  perl(Scalar::Util) >= 1.01
# Tests
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
# Needed for filter-requires "/d" syntax
%if 0%{?rhel}
BuildRequires:   redhat-rpm-config
%endif

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Module::Util) >= 1.00

# RPM 4.8 style
%{?perl_default_filter:
# Replace unversioned dependencies with versioned ones.
%filter_from_requires /^perl(Module::Util)$/d
%perl_default_filter
}
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Util\\)$

%description
Sometimes you need to test what happens when a given module is not
installed. This module provides a way of temporarily hiding installed
modules from perl's require mechanism. The Module::Mask object adds itself
to @INC and blocks require calls to restricted modules.

%prep
%setup -q -n Module-Mask-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Nov 30 2013 Nico  Kadel-Garcia <nkadel@gmail.com> - 0.04-0.2
- Add BuldRequired for r redhat-rpm-config on RHEL

* Wed Mar 13 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholsatic.com> - 0.04-0.1
- Roll back release to avoid update conflicts.
- Add PerlRequires: perl(Test::Harness) to build under mock.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.04-2
- Perl 5.16 rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.04-1
- 0.04 bump (to pass tests)

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.03-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 0.03-3
- RPM 4.9 dependency filtering added

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.03-2
- Perl mass rebuild

* Tue Mar 29 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.03-1
- Specfile autogenerated by cpanspec 1.78.
