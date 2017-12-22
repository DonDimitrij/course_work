Name: cours_work 
Version: 1.0 
Release: 1
Summary: Тестовое прмложение для проверки скрипата авто сборки
Group: Development/Tools
License: proprietary 
Source0: cours_work.tar.gz 
BuildArch: x86_64 
BuildRoot: /tmp/cours_work

%description 
Тестовое прмложение для проверки скрипата авто сборки

%prep
%setup -q -n cours_work

%build
qmake4 CONFIG+=build_all cours_work.pro
make

%install
mkdir -p /usr/local/sbin/app
mkdir -p /usr/local/sbin/test

INSTALL_ROOT=$RPM_BUILD_ROOT make install

cd app/release
install app /usr/local/sbin/
cd ../../test/release
install tst_testtest /usr/local/sbin/

%files
%defattr(-,root,root)
/usr/local/sbin/app/app
/usr/local/sbin/test/tst_testtest

%changelog
* Tue Dec 21 2017 Kozlov
- Test RPM packet created.
