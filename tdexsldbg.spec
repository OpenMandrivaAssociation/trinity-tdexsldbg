%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg tdexsldbg
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity



Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	%{tde_version}
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Graphical XSLT debugger for TDE
Group:		Applications/Multimedia
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/development/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DLIB_INSTALL_DIR=%{tde_prefix}/%{_lib}
BuildOption:    -DBUILD_ALL=ON -DWITH_ALL_OPTIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

Obsoletes:		trinity-kxsldbg < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kxsldbg = %{?epoch:%{epoch}:}%{version}-%{release}

%description
KXSLDbg is a debugger for XSLT scripts. It includes a graphical user
interface as well as a text-based debugger. KXSLDbg can be run as a
standalone application or as an embedded TDE part.

XSLT is an XML language for defining transformations of XML files from
XML to some other arbitrary format, such as XML, HTML, plain text, etc.,
using standard XSLT stylesheets.

This package is part of TDE, as a component of the TDE web development module.
See the 'tde-trinity' and 'tdewebdev-trinity' packages for more information.


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
%lang(da) %{tde_tdedocdir}/HTML/da/kxsldbg/
%lang(da) %{tde_tdedocdir}/HTML/da/xsldbg/
%lang(de) %{tde_tdedocdir}/HTML/de/kxsldbg/
%lang(en) %{tde_tdedocdir}/HTML/en/kxsldbg/
%lang(en) %{tde_tdedocdir}/HTML/en/xsldbg/
%lang(es) %{tde_tdedocdir}/HTML/es/kxsldbg/
%lang(es) %{tde_tdedocdir}/HTML/es/xsldbg/
%lang(et) %{tde_tdedocdir}/HTML/et/kxsldbg/
%lang(et) %{tde_tdedocdir}/HTML/et/xsldbg/
%lang(fr) %{tde_tdedocdir}/HTML/fr/kxsldbg/
%lang(it) %{tde_tdedocdir}/HTML/it/kxsldbg/
%lang(it) %{tde_tdedocdir}/HTML/it/xsldbg/
%lang(nl) %{tde_tdedocdir}/HTML/nl/kxsldbg/
%lang(nl) %{tde_tdedocdir}/HTML/nl/xsldbg/
%lang(pt) %{tde_tdedocdir}/HTML/pt/kxsldbg/
%lang(pt) %{tde_tdedocdir}/HTML/pt/xsldbg/
%lang(pt_BR) %{tde_tdedocdir}/HTML/pt_BR/kxsldbg/
%lang(pt_BR) %{tde_tdedocdir}/HTML/pt_BR/xsldbg/
%lang(ru) %{tde_tdedocdir}/HTML/ru/kxsldbg/
%lang(ru) %{tde_tdedocdir}/HTML/ru/xsldbg/
%lang(sv) %{tde_tdedocdir}/HTML/sv/kxsldbg/
%lang(sv) %{tde_tdedocdir}/HTML/sv/xsldbg/
%{tde_prefix}/share/icons/hicolor/*/actions/*.png
%{tde_prefix}/share/icons/hicolor/*/apps/*.png
%{tde_prefix}/share/icons/locolor/*/apps/*.png
%{tde_prefix}/share/man/man1/kxsldbg.1*
%{tde_prefix}/share/services/kxsldbg_part.desktop

