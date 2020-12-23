Name:		om-camera
Summary:	PinePhone Camera viewer
Version:	0.0.1
Release:	1
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

%description
PinePhone camera

%prep
%autosetup -p1
%cmake \
	-G Ninja

%build
%ninja_build -C build
cp build/src/camera cameraf
sed -i -e 's,front,rear,g' src/CameraWidget.cpp
%ninja_build -C build

%install
%ninja_install -C build
cp -a cameraf %{buildroot}%{_bindir}
sed -e 's,Camera$,Camera (Front),g;s,/camera,/cameraf,g' %{buildroot}%{_datadir}/applications/ch.lindev.camera.desktop >%{buildroot}%{_datadir}/applications/ch.lindev.camera.front.desktop

%files
%{_bindir}/camera
%{_bindir}/cameraf
%{_datadir}/applications/ch.lindev.camera.desktop
%{_datadir}/applications/ch.lindev.camera.front.desktop
%{_datadir}/icons/hicolor/scalable/apps/ch.lindev.camera.svg
