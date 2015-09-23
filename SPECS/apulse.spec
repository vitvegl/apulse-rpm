%define debug_package %{nil}
%define __protect [ "${RPM_BUILD_ROOT}" != "/" ]
%define __build_dir %{_builddir}/%{name}-%{version}

Name:           apulse		
Version:	0.1.6
Release:	1%{?dist}
Summary:        PulseAudio emulation for ALSA
Provides:       pulseaudio
Group:          System/Environment
License:        MIT
URL:            https://github.com/i-rinat/apulse
Source0:        %{name}-%{version}.tar.gz

BuildRequires: gcc-sh-linux-gnu cmake alsa-lib-devel glib2-devel
Requires:      alsa-lib glib2

%description
PulseAudio emulation for ALSA.
Project is in stale state since its proclamation.
The main objective, working Skype test call, is reached.
I don't have any plans for further development

%prep
%setup -q


%build
cd %{__build_dir} && \
mkdir build && cd build

%if 0%{__isa_bits} == 64
cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release .. && \
make
%else
CFLAGS=-m32 cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release .. && \
make
%endif

%install
cd %{__build_dir}/build && \
make install DESTDIR=%{buildroot}

%clean
%{__protect} && rm -rf ${RPM_BUILD_ROOT}

%files
%doc
%{_bindir}/%{name}
%dir /usr/lib/%{name}
/usr/lib/%{name}/libpulse-simple.so
/usr/lib/%{name}/libpulse-simple.so.0
/usr/lib/%{name}/libpulse.so
/usr/lib/%{name}/libpulse.so.0
/usr/lib/%{name}/libpulsecommon-5.0.so

%changelog
* Wed Sep 23 2015 <vitvegl@quintagroup.org> - 0.1.6-1
- initial build

