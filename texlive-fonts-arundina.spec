%global tl_name fonts-arundina
%global tl_revision 78421

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4.0
Release:	%{tl_revision}.1
Summary:	DejaVu-compatible Thai fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/thai/fonts-arundina
License:	other-free lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fonts-arundina.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fonts-arundina.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fonts-arundina.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Arundina is a set of DejaVu-compatible Thai fonts from the Software
Industry Promotion Agency (Public Organization) of Thailand (otherwise
known as SIPA). Serif, sans-serif and monospace type faces are included,
with LaTeX support files.

