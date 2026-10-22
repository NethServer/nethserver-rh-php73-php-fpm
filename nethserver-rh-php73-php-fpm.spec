Name: nethserver-rh-php73-php-fpm
Version: 1.0.1
Release: 1%{?dist}
Summary: NethServer rh-php73-php-fpm configuration
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: nethserver-devtools

Requires: rh-php73, rh-php73-php-fpm
Requires: rh-php73-php-bcmath, rh-php73-php-gd, sclo-php73-php-imap
Requires: rh-php73-php-ldap, rh-php73-php-enchant, rh-php73-php-mbstring
Requires: rh-php73-php-pdo, sclo-php73-php-tidy, rh-php73-php-mysqlnd
Requires: rh-php73-php-soap, rh-php73-php-pgsql
Requires: rh-php73-php-pecl-apcu, rh-php73-php-intl
Requires: rh-php73-php-opcache

%description
Basic support for PHP 7.3 using SCL

%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist


%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update


%changelog
* Thu Oct 22 2026 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- PHP critical RCE vulnerabilities (CVE-2026-109618 / CVE-2026-109619) - NethServer/dev#8256

* Thu Mar 26 2020 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-1
- Nethserver-rh-php73-php-fpm - NethServer/dev#6087

