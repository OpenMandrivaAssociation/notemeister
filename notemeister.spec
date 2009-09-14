%define name	notemeister
%define version 0.1.7
%define release %mkrel 6

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
License:	GPL
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


