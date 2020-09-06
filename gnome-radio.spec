Summary:	Public radio mapping application for GNOME
Summary(pl.UTF-8):	Aplikacja z mapą publicznych stacji radiowych dla GNOME
Name:		gnome-radio
Version:	0.2.0
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-radio/0.2/%{name}-%{version}.tar.xz
# Source0-md5:	cc28d76e76c088661a045e7dbe2f2673
URL:		https://wiki.gnome.org/Apps/Radio
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-bad-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.22.30
BuildRequires:	libchamplain-devel >= 0.12.10
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gstreamer-plugins-bad >= 1.0
Requires:	gstreamer-plugins-base >= 1.0
Requires:	gstreamer-plugins-good >= 1.0
Requires:	gtk+3 >= 3.22.30
Requires:	hicolor-icon-theme
Requires:	libchamplain >= 0.12.10
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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-radio
