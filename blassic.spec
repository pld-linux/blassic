Summary:	Classic Basic interpreter
Summary(pl):	Interpreter klasycznego Basica
Name:		blassic
Version:	0.4.4
Release:	1
License:	GPL v2
Group:		Development/Languages
Source0:	http://www.arrakis.es/~ninsesabe/%{name}/%{name}-%{version}.tgz
URL:		http://www.arrakis.es/~ninsesabe/blassic/
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

%build
%configure
# Yes, they don't know how to use ac properly
%{__make} CPPFLAGS='-I%{_includedir}/ncurses' CXXFLAGS='%{rpmcflags}'

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT examplesdir=%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS THANKS
%doc %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/*
