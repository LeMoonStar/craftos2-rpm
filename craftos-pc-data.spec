Name:       craftos-pc-data
Version:    2.6.2
Release:    1%{dist}
Summary:    ROM package for CraftOS-PC
BuildArch:  noarch

URL:        https://github.com/MCJack123/craftos2-rom
License:    CCPL
Source0:    https://github.com/MCJack123/craftos2-rom/archive/refs/tags/craftos2-rom-%{version}.tar.gz

%description

%prep
%setup -n craftos2-rom-%{version} -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/craftos
cp -R ./* %{buildroot}/usr/share/craftos/

%files
/usr/share/craftos/
