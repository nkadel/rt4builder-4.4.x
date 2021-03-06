Name:           perl-List-UtilsBy
Version:        0.09
Release:        3%{?dist}
Summary:        Higher-order list utility functions
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/List-UtilsBy/
Source0:        http://www.cpan.org/authors/id/P/PE/PEVANS/List-UtilsBy-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)

# for improved testing
BuildRequires:  perl(Test::Pod) >= 1.00

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides a number of list utility functions, all of which take
an initial code block to control their behaviour. They are variations on
similar core perl or List::Util functions of similar names, but which use
the block to control their behaviour. For example, the core Perl function
sort takes a list of values and returns them, sorted into order by their
string value. The sort_by function sorts them according to the string value
returned by the extra function, when given each value.

%prep
%setup -q -n List-UtilsBy-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.09-2
- Perl 5.16 rebuild

* Sun Mar 04 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.09-1
- Upstream update.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.08-1
- Upstream update.

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.07-2
- Perl mass rebuild

* Thu Apr 28 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.07-1
- Upstream update.
- Spec cleanup.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.06-1
- Initial Fedora package.
