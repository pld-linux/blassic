Summary:	Classic Basic interpret
Summary(pl):	Interpreter klasycznego Basica
Name:		blassic
Version:	0.3.4
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.xente.mundo-r.com/notfound/blassic/%{name}0_3_4.tgz
URL:		http://www.xente.mundo-r.com/notfound/blassic/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blassic is a classic Basic interpreter. The line numbers are
mandatory, and it has PEEK & POKE. The main goal is to execute
programs written in old interpreters, but it can be used as a
scripting language.

%description -l pl
Blassic jest interpreterem klasycznego Basica. Numeracja linii jest
obligatoryjna, PEEK i POKE s± obs³ugiwane. G³ównym jego przeznaczeniem
jest wykonywanie programów napisanych dla starych interpreterów, ale
mo¿e byæ tak¿e wykorzystany do uruchamiania skryptów.

%prep
%setup -q -c

%build
%{__make} COPTS='-pedantic -Wall %{rpmcflags} -I%{_includedir}/ncurses'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

install blassic $RPM_BUILD_ROOT%{_bindir}/blassic

cp *.bas $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEW
%doc %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/*
