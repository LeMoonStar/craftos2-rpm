Name:       craftos-pc-devel
Version:    2.8.1
Release:    1%{dist}
Summary:    Developement headers for CraftOS-PC
BuildArch:  noarch

URL:        https://www.craftos-pc.cc/
License:    MIT
Source0:    https://github.com/MCJack123/craftos2/archive/v%{version}/craftos2-v%{version}.tar.gz

%description

%prep
%setup -n craftos2-%{version} -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p "%{buildroot}%{_includedir}"
cp -R api "%{buildroot}%{_includedir}/CraftOS-PC"

%files
%license LICENSE
%{_includedir}/CraftOS-PC
