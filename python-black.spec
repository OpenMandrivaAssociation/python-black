Name:           python-black
Version:        22.6.0
Release:        2
Summary:        The uncompromising code formatter
License:        MIT
URL:            https://github.com/psf/black
Source0:        https://files.pythonhosted.org/packages/source/b/black/black-%{version}.tar.gz
 
BuildArch:      noarch
 
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(tomli)

%description
Black is the uncompromising Python code formatter. By using it, you agree to
cease control over minutiae of hand-formatting. In return, Black gives you
speed, determinism, and freedom from pycodestyle nagging about formatting.
You will save time and mental energy for more important matters.
    
%prep
%autosetup -n black-%{version} -p1
  
%build
%py_build
  
%install
%py_install
  
%files
%{_bindir}/black
%{_bindir}/blackd
%{python_sitelib}/_black_version.py
%{python_sitelib}/black-%{version}-py*.*.egg-info
%{python_sitelib}/black/
%{python_sitelib}/blackd/
%{python_sitelib}/blib2to3/
