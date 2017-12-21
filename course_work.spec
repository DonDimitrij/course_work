Name: cours_work 
Version: 1.0 
Release: 1
Summary: Тестовое приложение для проверки работы скрипта
Group: Development/Tools
License: proprietary 
Source0: build.tar.gz 
BuildArch: x86_64 
BuildRoot: %{_tmppath}/repositories

%description 
Тестовое приложение для проверки работы скрипта

%prep
%setup -q -n cours_work

%build
qmake4 -r CONFIG+=build_all cours_work.pro
make all

%install
mkdir -p $RPM_BUILD_ROOT/usr/sbin/app
mkdir -p $RPM_BUILD_ROOT/usr/sbin/test

cd app/release
install app $RPM_BUILD_ROOT/usr/sbin/
cd ../../test/release
install tst_testtest $RPM_BUILD_ROOT/usr/sbin/

%files
%defattr(-,root,root)
/usr/sbin/app
/usr/sbin/tst_testtest

%clean
make clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Dec 21 2017 Kozlov
- Test RPM packet created.