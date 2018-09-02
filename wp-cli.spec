# License: MIT
# http://opensource.org/licenses/MIT

Name: wp-cli
Version: 2.0.1
Release: 2%{?dist}
Summary: The command line interface for WordPress

License: MIT 
URL: https://wp-cli.org/
Source0: https://github.com/wp-cli/%{name}/releases/download/v%{version}/%{name}-%{version}.phar
Source1: https://raw.githubusercontent.com/wp-cli/wp-cli/master/LICENSE

BuildArch: noarch

Requires:  php(language) >= 5.3
Requires:  php-mbstring
Requires:  php-openssl
Requires:  php-xml

%description
WP-CLI is the command-line interface for WordPress. You can 
update plugins, configure multisite installs and much more, 
without using a web browser.


%prep
# Nothing to do


%build
# Nothing to do


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 755 -p %SOURCE0 $RPM_BUILD_ROOT%{_bindir}/wp
%{__mkdir} -p $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
%{__install} -m 644 -p %SOURCE1 $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/

%files
%defattr(-,root,root)
%{_bindir}/wp
# Virtually add license macro for EL6:
%{!?_licensedir:%global license %%doc}
%dir %{_datadir}/doc/%{name}
%license %{_datadir}/doc/%{name}/LICENSE

%changelog
* Sun Sep 2 2018 Danila Vershinin <info@getpagespeed.com> 2.0.1-2
- install LICENSE as well

* Fri Aug 24 2018 Danila Vershinin <info@getpagespeed.com> 2.0.1-1
- upstream version auto-updated to 2.0.1

* Thu Aug 09 2018 Danila Vershinin <info@getpagespeed.com> 2.0.0-1
- upstream version auto-updated to 2.0.0

* Sat May 12 2018 Danila Vershinin <info@getpagespeed.com> 1.5.1-3
- Relax minimum PHP requirements to PHP 5.3

* Sat May 12 2018 Danila Vershinin <info@getpagespeed.com> 1.5.1-2
- Fix the name of executable file

* Fri May 11 2018 Danila Vershinin <info@getpagespeed.com> 1.5.0-1
- First release

