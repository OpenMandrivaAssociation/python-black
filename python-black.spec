%define module black
%bcond_without test

Name:           python-black
Version:        25.1.0
Release:        1
Summary:        The uncompromising code formatter
License:        MIT
URL:            https://github.com/psf/black
Source0:        https://files.pythonhosted.org/packages/source/b/black/%{module}-%{version}.tar.gz
 
BuildArch:      noarch
 
BuildRequires:	python
BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(click)
BuildRequires:  python%{pyver}dist(hatchling)
BuildRequires:  python%{pyver}dist(hatch-fancy-pypi-readme)
BuildRequires:  python%{pyver}dist(hatch-vcs)
BuildRequires:  python%{pyver}dist(mypy)
BuildRequires:  python%{pyver}dist(mypy-extensions)
BuildRequires:  python%{pyver}dist(packaging)
BuildRequires:  python%{pyver}dist(pathspec)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(platformdirs)
BuildRequires:  python%{pyver}dist(tomli)
BuildRequires:  python%{pyver}dist(typing-extensions)
BuildRequires:  python%{pyver}dist(wheel)
# optionals
BuildRequires:  python%{pyver}dist(aiohttp)
BuildRequires:  python%{pyver}dist(colorama)
BuildRequires:  python%{pyver}dist(ipython)
BuildRequires:  python%{pyver}dist(uvloop)
%if %{with test}
BuildRequires:  python%{pyver}dist(coverage)
BuildRequires:  python%{pyver}dist(hypothesis)
BuildRequires:  python%{pyver}dist(pluggy)
BuildRequires:  python%{pyver}dist(pre-commit)
BuildRequires:  python%{pyver}dist(pytest)
BuildRequires:  python%{pyver}dist(pytest-cov)

%endif

Suggests:	python%{pyver}dist(aiohttp)

%description
Black is the uncompromising Python code formatter. By using it, you agree to
cease control over minutiae of hand-formatting. In return, Black gives you
speed, determinism, and freedom from pycodestyle nagging about formatting.
You will save time and mental energy for more important matters.
    
%prep
%autosetup -n %{module}-%{version} -p1
  
%build
%py_build
  
%install
%py_install

%if %{with test}
%check
pytest -v tests/
%endif
  
%files
%{_bindir}/%{module}
%{_bindir}/%{module}d
%{python_sitelib}/_black_version.py
%{python_sitelib}/blib2to3/
%{python_sitelib}/__pycache__/_%{module}*.pyc
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}d/
%{python_sitelib}/%{module}-%{version}.dist-info
