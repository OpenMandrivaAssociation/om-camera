Name:		om-camera
Summary:	PinePhone Camera viewer
Version:	0.0.4
Release:	3
License:	GPLv3
Source0:	https://github.com/OpenMandrivaSoftware/om-camera/archive/%{version}/%{name}-%{version}.tar.gz
Requires:	mpv pinephone-tools v4l-utils
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qmake5
BuildRequires:	mpv
Requires:	mpv
Requires:	ffmpeg
# for arecord
Requires:	alsa-utils

%description
PinePhone camera

%prep
%autosetup -p1
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/camera
%{_datadir}/applications/ch.lindev.camera.desktop
%{_datadir}/icons/hicolor/scalable/apps/ch.lindev.camera.svg
