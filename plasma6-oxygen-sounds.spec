%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define git 20230707

Name: plasma6-oxygen-sounds
Version: 5.240.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/oxygen-sounds/-/archive/master/oxygen-sounds-master.tar.bz2#/oxygen-sounds-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/plasma/%(echo %{version}|cut -d. -f1-3)/oxygen-sounds-%{version}.tar.xz
%endif
Summary: Sounds for the Oxygen Plasma theme
URL: https://invent.kde.org/plasma/oxygen-sounds/
License: LGPL-3.0-or-later
Group: Graphical desktop/KDE
BuildArch: noarch
BuildRequires: cmake ninja extra-cmake-modules
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)

%description
Sounds for the Oxygen Plasma theme

%prep
%autosetup -p1 -n oxygen-sounds-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/sounds/Oxygen-*.ogg
%{_datadir}/sounds/oxygen
