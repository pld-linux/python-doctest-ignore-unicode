#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Add flag to ignore unicode literal prefixes in doctests
Summary(pl.UTF-8):	Flaga do ignorowania prefiksów stałych unikodowych w doctestach
Name:		python-doctest-ignore-unicode
Version:	0.1.2
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/doctest-ignore-unicode/
Source0:	https://files.pythonhosted.org/packages/source/d/doctest-ignore-unicode/doctest-ignore-unicode-%{version}.tar.gz
# Source0-md5:	ba64fe1ef48e8ed68d9ac9a9a03d0c65
URL:		https://pypi.org/project/doctest-ignore-unicode/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
doctest-ignore-unicode is a plugin (currently only for Nose) that adds
a flag to ignore unicode literal prefixes in doctests.

%description -l pl.UTF-8
doctest-ignore-unicode to wtyczka (obecnie tylko dla Nose), dodająca
flagę do ignorowania prefiksów stałych unikodowych w doctestach.

%package -n python3-doctest-ignore-unicode
Summary:	Add flag to ignore unicode literal prefixes in doctests
Summary(pl.UTF-8):	Flaga do ignorowania prefiksów stałych unikodowych w doctestach
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-doctest-ignore-unicode
doctest-ignore-unicode is a plugin (currently only for Nose) that adds
a flag to ignore unicode literal prefixes in doctests.

%description -n python3-doctest-ignore-unicode -l pl.UTF-8
doctest-ignore-unicode to wtyczka (obecnie tylko dla Nose), dodająca
flagę do ignorowania prefiksów stałych unikodowych w doctestach.

%prep
%setup -q -n doctest-ignore-unicode-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/nose_plugin.py[co]
%{py_sitescriptdir}/doctest_ignore_unicode-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-doctest-ignore-unicode
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/nose_plugin.py
%{py3_sitescriptdir}/__pycache__/nose_plugin.cpython-*.py[co]
%{py3_sitescriptdir}/doctest_ignore_unicode-%{version}-py*.egg-info
%endif
