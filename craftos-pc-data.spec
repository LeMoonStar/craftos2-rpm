Name:       craftos-pc-data
Version:    2.6.2
Release:    1%{dist}
Summary:    ROM package for CraftOS-PC
BuildArch:  noarch

URL:        https://github.com/MCJack123/craftos2-rom
License:    CCPL
Source0:    https://github.com/MCJack123/craftos2-rom/archive/refs/tags/v%{version}.tar.gz

%description

%prep
ls -la
%setup -n craftos2-rom-v%{version} -q
ls -la

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/craftos
cp -R ./* %{buildroot}/usr/share/craftos/

%files
/usr/share/craftos/
