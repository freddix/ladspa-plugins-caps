Summary:	C* Audio Plugin Suite
Name:		ladspa-plugins-caps
Version:	0.9.10
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://quitte.de/dsp/caps_%{version}.tar.bz2
# Source0-md5:	dac87bf3a967b6f6ddcea1d90b6f4808
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of refined LADSPA audio plugins capable of
(and mainly intended for) realtime operation. The suite includes
DSP units emulating instrument amplifiers, stomp-box classics,
versatile 'virtual analogue' oscillators, fractal oscillation,
reverb, equalization and more.

%prep
%setup -qn caps-%{version}

%build
%{__make} \
	OPTS="%{rpmcflags} -Wall -fPIC -DPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -D caps.so $RPM_BUILD_ROOT%{_libdir}/ladspa/caps.so
install -D caps.rdf $RPM_BUILD_ROOT%{_datadir}/ladspa/rdf/caps.rdf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/*.rdf

