Name:           python-black
Version:        22.3.0
Release:        1
Summary:        The uncompromising code formatter
License:        MIT
URL:            https://github.com/psf/black
Source0:        https://files.pythonhosted.org/packages/source/b/black/black-%{version}.tar.gz
 
BuildArch:      noarch
 
BuildRequires:  pkgconfig(python)

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