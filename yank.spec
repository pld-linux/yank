Summary:	yet another note-keeper (GNOME)
Name:		yank
Version:	0.1.3
Release:	1
License:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Source0:	ftp://yank.sourceforge.net/pub/yank/%{name}-%{version}.tar.bz2
URL:		http://yank.sourceforge.net/
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Yank is a simple notekeer and todo-list manager using the gnome and gtk
libraries. It feels stable and usable enough to be released to the public
but it surely lacks some (not so important) features which might be added
later. Excessive tests have shown that yank is fool-proof, irritating and
wasting too much memory.

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Applications

gzip -9nf AUTHORS ChangeLog NEWS README THANKS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/yank
%{_datadir}/pixmaps/yank.png
%{_applnkdir}/Applications/yank.desktop
