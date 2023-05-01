%bcond_without check

# https://github.com/coyim/gotk3extra
%global goipath         github.com/coyim/gotk3extra
Version:                0.0.2

%gometa

%global common_description %{expand:
Contains additional functionality to gotk3}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        0.1%{?dist}
Summary:        Contains adapters additional functionality to gotk3

License:        GPL-3.0-only
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gotk3/gotk3/gdk)
BuildRequires:  golang(github.com/gotk3/gotk3/glib)
BuildRequires:  golang(github.com/gotk3/gotk3/gtk)
BuildRequires:  golang(github.com/gotk3/gotk3/pango)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
Xvfb :99 &
export DISPLAY=:99
export GOFLAGS="-tags=gtk_3_18,glib_2_66"
%gocheck
%endif

%gopkgfiles

%changelog
* Sun Apr 30 11:00:00 -05 2023 CAD <fedora@autonomia.digital> - 0.0.2-1
- Initial package
