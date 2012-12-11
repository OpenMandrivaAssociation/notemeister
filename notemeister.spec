%define name	notemeister
%define version 0.1.7
%define release %mkrel 8

Name: 	 	%{name}
Summary: 	GNOME ideas and notes organizer
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Source1:	%{name}48.png
Source2:	%{name}32.png
Source3:	%{name}16.png
Patch0:		notemeister-fix-desktop-entry.patch
URL:		http://notemeister.sourceforge.net/
License:	GPLv2+
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel 
BuildRequires:  imagemagick
BuildRequires:  desktop-file-utils
Requires:	gnome-python
Requires:       python-pyxml
BuildArch:	noarch

%description
 Notemeister is a small, simple note organizer made for the GNOME2 desktop.
It's features include:
    * Notes stored in a tree view and structure
    * Drag and drop support for reordering notes
    * Simple text formatting by highlighted bounds
    * Auto-save feature 

%files
%defattr(-,root,root)
%doc AUTHORS PKG-INFO README
%{_bindir}/%name
%{py_puresitedir}/%{name}
%{py_puresitedir}/*.egg-info
%{_datadir}/%name
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

#--------------------------------------------------------------------


%prep
%setup -q
%patch0 -p0

%build
python setup.py build
										
%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT
rm -fr $RPM_BUILD_ROOT/%_prefix/doc

#menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Utility" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-Office-Accessories" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cp %SOURCE1 $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cp %SOURCE2 $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cp %SOURCE3 $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT




%changelog
* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 0.1.7-8mdv2011.0
+ Revision: 590158
- rebuild for python 2.7

* Sun Jan 31 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.1.7-7mdv2010.1
+ Revision: 498884
- Fix licence
- New maintainer

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.1.7-6mdv2010.0
+ Revision: 440344
- rebuild

* Thu Dec 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.7-5mdv2009.1
+ Revision: 313228
- lowercase ImageMagick

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.1.7-5mdv2009.0
+ Revision: 222749
- patch 0: fix 'error: value "0.4.11" for key "Version" in group "Desktop
  Entry" is not a known version'
- patch 0: fix 'key "Icon" in group "Desktop Entry" is an icon name with an
  extension' error
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Thu Jan 04 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0.1.7-4mdv2007.0
+ Revision: 104113
- Rebuild against new python
- Add menu entry
- Import notemeister

* Sun Mar 05 2006 Michael Scherer <misc@mandriva.org>
- add pyxml requires, fix 19951
- use mkrel
- use new python macro

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.1.7-2mdk
- Rebuild for new python

* Fri Jul 09 2004 Austin Acton <austin@mandrake.org> 0.1.7-1mdk
- 0.1.7

* Fri Jun 11 2004 Austin Acton <austin@mandrake.org> 0.1-1mdk
- initial package

