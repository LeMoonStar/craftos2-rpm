Name:           craftos-pc-accelerated
Version:        2.8
Release:        1%{?dist}
Summary:        Advanced ComputerCraft emulator written in C++, using the LuaJIT engine

License:        MIT
URL:            https://www.craftos-pc.cc/
Source0:        https://github.com/MCJack123/craftos2/archive/v%{version}-luajit/craftos2-v%{version}-luajit.tar.gz
Source1:        https://github.com/MCJack123/craftos2-luajit/archive/v2.7.5/craftos2-luajit-v2.7.5.tar.gz


BuildRequires:  make, gcc, gcc-c++, SDL2-devel >= 2.0.8, SDL2_mixer-devel, poco-devel, libharu-devel, ncurses-devel, libpng-devel, libwebp-devel, unzip

Requires: craftos-pc-data >= 2.5, SDL2 >= 2.0.8, SDL2_mixer, libharu, libpng, ncurses, libwebp

%description


%prep
%setup -n craftos2-%{version}-luajit -q
%setup -T -D -a 1 -n craftos2-%{version}-luajit -q
cp -R craftos2-luajit-2.7.5/* craftos2-luajit/
mkdir icons
unzip resources/linux-icons.zip -d icons

make -C craftos2-luajit -j$(nproc)
%configure
make -j$(nproc)


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p "%{buildroot}%{_bindir}"
install -D -m 0755 craftos "%{buildroot}%{_bindir}/craftos-luajit"
install -D -m 0644 icons/CraftOS-PC.desktop "%{buildroot}%{_datadir}/applications/CraftOS-PC-Accelerated.desktop"
install -D -m 0644 icons/16.png "%{buildroot}%{_datadir}/icons/hicolor/16x16/apps/craftos-luajit.png"
install -D -m 0644 icons/24.png "%{buildroot}%{_datadir}/icons/hicolor/24x24/apps/craftos-luajit.png"
install -D -m 0644 icons/32.png "%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/craftos-luajit.png"
install -D -m 0644 icons/48.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/craftos-luajit.png"
install -D -m 0644 icons/64.png "%{buildroot}%{_datadir}/icons/hicolor/64x64/apps/craftos-luajit.png"
install -D -m 0644 icons/96.png "%{buildroot}%{_datadir}/icons/hicolor/96x96/apps/craftos-luajit.png"
install -D -m 0644 icons/128.png "%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/craftos-luajit.png"
install -D -m 0644 icons/256.png "%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/craftos-luajit.png"
install -D -m 0644 icons/1024.png "%{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/craftos-luajit.png"

%files
%license LICENSE
%{_bindir}/craftos-luajit
%{_datadir}/applications/CraftOS-PC-Accelerated.desktop
%{_datadir}/icons/hicolor/16x16/apps/craftos-luajit.png
%{_datadir}/icons/hicolor/24x24/apps/craftos-luajit.png
%{_datadir}/icons/hicolor/32x32/apps/craftos-luajit.png
%{_datadir}/icons/hicolor/48x48/apps/craftos-luajit.png
%{_datadir}/icons/hicolor/64x64/apps/craftos-luajit.png
%{_datadir}/icons/hicolor/96x96/apps/craftos-luajit.png
%{_datadir}/icons/hicolor/128x128/apps/craftos-luajit.png
%{_datadir}/icons/hicolor/256x256/apps/craftos-luajit.png
%{_datadir}/icons/hicolor/1024x1024/apps/craftos-luajit.png

%changelog
