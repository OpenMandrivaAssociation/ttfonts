%define name ttfonts
%define version 1.3
%define release 36

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Freeware
Summary:	TrueType fonts
Group:		System/Fonts/True type 

Source:		ttfonts-%{version}.tar.bz2
Source1:	fonts-ttf-west_european-fonts.dir.bz2
Source2:	fonts-ttf-decoratives-fonts.dir.bz2

BuildArch:	noarch
BuildRequires: fontconfig
BuildRoot:	%_tmppath/%name-%version-%release-root

%description
This package is a collection of free TrueType fonts.

%package -n fonts-ttf-west_european
Summary:	TrueType fonts (West European charset)
Group:		System/Fonts/True type
Obsoletes:	ttfonts

%description -n fonts-ttf-west_european
This package is a collection of free TrueType fonts.

%package -n fonts-ttf-decoratives
Summary:	True Type Fonts (decoratives)
Group:		System/Fonts/True type

%description -n fonts-ttf-decoratives
This package is a collection of free TrueType fonts.

%prep
%setup -q -n ttfonts 

%build

%install
rm -rf $RPM_BUILD_ROOT
# iso8858-{1,15} and ascii-0 fonts
mkdir -p $RPM_BUILD_ROOT%_datadir/fonts/ttf/western
# decorative fonts, quite improper for normal use
mkdir -p $RPM_BUILD_ROOT%_datadir/fonts/ttf/decoratives

mkdir western
for i in Adventure Bluehigb Bluehigc Bluehigh a_d_mono babelfish \
	dirtydoz fudd larabief 
do
  install -m444 $i.ttf $RPM_BUILD_ROOT%_datadir/fonts/ttf/western
  cp $i.txt western || :
done 
bzcat %{SOURCE1} > $RPM_BUILD_ROOT%_datadir/fonts/ttf/western/fonts.dir
bzcat %{SOURCE1} > $RPM_BUILD_ROOT%_datadir/fonts/ttf/western/fonts.scale

mkdir decoratives
for i in CaptainPodd actionis bazaroni betadance betsy binary \
	brandnew creature davis demon densmore dienasty \
	distortia edgewater electroh eli5.0- embargo2 fadgod failed \
	fakerece flubber fontrstc goldengi hydrogen ikarrg ikart \
	ikarv independ indigo
do
  install -m444 $i.ttf $RPM_BUILD_ROOT%_datadir/fonts/ttf/decoratives
  cp $i.txt decoratives || :
done
bzcat %{SOURCE2} > $RPM_BUILD_ROOT%_datadir/fonts/ttf/decoratives/fonts.dir
bzcat %{SOURCE2} > $RPM_BUILD_ROOT%_datadir/fonts/ttf/decoratives/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/ttf/western \
	%{buildroot}%_sysconfdir/X11/fontpath.d/ttf-west_european:pri=50
ln -s ../../..%_datadir/fonts/ttf/decoratives \
	%{buildroot}%_sysconfdir/X11/fontpath.d/ttf-decoratives:pri=50

cp bluehigh.txt contourgenerator.txt western/
cp betsy.readme.txt decoratives/

%clean
rm -rf $RPM_BUILD_ROOT

%files -n fonts-ttf-west_european
%defattr (-,root,root)
%doc western/*
%dir %_datadir/fonts/ttf/western
%_datadir/fonts/ttf/western/*.ttf
%config(noreplace) %_datadir/fonts/ttf/western/fonts.scale
%config(noreplace) %_datadir/fonts/ttf/western/fonts.dir
%_sysconfdir/X11/fontpath.d/ttf-west_european:pri=50

%files -n fonts-ttf-decoratives
%defattr (-,root,root)
%doc decoratives/*
%dir %_datadir/fonts/ttf/decoratives
%_datadir/fonts/ttf/decoratives/*.ttf
%config(noreplace) %_datadir/fonts/ttf/decoratives/fonts.dir
%config(noreplace) %_datadir/fonts/ttf/decoratives/fonts.scale
%_sysconfdir/X11/fontpath.d/ttf-decoratives:pri=50



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.3-25mdv2011.0
+ Revision: 675431
- br fontconfig for fc-query used in new rpm-setup-build

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3-24
+ Revision: 670730
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-23mdv2011.0
+ Revision: 608043
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.3-22mdv2010.1
+ Revision: 494168
- fc-cache is now called by an rpm filetrigger

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.3-21mdv2010.0
+ Revision: 427435
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.3-20mdv2009.0
+ Revision: 225887
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.3-19mdv2008.1
+ Revision: 171149
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.3-18mdv2008.0
+ Revision: 48756
- normalize fontpath.d symlink name (based on pkg name)

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.3-17mdv2008.0
+ Revision: 48695
- fontpath.d conversion (#31756)

* Sat Apr 28 2007 Adam Williamson <awilliamson@mandriva.org> 1.3-16mdv2008.0
+ Revision: 18887
- more cleaning
- clean spec, rebuild for new era


* Wed Feb 08 2006 Frederic Crozat <fcrozat@mandriva.com> 1.3-15mdk
- Don't package fontconfig cache file
- Fix prereq

* Wed Sep 15 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 1.3-14mdk
- fixed fonts.dir files by removing missing fonts (bug #9428)

* Wed Nov 19 2003 Jean-Michel Dault <jmdault@mandrakesoft.com> 1.3-13mdk
- nuke beast wars font, it breaks xfs in a weird way

* Fri Jul 25 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.3-12mdk
- rebuild
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install
- fix no-prereq-on chkfontpath (rpmlint)
- fix conffile-without-noreplace-flag (rpmlint)

* Thu Feb 20 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 1.3-11mdk
- corrected Licence: line

* Tue Feb 18 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 1.3-10mdk
- proper use of fc-cache

