Summary:	Yet another note-keeper (GNOME)
Summary(pl):	Jeszcze jeden notatnik
Name:		yank
Version:	0.2.1
Release:	6
License:	GPL
Group:		X11/Applications
Source0:	http://download.sourceforge.net/yank/%{name}-%{version}.tar.bz2
Source1:	%{name}.png
Patch0:		%{name}-gconf_install.patch
Patch1:		%{name}-gtkspell_menu.patch
Patch2:		%{name}-build_spell_pligin_conditionaly.patch
Patch3:		%{name}-desktop.patch
URL:		http://yank.sourceforge.net/
BuildRequires:	GConf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gal-devel >= 0.19
BuildRequires:	gdk-pixbuf-gnome-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.28
BuildRequires:	gtk+-devel
BuildRequires:	libglade-gnome-devel
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
Yank is a simple notekeer and todo-list manager using the gnome and
gtk libraries. It feels stable and usable enough to be released to the
public but it surely lacks some (not so important) features which
might be added later. Excessive tests have shown that yank is
fool-proof, irritating and wasting too much memory.

%description -l pl
Yank jest prostym notatnikiem i programem do zarz±dzania osobist±
list± zadañ, korzystaj±cym z bibliotek GNOME i gtk+.

%package gpg
Summary:	GPG plugin
Summary(pl):	Wtyczka GPG
Group:		X11/Applications
Requires:	%{name} = %{version}

%description gpg
GPG plugin.

%description gpg -l pl
Wtyczka GPG.

%package pgp5
Summary:	PGP5 plugin
Summary(pl):	Wtyczka PGP5
Group:		X11/Applications
Requires:	%{name} = %{version}

%description pgp5
PGP5 plugin.

%description pgp5 -l pl
Wtyczka PGP5.

%package gtkspell
Summary:	Spellchecker plugin
Summary(pl):	Wtyczka sprawdzaj±ca pisowniê
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
%patch3 -p1

install %{SOURCE1} pixmaps

%build
rm -f aux/missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/yank
%dir %{_libdir}/yank/plugins/%{version}
%dir %{_libdir}/yank/plugins
%dir %{_libdir}/yank
%{_sysconfdir}/gconf/gconf.xml.defaults/apps/yank
%{_sysconfdir}/gconf/gconf.xml.defaults/schemas/apps/yank
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
