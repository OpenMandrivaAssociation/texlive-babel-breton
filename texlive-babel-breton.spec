%global tl_name babel-breton
%global tl_revision 79363

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.1
Release:	%{tl_revision}.1
Summary:	Babel contributed support for Breton
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/babel-breton
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-breton.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-breton.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-breton.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Breton (being, principally, a spoken language) does not have typographic
rules of its own; this package provides an "appropriate" selection of
French and British typographic rules.

