%global tl_name fonts-arundina
%global tl_revision 78421
%global tl_version 0.4.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Arundina is a set of DejaVu-compatible Thai fonts from the Software
Industry Promotion Agency (Public Organization) of Thailand (otherwise
known as SIPA). Serif, sans-serif and monospace type faces are included,
with LaTeX support files.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from fonts-arundina:
Map arundina.map
TL_DROPIN_EOF
