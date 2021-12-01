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
%autosetup

%build

%install
ls -la
ls -la %{_builddir}/craftos-pc-devel-%{version}
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/craftos
cp -R %{_builddir}/craftos-pc-devel-%{version}/* %{buildroot}/usr/share/craftos/
ls -la %{buildroot}/usr/share/craftos/

%files
/usr/share/craftos/
