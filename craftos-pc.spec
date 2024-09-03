Name:           craftos-pc
Version:        2.8.3
Release:        1%{?dist}
Summary:        Advanced ComputerCraft emulator written in C++

License:        MIT
URL:            https://www.craftos-pc.cc/
# REPLACE WITH
# Source0:        https://github.com/MCJack123/craftos2/archive/v%{version}/craftos2-v%{version}.tar.gz
# ONCE https://github.com/MCJack123/craftos2/pull/373 IS MERGED
Source0:        https://github.com/tomodachi94/craftos2/archive/refs/heads/refactor-make-install.zip
Source1:        https://github.com/MCJack123/craftos2-lua/archive/v%{version}/craftos2-lua-v%{version}.tar.gz

BuildRequires:  make, gcc, gcc-c++, SDL2-devel >= 2.0.8, SDL2_mixer-devel, poco-devel, libharu-devel, ncurses-devel, libpng-devel, libwebp-devel, patchelf, unzip

Requires: craftos-pc-data >= 2.5, SDL2 >= 2.0.8, SDL2_mixer, libharu, libpng, ncurses, libwebp

%description


%prep
# REPLACE CURRENT VERSIONS WITH COMMENTED_OUT ONES ONCE PR IS MERGED.
#%setup -n craftos2-%{version} -q
%setup -n craftos2-refactor-make-install -q
#%setup -T -D -a 1 -n craftos2-%{version} -q
%setup -T -D -a 1 -n craftos2-refactor-make-install -q
cp -R craftos2-lua-%{version}/* craftos2-lua/

%build
# Build the custom lua version
make -C craftos2-lua -j$(nproc) linux
# Configure and build CraftOS-PC itself
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%license LICENSE
%{_libdir}/libcraftos2-liblua.so
%{_bindir}/craftos
%{_datadir}/applications/CraftOS-PC.desktop
%{_datadir}/icons/hicolor/16x16/apps/craftos.png
%{_datadir}/icons/hicolor/24x24/apps/craftos.png
%{_datadir}/icons/hicolor/32x32/apps/craftos.png
%{_datadir}/icons/hicolor/48x48/apps/craftos.png
%{_datadir}/icons/hicolor/64x64/apps/craftos.png
%{_datadir}/icons/hicolor/96x96/apps/craftos.png
%{_datadir}/icons/hicolor/128x128/apps/craftos.png
%{_datadir}/icons/hicolor/256x256/apps/craftos.png
%{_datadir}/icons/hicolor/1024x1024/apps/craftos.png

%changelog
