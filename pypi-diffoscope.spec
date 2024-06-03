#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v12
# autospec commit: fbcebd0
#
Name     : pypi-diffoscope
Version  : 269
Release  : 250
URL      : https://files.pythonhosted.org/packages/4d/3d/c6753ae5e63b41f745e4918544f8a73e0819071599beff7170fd6ea42801/diffoscope-269.tar.gz
Source0  : https://files.pythonhosted.org/packages/4d/3d/c6753ae5e63b41f745e4918544f8a73e0819071599beff7170fd6ea42801/diffoscope-269.tar.gz
Summary  : in-depth comparison of files, archives, and directories
Group    : Development/Tools
License  : GPL-3.0 MIT
Requires: pypi-diffoscope-bin = %{version}-%{release}
Requires: pypi-diffoscope-license = %{version}-%{release}
Requires: pypi-diffoscope-python = %{version}-%{release}
Requires: pypi-diffoscope-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : libarchive-dev
BuildRequires : rpm
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
diffoscope
==========
.. image:: https://badge.fury.io/py/diffoscope.svg
:target: http://badge.fury.io/py/diffoscope

%package bin
Summary: bin components for the pypi-diffoscope package.
Group: Binaries
Requires: pypi-diffoscope-license = %{version}-%{release}

%description bin
bin components for the pypi-diffoscope package.


%package license
Summary: license components for the pypi-diffoscope package.
Group: Default

%description license
license components for the pypi-diffoscope package.


%package python
Summary: python components for the pypi-diffoscope package.
Group: Default
Requires: pypi-diffoscope-python3 = %{version}-%{release}

%description python
python components for the pypi-diffoscope package.


%package python3
Summary: python3 components for the pypi-diffoscope package.
Group: Default
Requires: python3-core
Provides: pypi(diffoscope)
Requires: pypi(libarchive_c)
Requires: pypi(python_magic)

%description python3
python3 components for the pypi-diffoscope package.


%prep
%setup -q -n diffoscope-269
cd %{_builddir}/diffoscope-269
pushd ..
cp -a diffoscope-269 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1717431877
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
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-diffoscope
cp %{_builddir}/diffoscope-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-diffoscope/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/diffoscope-%{version}/debian/copyright %{buildroot}/usr/share/package-licenses/pypi-diffoscope/c5721cab069b36c92f0cecbcc66f1699790b3fe6 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/diffoscope

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-diffoscope/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/pypi-diffoscope/c5721cab069b36c92f0cecbcc66f1699790b3fe6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
