%global module h11

%bcond_with tests

Name:           python-h11
Version:        0.14.0
Release:        3
Summary:        A pure-Python, bring-your-own-I/O implementation of HTTP/1.1
License:        MIT
URL:            https://github.com/python-hyper/h11
Source0:        https://files.pythonhosted.org/packages/source/h/h11/h11-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

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

%files
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/h11
%{python_sitelib}/h11-%{version}*-info

#----------------------------------------------------------------------------

%prep
%autosetup -n h11-%{version}
rm -rf h11.egg-info

%build
%py_build

%install
%py_install

%if %{with tests}
%check
py.test-%{python_version} --verbose
%endif

