Summary: yet another note-keeper (GNOME)
Name: yank
%define version		@VERSION@
%define rel		1
%define prefix		/usr
Version: %{version}
Release: %{rel}
Copyright: GPL
Packager: Thomas Schultz <tststs@gmx.de>
URL: http://home.ins.de/%7Em.hussmann/software/yank/index.html
Group: X11/Utilities
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-root

%description
Yank is a simple notekeer and todo-list manager using the gnome and gtk
libraries. It feels stable and usable enough to be released to the public
but it surely lacks some (not so important) features which might be added
later. Excessive tests have shown that yank is fool-proof, irritating and
wasting too much memory. ;)

%changelog
* Tue Mar 28 2000 Thomas Schultz <tststs@gmx.de>
- First release of .spec file

%prep
%setup

%build
./configure --prefix=%prefix
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
strip src/yank

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%{prefix}/bin/yank
%{prefix}/share/pixmaps/yank.png
%{prefix}/share/locale/*/*/*
%{prefix}/share/gnome/apps/Applications/yank.desktop
