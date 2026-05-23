%bcond clang 1

# TDE variables
%define tde_pkg tdexsldbg
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity

Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	Graphical XSLT debugger for TDE
Group:		Applications/Multimedia
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/development/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DBUILD_ALL=ON -DWITH_ALL_OPTIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:	libtool

Obsoletes:		trinity-kxsldbg < %{EVRD}
Provides:		trinity-kxsldbg = %{EVRD}

%description
KXSLDbg is a debugger for XSLT scripts. It includes a graphical user
interface as well as a text-based debugger. KXSLDbg can be run as a
standalone application or as an embedded TDE part.

XSLT is an XML language for defining transformations of XML files from
XML to some other arbitrary format, such as XML, HTML, plain text, etc.,
using standard XSLT stylesheets.

This package is part of TDE, as a component of the TDE web development module.
See the 'tde-trinity' and 'tdewebdev-trinity' packages for more information.

%patchlist
trinity-tdexsldbg-fix-cflags.patch


%install -a
%find_lang kxsldbg

%files -f kxsldbg.lang
%defattr(-,root,root,-)
%{tde_prefix}/bin/kxsldbg
%{tde_prefix}/bin/xsldbg
%{tde_prefix}/%{_lib}/trinity/libkxsldbgpart.la
%{tde_prefix}/%{_lib}/trinity/libkxsldbgpart.so
%{tde_prefix}/share/applications/tde/kxsldbg.desktop
%{tde_prefix}/share/applnk/.hidden/xsldbg.desktop
%{tde_prefix}/share/apps/kxsldbg/kxsldbg_shell.rc
%{tde_prefix}/share/apps/kxsldbgpart/kxsldbg_part.rc
%lang(da) %{tde_prefix}/share/doc/tde/HTML/da/kxsldbg/
%lang(da) %{tde_prefix}/share/doc/tde/HTML/da/xsldbg/
%lang(de) %{tde_prefix}/share/doc/tde/HTML/de/kxsldbg/
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/kxsldbg/
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/xsldbg/
%lang(es) %{tde_prefix}/share/doc/tde/HTML/es/kxsldbg/
%lang(es) %{tde_prefix}/share/doc/tde/HTML/es/xsldbg/
%lang(et) %{tde_prefix}/share/doc/tde/HTML/et/kxsldbg/
%lang(et) %{tde_prefix}/share/doc/tde/HTML/et/xsldbg/
%lang(fr) %{tde_prefix}/share/doc/tde/HTML/fr/kxsldbg/
%lang(it) %{tde_prefix}/share/doc/tde/HTML/it/kxsldbg/
%lang(it) %{tde_prefix}/share/doc/tde/HTML/it/xsldbg/
%lang(nl) %{tde_prefix}/share/doc/tde/HTML/nl/kxsldbg/
%lang(nl) %{tde_prefix}/share/doc/tde/HTML/nl/xsldbg/
%lang(pt) %{tde_prefix}/share/doc/tde/HTML/pt/kxsldbg/
%lang(pt) %{tde_prefix}/share/doc/tde/HTML/pt/xsldbg/
%lang(pt_BR) %{tde_prefix}/share/doc/tde/HTML/pt_BR/kxsldbg/
%lang(pt_BR) %{tde_prefix}/share/doc/tde/HTML/pt_BR/xsldbg/
%lang(ru) %{tde_prefix}/share/doc/tde/HTML/ru/kxsldbg/
%lang(ru) %{tde_prefix}/share/doc/tde/HTML/ru/xsldbg/
%lang(sv) %{tde_prefix}/share/doc/tde/HTML/sv/kxsldbg/
%lang(sv) %{tde_prefix}/share/doc/tde/HTML/sv/xsldbg/
%{tde_prefix}/share/icons/hicolor/*/actions/*.png
%{tde_prefix}/share/icons/hicolor/*/apps/*.png
%{tde_prefix}/share/icons/locolor/*/apps/*.png
%{tde_prefix}/share/man/man1/kxsldbg.1*
%{tde_prefix}/share/services/kxsldbg_part.desktop

