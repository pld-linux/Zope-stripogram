%define		zope_subname	stripogram
Summary:	Library for converting HTML to Plain Text
Summary(pl):	Biblioteka konwertuj±ca format HTML do zwyk³ego tekstu
Name:		Zope-%{zope_subname}
Version:	1.4
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/squishdot/%{zope_subname}-1-4.tgz
# Source0-md5:	d09a0fa325ec2ae9a6a94b0b4aabd408
URL:		http://zope.org/Members/chrisw/StripOGram/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
stripogram is a library for converting HTML to Plain Text.

%description -l pl
stripogram jest bibliotek± konwertuj±c± format HTML do zwyk³ego
tekstu.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af *.py $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc readme.txt
%{_datadir}/%{name}
