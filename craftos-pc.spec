Name:           craftos-pc
Version:        2.6.2
Release:        1%{?dist}
Summary:        Advanced ComputerCraft emulator written in C++

License:        MIT
URL:            https://www.craftos-pc.cc/
Source0:        https://github.com/MCJack123/craftos2/archive/v%{version}/craftos2-v%{version}.tar.gz
Source1:        https://github.com/MCJack123/craftos2-lua/archive/v%{version}/craftos2-lua-v%{version}.tar.gz


BuildRequires:  make, gcc, SDL2-devel >= 2.0.8, SDL2_mixer-devel, poco-devel, libharu-devel, ncurses-devel, libpng-devel, libwebp-devel, patchelf, unzip

Requires: craftos-pc-data >= 2.5, SDL2 >= 2.0.8, SDL2_mixer, libharu, libpng, ncurses, libwebp

%description


%prep
%setup -n craftos2-%{version} -q
%setup -T -D -a 1 -n craftos2-%{version} -q
cp -R craftos2-lua-%{version}/* craftos2-lua/
mkdir icons
unzip resources/linux-icons.zip -d icons


%build
make -C craftos2-lua -j$(nproc) linux
%configure
make -j$(nproc)


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p "%{buildroot}%{_bindir}"
DESTDIR="%{buildroot}%{_bindir}" make install
install -D -m 0755 craftos2-lua/src/liblua.so "%{buildroot}%{_libdir}/libcraftos2-lua.so"
patchelf --replace-needed craftos2-lua/src/liblua.so libcraftos2-lua.so "%{buildroot}%{_bindir}/craftos"
mkdir -p "%{buildroot}%{_includedir}"
cp -R api "%{buildroot}%{_includedir}/CraftOS-PC"
install -D -m 0644 icons/CraftOS-PC.desktop "%{buildroot}%{_datadir}/applications/CraftOS-PC.desktop"
install -D -m 0644 icons/16.png "%{buildroot}%{_datadir}/icons/hicolor/16x16/apps/craftos.png"
install -D -m 0644 icons/24.png "%{buildroot}%{_datadir}/icons/hicolor/24x24/apps/craftos.png"
install -D -m 0644 icons/32.png "%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/craftos.png"
install -D -m 0644 icons/48.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/craftos.png"
install -D -m 0644 icons/64.png "%{buildroot}%{_datadir}/icons/hicolor/64x64/apps/craftos.png"
install -D -m 0644 icons/96.png "%{buildroot}%{_datadir}/icons/hicolor/96x96/apps/craftos.png"

%files
%license LICENSE
%doc DOCUMENTATION.md
%{_libdir}/libcraftos2-lua.so
%{_bindir}/craftos
%{_includedir}/CraftOS-PC
%{_datadir}/applications/CraftOS-PC.desktop
%{_datadir}/icons/hicolor/16x16/apps/craftos.png
%{_datadir}/icons/hicolor/24x24/apps/craftos.png
%{_datadir}/icons/hicolor/32x32/apps/craftos.png
%{_datadir}/icons/hicolor/48x48/apps/craftos.png
%{_datadir}/icons/hicolor/64x64/apps/craftos.png
%{_datadir}/icons/hicolor/96x96/apps/craftos.png

%changelog
