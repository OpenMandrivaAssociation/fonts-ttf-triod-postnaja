%define pkgname TriodPostnaja

Summary: Decorative font in Slavonic Church style
Name: fonts-ttf-triod-postnaja
Version: 20100305
Release: 3
License: OFL
Group: System/Fonts/True type
URL: https://io.debian.net/~danielj/
Source0: http://io.debian.net/~danielj/triod-postnaja/%{pkgname}-%{version}.sfd.gz
BuildArch: noarch
BuildRequires: freetype-tools
BuildRequires: fontforge


%description
Triod Postnaja attempts to mimic the typefaces used to publish Old Church
Slavonic service books prior to the 20th century. It also provides a range of
Latin letters in the same style, sufficient for the needs of central, northern
and western European languages.

%prep
#%setup -q -c -n %{pkgname}-%{version}
cd %_builddir
%__mkdir_p %{pkgname}-%{version}
cd %{pkgname}-%{version}
%__gzip -dc %{SOURCE0} > %{pkgname}-%{version}.sfd

%build
cd %{_builddir}/%{pkgname}-%{version}
for sfdfile in *.sfd
do
  fontforge -lang=ff -c "Open(\"./$sfdfile\"); Generate(\"./$sfdfile\":r + \".ttf\")"
done

%install
cd %{pkgname}-%{version}

%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/triod-postnaja

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/triod-postnaja
ttmkfdir %{buildroot}%{_xfontdir}/TTF/triod-postnaja > %{buildroot}%{_xfontdir}/TTF/triod-postnaja/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/triod-postnaja/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/triod-postnaja \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-triod-postnaja:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{_xfontdir}/TTF/triod-postnaja
%{_xfontdir}/TTF/triod-postnaja/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/triod-postnaja/fonts.dir
%{_xfontdir}/TTF/triod-postnaja/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-triod-postnaja:pri=50





%changelog
* Sat Jul 23 2011 Sergey Zhemoitel <serg@mandriva.org> 20100305-1mdv2012.0
+ Revision: 691280
- imported package fonts-ttf-triod-postnaja

