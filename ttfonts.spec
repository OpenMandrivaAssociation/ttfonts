Name:		ttfonts
Version:	1.4
Release:	8
License:	Freeware
Summary:	TrueType fonts
Group:		System/Fonts/True type 
Source0:	ttfonts-%{version}.tar.xz
Source1:	fonts-ttf-west_european-fonts.dir.bz2
Source2:	fonts-ttf-decoratives-fonts.dir.bz2
BuildArch:	noarch

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
# iso8858-{1,15} and ascii-0 fonts
mkdir -p %{buildroot}%_datadir/fonts/ttf/western
# decorative fonts, quite improper for normal use
mkdir -p %{buildroot}%_datadir/fonts/ttf/decoratives

mkdir western
for i in Adventure Bluehigb Bluehigc Bluehigh a_d_mono babelfish \
	dirtydoz fudd larabief 
do
  install -m444 $i.ttf %{buildroot}%_datadir/fonts/ttf/western
  cp $i.txt western || :
done 
bzcat %{SOURCE1} > %{buildroot}%_datadir/fonts/ttf/western/fonts.dir
bzcat %{SOURCE1} > %{buildroot}%_datadir/fonts/ttf/western/fonts.scale

mkdir decoratives
for i in CaptainPodd actionis bazaroni betadance betsy binary \
	brandnew creature davis demon densmore dienasty \
	distortia edgewater electroh eli5.0- embargo2 fadgod failed \
	fakerece flubber fontrstc goldengi hydrogen ikarrg ikart \
	ikarv independ indigo
do
  install -m444 $i.ttf %{buildroot}%_datadir/fonts/ttf/decoratives
  cp $i.txt decoratives || :
done
bzcat %{SOURCE2} > %{buildroot}%_datadir/fonts/ttf/decoratives/fonts.dir
bzcat %{SOURCE2} > %{buildroot}%_datadir/fonts/ttf/decoratives/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/ttf/western \
	%{buildroot}%_sysconfdir/X11/fontpath.d/ttf-west_european:pri=50
ln -s ../../..%_datadir/fonts/ttf/decoratives \
	%{buildroot}%_sysconfdir/X11/fontpath.d/ttf-decoratives:pri=50

cp bluehigh.txt contourgenerator.txt western/
cp betsy.readme.txt decoratives/

%files -n fonts-ttf-west_european
%doc western/*
%dir %_datadir/fonts/ttf/western
%_datadir/fonts/ttf/western/*.ttf
%config(noreplace) %_datadir/fonts/ttf/western/fonts.scale
%config(noreplace) %_datadir/fonts/ttf/western/fonts.dir
%_sysconfdir/X11/fontpath.d/ttf-west_european:pri=50

%files -n fonts-ttf-decoratives
%doc decoratives/*
%dir %_datadir/fonts/ttf/decoratives
%_datadir/fonts/ttf/decoratives/*.ttf
%config(noreplace) %_datadir/fonts/ttf/decoratives/fonts.dir
%config(noreplace) %_datadir/fonts/ttf/decoratives/fonts.scale
%_sysconfdir/X11/fontpath.d/ttf-decoratives:pri=50
