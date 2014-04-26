Name:           linux-firmware
Version:        20140316
Release:        1
Summary:        Firmware for various devices

Group:          System/Kernel
License:        Redistributable, no modification permitted
URL:            http://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Source0:        linux-firmware-%{version}.tar.xz
BuildArch:      noarch

%description
This package contains the firmware required by various devices

%prep
%setup -q -n %{name}-%{version}/upstream

%build
make

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%doc README LICENCE.*
/lib/firmware/*
