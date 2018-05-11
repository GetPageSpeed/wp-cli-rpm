# License: MIT
# http://opensource.org/licenses/MIT

Name: wp-cli
Version: 1.5.1
Release: 1%{?dist}
Summary: The command line interface for WordPress

License: MIT 
URL: https://wp-cli.org/
Source0: https://github.com/wp-cli/%{name}/releases/download/v%{version}/%{name}-%{version}.phar

BuildArch: noarch

Requires:  php(language) >= 5.5
Requires:  php-mbstring
Requires:  php-openssl
Requires:  php-xml

# TODO: Get info from phpcompatinfo reports for 1.5.0


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
%{__install} -m 755 -p %SOURCE0 $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%defattr(-,root,root)
%{_bindir}/%{name}

%changelog
* Fri May 11 2018 Danila Vershinin <info@getpagespeed.com> 1.5.0-1
- First release

