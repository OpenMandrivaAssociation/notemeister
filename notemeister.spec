Name: 	 	notemeister
Summary: 	GNOME ideas and notes organizer
Version:	0.1.7
Release: 	10

Source:		%{name}-%{version}.tar.bz2
Source1:	%{name}48.png
Source2:	%{name}32.png
Source3:	%{name}16.png
Patch0:		notemeister-fix-desktop-entry.patch
Patch1:		notemeister-0.1.7-no-pyxml.patch
URL:		http://notemeister.sourceforge.net/
License:	GPLv2+
Group:		Office
BuildRequires:	pkgconfig(python2)
BuildRequires:  imagemagick
BuildRequires:  desktop-file-utils
Requires:	gnome-python
BuildArch:	noarch

%description
 Notemeister is a small, simple note organizer made for the GNOME2 desktop.
It's features include:
    * Notes stored in a tree view and structure
    * Drag and drop support for reordering notes
    * Simple text formatting by highlighted bounds
    * Auto-save feature 

%files
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
%patch1 -p1

%build
python2 setup.py build
										
%install
python2 setup.py install --root=%{buildroot}
rm -fr %{buildroot}/%_prefix/doc

#menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Utility" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-Office-Accessories" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#icons
mkdir -p %{buildroot}/%_liconsdir
cp %SOURCE1 %{buildroot}/%_liconsdir/%name.png
mkdir -p %{buildroot}/%_iconsdir
cp %SOURCE2 %{buildroot}/%_iconsdir/%name.png
mkdir -p %{buildroot}/%_miconsdir
cp %SOURCE3 %{buildroot}/%_miconsdir/%name.png
