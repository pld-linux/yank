Summary:	Yet another note-keeper (GNOME)
Summary(pl):	Jeszcze jeden notatnik
Name:		yank
Version:	0.2.1
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://download.sourceforge.net/yank/%{name}-%{version}.tar.bz2
Patch0:		%{name}-gconf_install.patch
Patch1:		%{name}-gtkspell_menu.patch
Patch2:		%{name}-build_spell_pligin_conditionaly.patch
URL:		http://yank.sourceforge.net/
BuildRequires:	GConf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	gal-devel >= 0.19
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.28
BuildRequires:	gtk+-devel
BuildRequires:	libglade-devel
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME

%description
Yank is a simple notekeer and todo-list manager using the gnome and
gtk libraries. It feels stable and usable enough to be released to the
public but it surely lacks some (not so important) features which
might be added later. Excessive tests have shown that yank is
fool-proof, irritating and wasting too much memory.

%description -l pl
Yank jest prostym notatnikiem i menad¿erem listy rzeczy do zrobienia,
u¿ywaj±cym bibliotek GNOME i gtk+.

%package gpg
Summary:	GPG plugin
Summary(pl):	Wtyczka GPG.
Group:		X11/Applications
Requires:	%{name} = %{version}

%description gpg
GPG plugin.

%description gpg -l pl
Wtyczka GPG.

%package pgp5
Summary:	PGP5 plugin
Summary(pl):	Wtyczka PGP5.
Group:		X11/Applications
Requires:	%{name} = %{version}

%description pgp5
PGP5 plugin.

%description pgp5 -l pl
Wtyczka PGP5.

%package gtkspell
Summary:	Spellchecker plugin
Summary(pl):	Wtyczka sprawdzaj±ca pisowniê.
Group:		X11/Applications
Requires:	%{name} = %{version}

%description gtkspell
Spellchecker plugin.

%description gtkspell -l pl
Wtyczka sprawdzaj±ca pisowniê.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f aux/missing
libtoolize --copy --force
gettextize --copy --force
aclocal
autoconf
automake -a -c

CFLAGS="%{rpmcflags}"
%configure \
	--enable-spell-plugin \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/gconf

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Office/PIMs

gzip -9nf AUTHORS ChangeLog NEWS README THANKS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/yank
%dir %{_libdir}/yank/plugins/%{version}
%dir %{_libdir}/yank/plugins
%dir %{_libdir}/yank
%{_sysconfdir}/*/*/*
%{_pixmapsdir}/yank.png
%{_applnkdir}/Office/PIMs/yank.desktop

%files gpg
%defattr(644,root,root,755)
%{_libdir}/%{name}/plugins/%{version}/libGpg*

%files pgp5
%defattr(644,root,root,755)
%{_libdir}/%{name}/plugins/%{version}/libPgp5*

%files gtkspell
%defattr(644,root,root,755)
%{_libdir}/%{name}/plugins/%{version}/libGtkSpell*
