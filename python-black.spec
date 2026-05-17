%define module black
# disable test on abf
%bcond tests 1

Name:		python-black
Version:	26.5.0
Release:	1
Summary:	The uncompromising code formatter
License:	MIT
Group:		Development/Python
URL:		https://github.com/psf/black
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(click)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-fancy-pypi-readme)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(mypy)
BuildRequires:	python%{pyver}dist(mypy-extensions)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pathspec)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(platformdirs)
BuildRequires:	python%{pyver}dist(pytokens)
BuildRequires:	python%{pyver}dist(wheel)
# optionals
BuildRequires:	python%{pyver}dist(aiohttp)
BuildRequires:	python%{pyver}dist(colorama)
BuildRequires:	python%{pyver}dist(ipython)
BuildRequires:	python%{pyver}dist(uvloop)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

Suggests:	python%{pyver}dist(aiohttp)

%description
Black is the uncompromising Python code formatter. By using it, you agree to
cease control over minutiae of hand-formatting. In return, Black gives you
speed, determinism, and freedom from pycodestyle nagging about formatting.
You will save time and mental energy for more important matters.

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
export PIP_INDEX_URL=http://host.invalid./
export PIP_NO_DEPS=yes
pytest -Wdefault -rs --run-optional no_jupyter
%endif

%files
%{_bindir}/%{module}
%{_bindir}/%{module}d
%{python_sitelib}/_black_version.py
%{python_sitelib}/_black_version.pyi
%{python_sitelib}/blib2to3/
%{python_sitelib}/__pycache__/_%{module}*.pyc
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}d/
%{python_sitelib}/%{module}-%{version}.dist-info
