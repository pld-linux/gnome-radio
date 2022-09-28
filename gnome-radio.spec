Summary:	Public radio mapping application for GNOME
Summary(pl.UTF-8):	Aplikacja z mapą publicznych stacji radiowych dla GNOME
Name:		gnome-radio
Version:	47.0
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-radio/47/%{name}-%{version}.tar.xz
# Source0-md5:	b269f4948c927191bf0a2939d3963e24
URL:		https://wiki.gnome.org/Apps/Radio
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	geoclue2-devel >= 2.4.12
BuildRequires:	geocode-glib-devel >= 3.20
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-bad-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.24.34
BuildRequires:	gtk-doc >= 1.16
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libchamplain-devel >= 0.12.10
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pango-devel >= 1:0.28
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	geoclue2 >= 2.4.12
Requires:	geocode-glib >= 3.20
Requires:	glib2 >= 1:2.38.0
Requires:	gstreamer-plugins-bad >= 1.0
Requires:	gstreamer-plugins-base >= 1.0
Requires:	gstreamer-plugins-good >= 1.0
Requires:	gtk+3 >= 3.24.34
Requires:	hicolor-icon-theme
Requires:	libchamplain >= 0.12.10
Requires:	pango >= 1:0.28
Obsoletes:	girl < 10.1
Obsoletes:	gnome-internet-radio-locator < 13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Radio is the Public Network Radio Software for Accessing Free
Audio Broadcasts from the Internet.

%description -l pl.UTF-8
GNOME Radio to program do publicznych sieci radiowych, pozwalający na
dostęp do darmowych rozgłośni dźwiękowych z Internetu.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-internet-radio-locator
%attr(755,root,root) %{_bindir}/gnome-radio
%attr(755,root,root) %{_bindir}/org.gnome.Radio
%{_datadir}/gnome-radio
%{_datadir}/metainfo/gnome-radio.appdata.xml
%{_desktopdir}/gnome-radio.desktop
%{_iconsdir}/hicolor/scalable/apps/gnome-radio.svg
%{_mandir}/man1/gnome-radio.1*
