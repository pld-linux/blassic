Summary:	Classic Basic interpreter
Summary(pl):	Interpreter klasycznego Basica
Name:		blassic
Version:	0.5.7
Release:	1
License:	GPL v2
Group:		Development/Languages
Source0:	http://www.arrakis.es/~ninsesabe/%{name}/%{name}-%{version}.tgz
# Source0-md5:	e99839c048d5ac81a17eeb76f9abd823
Patch0:		%{name}-ac_fix.patch
URL:		http://www.arrakis.es/~ninsesabe/blassic/
BuildRequires:	ncurses-devel
BuildRequires:	XFree86-devel
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
%setup -q
%patch0 -p1

%build
rm -f missing
mv -f aclocal.m4 acinclude.m4
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	examplesdir=%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%doc %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/*
