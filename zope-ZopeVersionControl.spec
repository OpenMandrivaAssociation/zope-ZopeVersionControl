%define Product ZopeVersionControl
%define product zopeversioncontrol
%define name    zope-%{Product}
%define version 0.3.4
%define release %mkrel 5

%define zope_minver     2.7
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Zope Version Control
License:    GPL
Group:      System/Servers
URL:        https://wiki.zope.org/ZPT/ZopeVersionControl/FrontPage
Source:     http://antiloop.plone.org/download/%{product}/releases/%{version}/%{Product}-%{version}.tar.gz
Requires:   zope >= %{zope_minver}
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This project aims to provide tools to achieve common version control goals of
content management applications.

%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
