# what it's called on pypi
%global srcname h11
# what it's imported as
%global libname h11
# name of egg info directory
%global eggname h11
# package name fragment
%global pkgname h11

%bcond_without tests


Name:           python-%{pkgname}
Version:        0.9.0
Release:        1
Summary:        A pure-Python, bring-your-own-I/O implementation of HTTP/1.1
License:        MIT
URL:            https://github.com/python-hyper/h11
Source0:        https://github.com/python-hyper/h11/archive/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description
This is a little HTTP/1.1 library written from scratch in Python, heavily\
inspired by hyper-h2.  It is a "bring-your-own-I/O" library; h11 contains no IO\
code whatsoever.  This means you can hook h11 up to your favorite network API,\
and that could be anything you want: synchronous, threaded, asynchronous, or\
your own implementation of RFC 6214 -- h11 will not judge you.  This also means\
that h11 is not immediately useful out of the box: it is a toolkit for building\
programs that speak HTTP, not something that could directly replace requests or\
twisted.web or whatever.  But h11 makes it much easier to implement something\
like requests or twisted.web.


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info

%build
%py_build

%install
%py_install

%if %{with tests}
%check
py.test-%{python_version} --verbose
%endif


%files
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/%{libname}
%{python_sitelib}/%{eggname}-%{version}-py%{python_version}.egg-info
