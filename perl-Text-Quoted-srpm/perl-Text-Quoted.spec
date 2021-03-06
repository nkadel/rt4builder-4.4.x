Name: 		perl-Text-Quoted
Version: 	2.09
#Release: 	3%{?dist}
Release: 	0.3%{?dist}
Summary: 	Extract the structure of a quoted mail message
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Text-Quoted/
Source0:        http://www.cpan.org/authors/id/A/AL/ALEXMV/Text-Quoted-%{version}.tar.gz

BuildArch: 	noarch

Requires:  	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires: perl(Test::More)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Text::Autoformat)

%description
Text::Quoted examines the structure of some text which may contain multiple
different levels of quoting, and turns the text into a nested data structure.

%prep
%setup -q -n Text-Quoted-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/Text
%{_mandir}/man3/*

%changelog
* Sat Mar 19 2016 Nico Kadel-Garcia <nkadel@gmail.com> - 2.09-0.3
- Backport to RHEL 7

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-2
- Perl 5.22 rebuild

* Mon Mar 09 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.09-1
- Upstream update.
- Reflect Source0: having changed.

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.08-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 2.08-2
- Perl 5.18 rebuild

* Wed May 22 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.08-1
- Upstream update.

* Tue May 21 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.07-1
- Upstream update.
- Reflect Source0-URL having changed.
- Modernize spec.
- Fix up bogus changelog entries.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 2.06-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.06-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.06-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.06-1
- Upstream update.
- Update Source0:-URL.
- Minor spec cleanup.

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.05-6
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 2.05-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.05-2
- Rebuild for new perl

* Fri Jan 25 2008 Ralf Corsépius <rc040203@freenet.de> - 2.05-1
- Upstream update.

* Tue Nov 13 2007 Ralf Corsépius <rc040203@freenet.de> - 2.03-1
- Upstream update.

* Fri Aug 31 2007 Ralf Corsépius <rc040203@freenet.de> - 2.02-3
- BR: perl(Test::More).
- Update license tag.

* Mon Mar 12 2007 Ralf Corsépius <rc040203@freenet.de> - 2.02-2
- BR: perl(ExtUtils::MakeMaker).

* Fri Mar 02 2007 Ralf Corsépius <rc040203@freenet.de> - 2.02-1
- Upstream update.

* Fri Feb 16 2007 Ralf Corsépius <rc040203@freenet.de> - 1.10-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.8-5
- Mass rebuild.

* Tue Feb 28 2006 Ralf Corsépius <rc040203@freenet.de> - 1.8-4
- Rebuild for perl-5.8.8.

* Fri Aug 19 2005 Ralf Corsepius <ralf@links2linux.de> - 1.8-3
- chmod -x Quote.pm.

* Fri Aug 19 2005 Ralf Corsepius <ralf@links2linux.de> - 1.8-2
- Spec cleanup.

* Thu Aug 11 2005 Ralf Corsepius <ralf@links2linux.de> - 1.8-1
- FE submission.
