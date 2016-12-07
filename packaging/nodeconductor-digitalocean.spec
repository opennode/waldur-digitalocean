Name: nodeconductor-digitalocean
Summary: DigitalOcean plugin for NodeConductor
Group: Development/Libraries
Version: 0.1.2
Release: 1.el7
License: MIT
Url: http://nodeconductor.com
Source0: %{name}-%{version}.tar.gz

Requires: nodeconductor >= 0.110.0
Requires: python-digitalocean >= 1.5

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: python-setuptools

%description
DigitalOcean plugin for NodeConductor.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*

%changelog
* Wed Dec 7 2016 Jenkins <jenkins@opennodecloud.com> - 0.1.2-1.el7
- New upstream release

* Tue Dec 6 2016 Jenkins <jenkins@opennodecloud.com> - 0.1.1-1.el7
- New upstream release

* Tue Dec 6 2016 Jenkins <jenkins@opennodecloud.com> - 0.1.0-1.el7
- New upstream release

* Wed Nov 30 2016 Dmitri Tsumak <dmitri@opennodecloud.com> - 0.1.0-1.el7
- Initial version of the package
