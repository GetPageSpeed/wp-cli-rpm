# License: MIT
# http://opensource.org/licenses/MIT

Name: wp-cli
Version: 2.8.1
Release: 1%{?dist}
# EPEL now builds a shitty wp-cli that requires Apache to be installed - we don't want this:
Epoch: 1
Summary: The command line interface for WordPress

License: MIT 
URL: https://wp-cli.org/
Source0: https://github.com/wp-cli/wp-cli/archive/v%{version}/wp-cli-%{version}.tar.gz
Source1: https://github.com/wp-cli/%{name}/releases/download/v%{version}/%{name}-%{version}.phar

BuildArch: noarch

Requires:  php(language) >= 5.3
Requires:  php-mbstring
Requires:  php-openssl
Requires:  php-xml

%description
WP-CLI is the command-line interface for WordPress. You can 
update plugins, configure multisite installs and much more, 
without using a web browser.


%package completion-bash
Group:          System Environment/Shells
Summary:        A bash completion helper for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       bash-completion

%description completion-bash
Install this package to enable tab-completion of functions and installed
modules with the %{name} command in bash shell.


%prep
%setup -n wp-cli-%{version}


%build
# Nothing to do


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 755 -p %SOURCE1 $RPM_BUILD_ROOT%{_bindir}/wp
%{__mkdir} -p $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
%{__install} -m 644 -p LICENSE $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/

# bash completions
%if 0%{?rhel} && 0%{?rhel} < 7
%{__install} -Dp -m0644 utils/wp-completion.bash \
  $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}.bash
%else
%{__install} -Dp -m0644 utils/wp-completion.bash \
  $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/%{name}
%endif


%post completion-bash
. /etc/profile.d/bash_completion.sh


%postun completion-bash
. /etc/profile.d/bash_completion.sh


%files
%defattr(-,root,root)
%{_bindir}/wp
# Virtually add license macro for EL6:
%{!?_licensedir:%global license %%doc}
%dir %{_datadir}/doc/%{name}
%license %{_datadir}/doc/%{name}/LICENSE


%files completion-bash
%if 0%{?rhel} && 0%{?rhel} < 7
%config %{_sysconfdir}/bash_completion.d/*
%else
%{_datadir}/bash-completion/completions/*
%endif


%changelog
* Tue Jun 06 2023 Danila Vershinin <info@getpagespeed.com> 2.8.1-1
- release 2.8.1

* Thu Jun 01 2023 Danila Vershinin <info@getpagespeed.com> 2.8.0-1
- release 2.8.0

* Tue Oct 18 2022 Danila Vershinin <info@getpagespeed.com> 2.7.1-1
- release 2.7.1

* Thu Oct 13 2022 Danila Vershinin <info@getpagespeed.com> 2.7.0-1
- release 2.7.0

* Wed Jan 26 2022 Danila Vershinin <info@getpagespeed.com> 2.6.0-1
- release 2.6.0

* Thu May 20 2021 Danila Vershinin <info@getpagespeed.com> 2.5.0-1
- release 2.5.0

* Wed Feb 19 2020 Danila Vershinin <info@getpagespeed.com> 2.4.1-1
- upstream version auto-updated to 2.4.1

* Wed Nov 13 2019 Danila Vershinin <info@getpagespeed.com> 2.4.0-1
- upstream version auto-updated to 2.4.0

* Wed Aug 14 2019 Danila Vershinin <info@getpagespeed.com> 2.3.0-1
- upstream version auto-updated to 2.3.0

* Fri Apr 26 2019 Danila Vershinin <info@getpagespeed.com> 2.2.0-1
- upstream version auto-updated to 2.2.0

* Wed Dec 19 2018 Danila Vershinin <info@getpagespeed.com> 2.1.0-1
- upstream version auto-updated to 2.1.0

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

