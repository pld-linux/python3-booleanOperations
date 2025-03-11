#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Boolean operations on paths
Summary(pl.UTF-8):	Operacje logiczne na ścieżkach
Name:		python3-booleanOperations
Version:	0.9.0
Release:	5
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/booleanOperations/
Source0:	https://files.pythonhosted.org/packages/source/b/booleanOperations/booleanOperations-%{version}.zip
# Source0-md5:	a5bbdb108b0fc58a6f7effcc27c51285
Patch0:		%{name}-deps.patch
URL:		https://pypi.org/project/booleanOperations/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm >= 1.14.1
%if %{with tests}
BuildRequires:	python3-fontPens
BuildRequires:	python3-fonttools >= 4.0.2
BuildRequires:	python3-pyclipper >= 1.1.0.post1
BuildRequires:	python3-pytest >= 3.0.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Boolean operations on paths using a super fast polygon clipper
library by Angus Johnson.

%description -l pl.UTF-8
Operacje logiczne na ścieżkach przy użyciu bardzo szybkiej
biblioteki obcinania wielokątów autorstwa Angusa Johnsona.

%prep
%setup -q -n booleanOperations-%{version}
%patch -P 0 -p1

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/Lib \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/booleanOperations
%{py3_sitescriptdir}/booleanOperations-%{version}-py*.egg-info
