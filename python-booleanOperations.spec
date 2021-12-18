#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-booleanOperations.spec)

Summary:	Boolean operations on paths
Summary(pl.UTF-8):	Operacje logiczne na ścieżkach
Name:		python-booleanOperations
# keep 0.8.x here for python2 support
Version:	0.8.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/booleanOperations/
Source0:	https://files.pythonhosted.org/packages/source/b/booleanOperations/booleanOperations-%{version}.zip
# Source0-md5:	d4ddd0f486e4b213d35d4071aa47d864
URL:		https://pypi.org/project/booleanOperations/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm >= 1.14.1
%if %{with tests}
BuildRequires:	python-fontPens
BuildRequires:	python-fonttools >= 3.32.0
BuildRequires:	python-pyclipper >= 1.0.5
BuildRequires:	python-pytest >= 3.0.2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm >= 1.14.1
%if %{with tests}
BuildRequires:	python3-fontPens
BuildRequires:	python3-fonttools >= 3.32.0
BuildRequires:	python3-pyclipper >= 1.0.5
BuildRequires:	python3-pytest >= 3.0.2
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Boolean operations on paths using a super fast polygon clipper
library by Angus Johnson.

%description -l pl.UTF-8
Operacje logiczne na ścieżkach przy użyciu bardzo szybkiej
biblioteki obcinania wielokątów autorstwa Angusa Johnsona.

%package -n python3-booleanOperations
Summary:	Boolean operations on paths
Summary(pl.UTF-8):	Operacje logiczne na ścieżkach
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-booleanOperations
Boolean operations on paths using a super fast polygon clipper
library by Angus Johnson.

%description -n python3-booleanOperations -l pl.UTF-8
Operacje logiczne na ścieżkach przy użyciu bardzo szybkiej
biblioteki obcinania wielokątów autorstwa Angusa Johnsona.

%prep
%setup -q -n booleanOperations-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/Lib \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/Lib \
%{__python3} -m pytest tests
%endif
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
%doc LICENSE README.rst
%{py_sitescriptdir}/booleanOperations
%{py_sitescriptdir}/booleanOperations-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-booleanOperations
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/booleanOperations
%{py3_sitescriptdir}/booleanOperations-%{version}-py*.egg-info
%endif
