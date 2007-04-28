%define name ttfonts
%define version 1.3
%define release %mkrel 16

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Freeware
Summary:	Free TrueType fonts
Group:		System/Fonts/True type 

Source:		ttfonts-%{version}.tar.bz2
Source1:	fonts-ttf-west_european-fonts.dir.bz2
Source2:	fonts-ttf-decoratives-fonts.dir.bz2

BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-root

%description
This package is a collection of free True Type Fonts.

%package -n fonts-ttf-west_european
Summary:	Free True Type Fonts (west eruopean charset)
Group:		System/Fonts/True type
Obsoletes:	ttfonts
Requires(post):		chkfontpath
Requires(postun):	chkfontpath
Requires(post): fontconfig
Requires(postun): fontconfig

%description -n fonts-ttf-west_european
This package is a collection of free TrueType fonts.

%package -n fonts-ttf-decoratives
Summary:	Free True Type Fonts (decoratives)
Group:		System/Fonts/True type
Requires(post):		chkfontpath
Requires(postun):	chkfontpath
Requires(post): fontconfig
Requires(postun): fontconfig

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

%files -n fonts-ttf-decoratives
%defattr (-,root,root)
%doc decoratives/*
%dir %_datadir/fonts/ttf/decoratives
%_datadir/fonts/ttf/decoratives/*.ttf
%config(noreplace) %_datadir/fonts/ttf/decoratives/fonts.dir
%config(noreplace) %_datadir/fonts/ttf/decoratives/fonts.scale

%post -n fonts-ttf-west_european
[ -x %_sbindir/chkfontpath ] && %_sbindir/chkfontpath -q -a %_datadir/fonts/ttf/western
[ -x %_bindir/fc-cache ] && %_bindir/fc-cache 

%postun -n fonts-ttf-west_european
if [ "$1" = "0" ];then
  [ -x %_sbindir/chkfontpath ] && %_sbindir/chkfontpath -q -r %_datadir/fonts/ttf/western
  [ -x %_bindir/fc-cache ] && %_bindir/fc-cache 
fi

%post -n fonts-ttf-decoratives
[ -x %_sbindir/chkfontpath ] && %_sbindir/chkfontpath -q -a %_datadir/fonts/ttf/decoratives
[ -x %_bindir/fc-cache ] && %_bindir/fc-cache 

%postun -n fonts-ttf-decoratives
if [ "$1" = "0" ];then
  [ -x %_sbindir/chkfontpath ] && %_sbindir/chkfontpath -q -r %_datadir/fonts/ttf/decoratives
  [ -x %_bindir/fc-cache ] && %_bindir/fc-cache 
fi

