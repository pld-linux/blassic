Summary:	Classic Basic interpreter
Summary(pl):	Interpreter klasycznego Basica
Name:		blassic
Version:	0.8.1
Release:	1
License:	GPL v2
Group:		Development/Languages
Source0:	http://www.arrakis.es/~ninsesabe/%{name}/%{name}-%{version}.tgz
# Source0-md5:	22e9c257463d77ddddbbb82a3c926cc7
Patch0:		%{name}-ac_fix.patch
URL:		http://www.arrakis.es/~ninsesabe/blassic/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blassic is a classic Basic interpreter. The line numbers are
mandatory, and it has PEEK & POKE. The main goal is to execute
programs written in old interpreters, but it can be used as a
scripting language.

%description -l pl
Blassic jest interpreterem klasycznego Basica. Numeracja linii jest
obligatoryjna, PEEK i POKE s� obs�ugiwane. G��wnym jego przeznaczeniem
jest wykonywanie program�w napisanych dla starych interpreter�w, ale
mo�e by� tak�e wykorzystany do uruchamiania skrypt�w.

%prep
%setup -q
%patch0 -p1
mv -f aclocal.m4 acinclude.m4

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} \
	CPPFLAGS="-I/usr/include/ncurses"

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
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
