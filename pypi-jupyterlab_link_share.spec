#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v2
# autospec commit: f032afc
#
Name     : pypi-jupyterlab_link_share
Version  : 0.3.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/5f/63/037eef5db99816206935fe491e6cd8b8a72f6933895ec8c1af44eda8eab9/jupyterlab-link-share-0.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5f/63/037eef5db99816206935fe491e6cd8b8a72f6933895ec8c1af44eda8eab9/jupyterlab-link-share-0.3.0.tar.gz
Summary  : JupyterLab Extension to share the URL to a running Jupyter Server
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jupyterlab_link_share-data = %{version}-%{release}
Requires: pypi-jupyterlab_link_share-license = %{version}-%{release}
Requires: pypi-jupyterlab_link_share-python = %{version}-%{release}
Requires: pypi-jupyterlab_link_share-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jupyter_packaging)
BuildRequires : pypi(jupyterlab)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# jupyterlab-link-share
[![Extension status](https://img.shields.io/badge/status-ready-success "ready to be used")](https://jupyterlab-contrib.github.io/)
[![Github Actions Status](https://github.com/jupyterlab-contrib/jupyterlab-link-share/workflows/Build/badge.svg)](https://github.com/jupyterlab-contrib/jupyterlab-link-share/actions/workflows/build.yml)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyterlab-contrib/jupyterlab-link-share/main?urlpath=/lab)

%package data
Summary: data components for the pypi-jupyterlab_link_share package.
Group: Data

%description data
data components for the pypi-jupyterlab_link_share package.


%package license
Summary: license components for the pypi-jupyterlab_link_share package.
Group: Default

%description license
license components for the pypi-jupyterlab_link_share package.


%package python
Summary: python components for the pypi-jupyterlab_link_share package.
Group: Default
Requires: pypi-jupyterlab_link_share-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyterlab_link_share package.


%package python3
Summary: python3 components for the pypi-jupyterlab_link_share package.
Group: Default
Requires: python3-core
Provides: pypi(jupyterlab_link_share)
Requires: pypi(jupyter_server)

%description python3
python3 components for the pypi-jupyterlab_link_share package.


%prep
%setup -q -n jupyterlab-link-share-0.3.0
cd %{_builddir}/jupyterlab-link-share-0.3.0
pushd ..
cp -a jupyterlab-link-share-0.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697493250
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyterlab_link_share
cp %{_builddir}/jupyterlab-link-share-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyterlab_link_share/1205131cb34e2244df162b97848eba8963fa41c1 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
## Remove excluded files
rm -f %{buildroot}*/usr/etc/jupyter/jupyter_notebook_config.d/jupyterlab_link_share.json
rm -f %{buildroot}*/usr/etc/jupyter/jupyter_server_config.d/jupyterlab_link_share.json
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/labextensions/jupyterlab-link-share/build_log.json
/usr/share/jupyter/labextensions/jupyterlab-link-share/install.json
/usr/share/jupyter/labextensions/jupyterlab-link-share/package.json
/usr/share/jupyter/labextensions/jupyterlab-link-share/static/lib_index_js.6e353b15f3ac12b63b8e.js
/usr/share/jupyter/labextensions/jupyterlab-link-share/static/lib_index_js.6e353b15f3ac12b63b8e.js.map
/usr/share/jupyter/labextensions/jupyterlab-link-share/static/remoteEntry.baaa94ab8d652988bfff.js
/usr/share/jupyter/labextensions/jupyterlab-link-share/static/remoteEntry.baaa94ab8d652988bfff.js.map
/usr/share/jupyter/labextensions/jupyterlab-link-share/static/style.js
/usr/share/jupyter/labextensions/jupyterlab-link-share/static/style_index_js.e7915aaf967563326af7.js
/usr/share/jupyter/labextensions/jupyterlab-link-share/static/style_index_js.e7915aaf967563326af7.js.map
/usr/share/jupyter/labextensions/jupyterlab-link-share/static/vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-926fd9.d6183d8565a8d998883e.js
/usr/share/jupyter/labextensions/jupyterlab-link-share/static/vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-926fd9.d6183d8565a8d998883e.js.map
/usr/share/jupyter/labextensions/jupyterlab-link-share/static/vendors-node_modules_retrolab_application_lib_index_js.8bef599bfec9bd786f64.js
/usr/share/jupyter/labextensions/jupyterlab-link-share/static/vendors-node_modules_retrolab_application_lib_index_js.8bef599bfec9bd786f64.js.map

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyterlab_link_share/1205131cb34e2244df162b97848eba8963fa41c1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
