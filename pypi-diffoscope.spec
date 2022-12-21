#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1E953E27D4311E58 (lamby@gnu.org)
#
Name     : pypi-diffoscope
Version  : 229
Release  : 207
URL      : https://files.pythonhosted.org/packages/78/73/788421456661a8f1a8fabacb2abb489e5ed3b28879f240ce31ceb367f2d8/diffoscope-229.tar.gz
Source0  : https://files.pythonhosted.org/packages/78/73/788421456661a8f1a8fabacb2abb489e5ed3b28879f240ce31ceb367f2d8/diffoscope-229.tar.gz
Source1  : https://files.pythonhosted.org/packages/78/73/788421456661a8f1a8fabacb2abb489e5ed3b28879f240ce31ceb367f2d8/diffoscope-229.tar.gz.asc
Summary  : in-depth comparison of files, archives, and directories
Group    : Development/Tools
License  : GPL-3.0
Requires: pypi-diffoscope-bin = %{version}-%{release}
Requires: pypi-diffoscope-license = %{version}-%{release}
Requires: pypi-diffoscope-python = %{version}-%{release}
Requires: pypi-diffoscope-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : libarchive-dev
BuildRequires : pypi(libarchive_c)
BuildRequires : pypi(python_magic)
BuildRequires : rpm

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
%setup -q -n diffoscope-229
cd %{_builddir}/diffoscope-229
pushd ..
cp -a diffoscope-229 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671642021
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-diffoscope
cp %{_builddir}/diffoscope-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-diffoscope/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
