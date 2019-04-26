Summary: A bash completion helper for wp-cli
Name: wp-cli-completion-bash
Version: 2.2.0
Release: 1%{?dist}
License: GPL
URL: https://github.com/wp-cli/wp-cli

Source0: https://github.com/wp-cli/wp-cli/archive/v%{version}/wp-cli-%{version}.tar.gz
Source1: https://raw.githubusercontent.com/wp-cli/wp-cli/master/LICENSE

BuildArch: noarch
Requires: bash-completion

%description
Install this package to enable tab-completion of functions and installed
modules with the wp-cli command.

%prep
%setup -n wp-cli-%{version}


%build
# Nothing to do

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -d -m0755 $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/
%{__install} -Dp -m0755 utils/wp-completion.bash $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/
%{__mkdir} -p $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
%{__install} -m 644 -p %SOURCE1 $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/

%post
. /etc/profile.d/bash_completion.sh

%postun
. /etc/profile.d/bash_completion.sh

%files
%defattr(-, root, root, 0755)
%config %{_sysconfdir}/bash_completion.d/*
# Virtually add license macro for EL6:
%{!?_licensedir:%global license %%doc}
%dir %{_datadir}/doc/%{name}
%license %{_datadir}/doc/%{name}/LICENSE

%changelog
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

* Sun May 27 2018 Danila Vershinin <info@getpagespeed.com> 1.5.1-1
- initial release

