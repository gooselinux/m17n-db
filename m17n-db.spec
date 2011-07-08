Name:       m17n-db
Summary:    Multilingualization datafiles for m17n-lib
Version:    1.5.5
Release:    1.1%{?dist}
Group:      System Environment/Libraries
License:    LGPLv2+
URL:        http://www.m17n.org/m17n-lib/index.html
Source0:    http://www.m17n.org/m17n-lib-download/%{name}-%{version}.tar.gz
BuildArch:  noarch
Buildroot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gettext
Patch1:     number_pad_itrans-222634.patch
Patch2:     si-wijesekera-keymap-rename_key-summary.patch
Patch4:     bn-itrans-t-182227.patch
Patch5:     kn-itrans-ZWNJ-221965.patch
Patch6:     kn-itrans_key-summary_228806.patch
Patch7:     ml-itrans-keysummary-435260.patch

%description
This package contains multilingualization (m17n) datafiles for m17n-lib
which describe input maps, encoding maps, and OpenType font data
for many languages.


%package datafiles
Summary:  Multilingualization datafiles for m17n-lib
Group:    System Environment/Libraries
Requires: %{name} = %{version}-%{release} 

%description datafiles
m17n-db datafiles not needed for using the input maps.


%package devel
Summary:  Development files for m17n-db
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
m17n-db development files


%package common-cjk
Summary:  Common m17n-db files for CJK input
Group:    System Environment/Libraries
Requires: %{name} = %{version}-%{release} 

%description common-cjk
m17n-db common files for Chinese, Japanese and Korean input maps.


%package chinese
Summary:  Chinese m17n-db input maps
Group:    System Environment/Libraries
Requires: %{name}-common-cjk
Obsoletes: %{name}-bopomofo < 1.3.3-13.fc6
Obsoletes: ibus-m17n-chinese < 0.1.1.20081013-3

%description chinese
m17n-db Chinese input map.


%package generic
Summary:  Generic m17n-db input maps
Group:    System Environment/Libraries
Requires: %{name} = %{version}-%{release} 

%description generic
This package contains generic m17n-db input maps.


%package greek
Summary:  Greek m17n-db input maps
Group:    System Environment/Libraries
Requires: %{name} = %{version}-%{release} 
Obsoletes: ibus-m17n-greek < 0.1.1.20081013-3

%description greek
m17n-db Greek input table.


%package gregorian
Summary:  Gregorian m17n-db input maps
Group:    System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: m17n-db-georgian <= 1.4.0
Obsoletes: ibus-m17n-gregorian < 0.1.1.20081013-3

%description gregorian
m17n-db Gregorian input table.

%package uyghur
Summary:  Uyghur m17n-db input maps
Group:    System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: m17n-db-Uyghur <= 1.4.0
Obsoletes: ibus-m17n-uyghur < 0.1.1.20081013-3

%description uyghur
m17n-db uyghur input table.

%define mk_pkg() \
%package %1\
Summary:    m17n-db input maps for %(echo %1 | sed -e "s/\\(.*\\)/\\u\\1/")\
Group:      System Environment/Libraries\
Requires:   %{name} = %{version}-%{release}\
Obsoletes:  ibus-m17n-%1 < 0.1.1.20081013-3\
\
%description %1\
This package contains m17n-db input maps for %(echo %1 | sed -e "s/\\(.*\\)/\\u\\1/").\
\
%files %1\
%defattr(-,root,root)\
%{_datadir}/m17n/%2-*.mim\
%if %3\
%{_datadir}/m17n/icons/%2-*.png\
%else\
%{nil}\
%endif\

%define mk_pkg_uses_contrib() \
%package %1\
Summary:    m17n-db input maps for %(echo %1 | sed -e "s/\\(.*\\)/\\u\\1/")\
Group:      System Environment/Libraries\
Requires:   %{name} = %{version}-%{release} \
Requires:   m17n-contrib-%1 >= 1.1.3 \
Obsoletes:  ibus-m17n-%1 < 0.1.1.20081013-3\
\
%description %1\
This package contains m17n-db input maps for %(echo %1 | sed -e "s/\\(.*\\)/\\u\\1/").\
\
%files %1\
%defattr(-,root,root)\
%{_datadir}/m17n/%2-*.mim\
%if %3\
%{_datadir}/m17n/icons/%2-*.png\
%else\
%{nil}\
%endif\

%mk_pkg amharic am 1
%mk_pkg arabic ar 1
%mk_pkg armenian hy 1
%mk_pkg_uses_contrib assamese as 1
%mk_pkg_uses_contrib bengali bn 1
%mk_pkg cham cmc 1
%mk_pkg croatian hr 1
%mk_pkg danish da 0
%mk_pkg dhivehi dv 1
%mk_pkg farsi fa 1
%mk_pkg french fr 0
%mk_pkg_uses_contrib gujarati gu 1
%mk_pkg hebrew he 1
%mk_pkg_uses_contrib hindi hi 1
%mk_pkg japanese ja 1
%mk_pkg_uses_contrib kannada kn 1
%mk_pkg kazakh kk 1 
%mk_pkg khmer km 1 
%mk_pkg korean ko 1
%mk_pkg lao lo 1
%mk_pkg latin latn 1
%mk_pkg_uses_contrib malayalam ml 1
%mk_pkg myanmar my 1
%mk_pkg_uses_contrib oriya or 1
%mk_pkg_uses_contrib punjabi pa 1
%mk_pkg_uses_contrib russian ru 1
%mk_pkg sanskrit sa 0
%mk_pkg serbian sr 1
%mk_pkg_uses_contrib sinhala si 1
%mk_pkg slovak sk 1
%mk_pkg swedish sv 1
%mk_pkg syriac syrc 1
%mk_pkg_uses_contrib tamil ta 1
%mk_pkg_uses_contrib telugu te 1
%mk_pkg thai th 1
%mk_pkg tibetan bo 1
%mk_pkg_uses_contrib vietnamese vi 1


%prep
%setup -q 
pushd MIM
%patch1 -p1 -b .1
%patch2 -p0 -b .2
%patch4 -p1 -b .4
%patch5 -p0 -b .5
%patch6 -p0 -b .6
%patch7 -p0 -b .7
popd

%build
%configure
make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# don't need ispell or anthy
rm $RPM_BUILD_ROOT%{_datadir}/m17n/{ispell.mim,icons/en-ispell.png}
rm $RPM_BUILD_ROOT%{_datadir}/m17n/{ja-anthy.mim,icons/ja-anthy.png}
# don't ship unijoy map for now
rm $RPM_BUILD_ROOT%{_datadir}/m17n/{bn-unijoy.mim,icons/bn-unijoy.png}

# dont install si-wijesekera.mim as si-wijesekera-predit.mim works for us, see RH bug 208104
rm $RPM_BUILD_ROOT%{_datadir}/m17n/si-wijesekera.mim

# For installing the translation files
%find_lang %name


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%dir %{_datadir}/m17n
%dir %{_datadir}/m17n/icons
%{_datadir}/m17n/mdb.dir
%{_datadir}/m17n/*.tbl
%{_datadir}/m17n/global.mim


# include translations
%files datafiles -f %{name}.lang
%defattr(-,root,root)
%{_datadir}/m17n/*.flt
%{_datadir}/m17n/*.fst
%{_datadir}/m17n/*.map
%{_datadir}/m17n/*.tab
%{_datadir}/m17n/*.lnm
%{_datadir}/m17n/LOCALE.*

%files devel
%defattr(-,root,root)
%{_bindir}/m17n-db
%{_datadir}/pkgconfig/m17n-db.pc

%files common-cjk
%defattr(-,root,root)
%{_datadir}/m17n/cjk-*.mim

%files chinese
%defattr(-,root,root)
%{_datadir}/m17n/zh-*.mim
%{_datadir}/m17n/icons/zh-*.png
%{_datadir}/m17n/icons/bopo-*.png

%files generic
%defattr(-,root,root)
%{_datadir}/m17n/rfc1345.mim
%{_datadir}/m17n/icons/rfc1345.png
%{_datadir}/m17n/unicode.mim
%{_datadir}/m17n/icons/unicode.png

%files greek
%defattr(-,root,root)
%{_datadir}/m17n/el-*.mim
%{_datadir}/m17n/grc-*.mim
%{_datadir}/m17n/icons/el-*.png

%files gregorian
%defattr(-,root,root)
%{_datadir}/m17n/ka*.mim
%{_datadir}/m17n/icons/ka*.png

%files uyghur
%defattr(-,root,root)
%dir %{_datadir}/m17n
%{_datadir}/m17n/ug-*.mim

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.5.5-1.1
- Rebuilt for RHEL 6

* Wed Jul 29 2009 Parag Nemade <pnemade@redhat.com> -1.5.5-1
- update to new upstream release 1.5.5

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 08 2009 Parag Nemade <pnemade@redhat.com> -1.5.4-2
- Resolves: rh#494810-[indic][m17n-db][m17n-contrib] ibus .engine files no longer needed for new ibus

* Tue Mar 03 2009 Parag Nemade <pnemade@redhat.com> -1.5.4-1
- Update to new upstream release 1.5.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 21 2008 Parag Nemade <pnemade@redhat.com> -1.5.3-1.fc10
- Update to new upstream release 1.5.3

* Mon Oct 20 2008 Jens Petersen <petersen@redhat.com> - 1.5.2-4.fc10
- add obsoletes for ibus-m17n subpackages
- fix m17n-gen-ibus-engine to check for lang 't'

* Wed Oct 15 2008 Jens Petersen <petersen@redhat.com> - 1.5.2-3.fc10
- create .engine files for ibus-m17n with m17n-gen-ibus-engine (#466410)

* Fri Aug 29 2008 Parag Nemade <pnemade@redhat.com> -1.5.2-2
- Recreated patch si-wijesekera-keymap-rename_key-summary.patch

* Thu Jul 03 2008 Parag Nemade <pnemade@redhat.com> -1.5.2-1
- Update to new upstream release 1.5.2

* Fri Apr 04 2008 Parag Nemade <pnemade@redhat.com> -1.5.1-3.fc9
- Resolves:rh#440567

* Wed Apr 02 2008 Parag Nemade <pnemade@redhat.com> -1.5.1-2.fc9
- Resolves:rh#435260

* Thu Feb 07 2008 Parag Nemade <pnemade@redhat.com> -1.5.1-1.fc9
- Update to new upstream release 1.5.1
- Added BR: gettext

* Fri Dec 28 2007 Parag Nemade <pnemade@redhat.com> -1.5.0-1.fc9
- Update to new upstream release 1.5.0

* Fri Sep 07 2007 Parag Nemade <pnemade@redhat.com> - 1.4.0-6.fc8
- Removed incorrect version of hi-typewriter.mim

* Mon Aug 20 2007 Parag Nemade <pnemade@redhat.com> - 1.4.0-5.fc8
- Added Obsoletes to m17n-db-gregorian
- Added Obsoletes to m17n-db-uyghur
- Added Provides to m17n-db-gregorian, m17n-db-gregorian, m17n-db-chinese

* Mon Aug 13 2007 Parag Nemade <pnemade@redhat.com> 
- update License tag

* Wed Jul 25 2007 Parag Nemade <pnemade@redhat.com> - 1.4.0-4
- Added m17n-db as Requires for mk_pkg() macro generating packages.
- Added m17b-db and m17n-contrib-lang as Requires 
  for mk_pkg_uses_contrib() macro generating packages.

* Wed Jul 25 2007 Jens Petersen <petersen@redhat.com> - 1.4.0-3
- cleanup summaries and descriptions
- make just main package own m17n and icons dir
- replace %%makeinstall with make install

* Tue Jul 24 2007 Parag Nemade <pnemade@redhat.com> - 1.4.0-2.1
- Fix directory ownership issue

* Mon Jul 23 2007 Parag Nemade <pnemade@redhat.com> - 1.4.0-2
- SPEC clean up. Remove m17n-contrib

* Thu Jul 19 2007 Parag Nemade <pnemade@redhat.com> - 1.4.0-1
- Updated to new upstream release 1.4.0

* Wed Jul 18 2007 Jens Petersen <petersen@redhat.com>
- install .pc file under %%{_datadir}/pkgconfig
  and include it in a new devel subpackage

* Mon Jun 18 2007 Jens Petersen <petersen@redhat.com> - 1.3.4-10
- name Uyghur subpackage consistently

* Wed May 16 2007 Jens Petersen <petersen@redhat.com> - 1.3.4-9
- update ta-typewriter.mim with bug fixes (I Felix, #236169)

* Thu Mar 15 2007 Mayank Jain <majain@redhat.com> 1.3.4-8
- Added key summary to kn-itrans,inscript keymaps - resolves 228806

* Thu Feb 15 2007 Mayank Jain <majain@redhat.com>
- Added ZWNJ (U+200d) needed in kn-* keymaps, resolved - 221965
- Added kn-itrans-ZWNJ-221965.patch

* Thu Feb 15 2007 Mayank Jain <majain@redhat.com>
- Added itrans layout for Marahi, resolved - 225561

* Thu Feb 8 2007 Mayank Jain <majain@redhat.com>
- Added phonetic keymaps for Marathi & Oriya, resolved - 225559 and 225562

* Tue Jan 17 2007 Mayank Jain <majain@redhat.com>
- Added Patch 4 as number_pad_itrans-222634.patch for adding number pad support in itrans keymaps
- Added number pad support in all indic keymaps except tamil as they used english numerals.
- Resolves bug : 222634

* Tue Jan 16 2007 Mayank Jain <majain@redhat.com>
- Added Patch 3 as sk-kbd-222804.patch to fix bug 222804

* Tue Jan 11 2007 Mayank Jain <majain@redhat.com>
- Moved all translations to m17n-db-datafiles package

* Tue Jan 8 2007 Mayank Jain <majain@redhat.com>
- Resolves: Bug 221794 - Rebased to new release m17n-db-1.3.4
- Removed patch: si-wijesekera_surrounding_to_preedit.patch
- Added directive to delete si-wijesekera from the upstream tarball as it used surrounding text
- Commented directive to copy bopo-kbd.mim
- Commented directive using variable.mim and command.mim - added global.mim in place of them
- Added sections for new Uyghur.
- Added copy directive for Mizuochi (grc-*) keymap for classical greek
- Added directives to install translations for japanese translations.
- Added patch to rename si-wijesekera-preedit to si-wijesekera and add key summary as Patch2

* Tue Jan 2 2007 Mayank Jain <majain@redhat.com>
- Resolves: Bug 221122: [hi_IN-remington] vowels in hi-remington are not typed correctly

* Thu Dec 7 2006 Mayank Jain <majain@redhat.com>
- Resolves: bug 218255 - Fixed ta-typewriter keymap.

* Tue Dec 1 2006 Mayank Jain <majain@redhat.com>
- Fixed typo in si-wijesekera key summary (in the patch)

* Tue Nov 28 2006 Mayank Jain <majain@redhat.com>
- Reverted back to upstream's tarball for m17n-db
- Added si-wijesekera-with-preedit as a patch to m17n-db tarball
- Updated license header in hi-remington, as-inscript, or-inscript, ta-typewriter
- Resolved - 217318, 217319

* Mon Nov 27 2006 Mayank Jain <majain@redhat.com>
- Added halant to (t) in bn-itrans.mim in m17n-indic tarball, resolves bug 217139
- Edited our own bn-itrans-t-182227.patch to resolve bug 217139

* Mon Nov 20 2006 Mayank Jain <majain@redhat.com>
- Retained mapping of (.) to (.) in as-inscript as per bug 215486
- Fixed an error in ta-tamil99 key summary.

* Mon Nov 14 2006 Mayank Jain <majain@redhat.com>
- Fixed Bug 177371: mapping of X and x in kn-kgp
- Fixed Bug 215486: Mapped 0x0964 to shift(.) instead of . in as-inscript
- Fixed Bug 215489: Mapped 0x0964 to shift(.) instead of . in bn-inscript

* Mon Nov 13 2006 Mayank Jain <majain@redhat.com>
- Added ZWNJ to ml-inscript, fixes 214971

* Mon Nov 9 2006 Mayank Jain <majain@redhat.com>
- Fixed an errounous fix of ZWNJ to hi-inscript/phonetic

* Mon Nov 6 2006 Mayank Jain <majain@redhat.com>
- Fixed Bug 213633: Need changes in Assamese Inscript layout

* Mon Nov 2 2006 Mayank Jain <majain@redhat.com>
- Added ZWNJ to hi-inscript/phonetic

* Mon Nov 1 2006 Mayank Jain <majain@redhat.com>
- Added 09CE mapped to z in as-inscript (213372)

* Mon Nov 1 2006 Mayank Jain <majain@redhat.com>
- Imported m17n-db-indic-0.4.29.tar.gz from RHEL-5 package, changes happened from .28 version are 
- Added few more key combinations for ta-typewriter keymap - bug 209088
- Added ZWJ for hi-inscript and hi-phonetic keymaps - bug 211576
- Corrected kn-kgp and kn-inscript keymaps for keymapping of X - bug 209963

* Mon Oct 17 2006 Mayank Jain <majain@redhat.com>
- Added si-wijesekera keymap with preedit, replaces si-wijesekera with surrounding text support
- Fixed kn-kgp keymap

* Mon Oct 16 2006 Mayank Jain <majain@redhat.com>
- Cleaned the spec file, versioning errors & removed use of epoch from the spec file
- Added ta-typewriter keymap & icon, fixes bug 209088

* Mon Oct 16 2006 Mayank Jain <majain@redhat.com>
- Switched the version number for m17n-db back to 1.3.3
- Added "Epoch : 1" in the spec file to override the 1.3.4 build.

* Mon Oct 9 2006 Mayank Jain <majain@redhat.com>
- Added key summary for si-wijesekera keymap

* Wed Oct 4 2006 Mayank Jain <majain@redhat.com>
- Removed errernous entries from ta-tamil99 keymap

* Tue Sep 12 2006 Mayank Jain <majain@redhat.com>
- Added key summary to te-inscript keymap

* Thu Sep 7 2006 Mayank Jain <majain@redhat.com>
- Updated keymaps for typo errors, updated copyright header in all keymaps with "This file is part of the m17n contrib; a sub-part of the m17n library"
- Added key summary for ta-tamil99 keymap
- updated key summary for bn-itrans.mim

* Wed Sep 6 2006 Mayank Jain <majain@redhat.com>
- Updated or-inscript.mim for bug 204726

* Wed Sep 6 2006 Mayank Jain <majain@redhat.com>
- Updated bn-probhat & as-phonetic keymaps with *=>ৎ
- Corrected date type in changelog

* Tue Sep 5 2006 Mayank Jain <majain@redhat.com>
- Updated as-phonetic with key summary

* Mon Sep 4 2006 Mayank Jain <majain@redhat.com>
- Added key summaries to pa-inscript/jhelum
- Fixed 204755

* Tue Aug 31 2006 Mayank Jain <majain@redhat.com>
- Added ur-phonetic icon
- Updated spec file to incorporate the icon

* Tue Aug 31 2006 Mayank Jain <majain@redhat.com>
- Updated bn-{inscript,probhat,itrans} for RH bug #204275
- Added ur-phonetic.mim file for RH bug #177372
- Updated m17n-db.spec file to incorporate Urdu keymap.

* Tue Aug 8 2006 Mayank Jain <majain@redhat.com>
- Updated bn-probhat.mim for RH bz #200890 ...weird... that previous update didnt showed up!
- https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=200890#c4

* Tue Aug 1 2006 Mayank Jain <majain@redhat.com>
- Corrected bn-probhat.mim file, RH bz #200890, added U+09CE

* Tue Aug 1 2006 Mayank Jain <majain@redhat.com>
- Corrected ml-inscript.mim file, RH bz #200876

* Tue Jul 25 2006 Jens Petersen <petersen@redhat.com> - 1.3.3-14
- move bopomofo to chinese subpackage

* Mon Jul 17 2006 Mayank Jain <majain@redhat.com> - 1.3.3-13
- Removed ta-typewriter.mim keymap as its not working
- Added ml-inscript.png
- Added hi-inscript.png
- added hi-remington.png

* Thu Jul 13 2006 Mayank Jain <majain@redhat.com>
- Added ta-typewriter.mim keymap

* Thu Jul 6 2006 Mayank Jain <majain@redhat.com>
- Added key summaries in various keymaps

* Thu Jun 29 2006 Mayank Jain <majain@redhat.com>
- Added hi-remington keymap - <rranjan@redhat.com>
- Added hi-remington.png - <aalam@redhat.com>

* Thu Jun 8 2006 Mayank Jain <majain@redhat.com>
- Added hi-typewriter keymap.

* Wed Jun 7 2006 Mayank Jain <majain@redhat.com>
- Added or-*.png icons.

* Mon Jun 5 2006 Mayank Jain <majain@redhat.com>
- Added as-*.png icons.

* Fri Jun 2 2006 Mayank Jain <majain@redhat.com>
- Added or-inscript keymap to the tarball
- Commented out as-*.png and or-*.png from the directives as respective .png files are missing from tarball.

* Fri Jun 2 2006 Mayank Jain <majain@redhat.com>
- Added modified as-phonetic.mim keymap, modified by <runab@redhat.com> for RH bz #193849

* Mon May 29 2006 Mayank Jain <majain@redhat.com>
- Added icon for marathi inscript - thanks to <aalam@redhat.com>

* Wed May 17 2006 Mayank Jain <majain@redhat.com>
- Added following keymaps
  - as-inscript.mim
  - as-phonetic.mim
  - mr-inscript.mim
  - ta-tamil99.mim

* Wed Mar 22 2006 Jens Petersen <petersen@redhat.com>
- fix language names in Indic .mim file headers (Naoto Takahashi)
- add make-dist script to m17n-db-indic

* Thu Mar  9 2006 Jens Petersen <petersen@redhat.com> - 1.3.3-2
- Bengali input maps fixes (runab)
  - map Probhat '*' key to an alternate sequence since glyph missing (#179821)
  - more itrans cleanup (#182227)
- add icon for Tamil99 (aalam)

* Thu Mar  2 2006 Jens Petersen <petersen@redhat.com> - 1.3.3-1
- update to 1.3.3 bugfix release
- fixes to Bengali, Hindi, and Punjabi maps (runab, aalam)
- Tamil phonetic map now works
- new Tamil99 Government Standard map (I Felix)

* Tue Feb 14 2006 Jens Petersen <petersen@redhat.com> - 1.3.2-2
- add Indian input maps ported from scim-tables
- add Nepali subpackage

* Fri Feb 10 2006 Jens Petersen <petersen@redhat.com> - 1.3.2-1
- update to 1.3.2 bugfix release
- do not include ja-anthy.mim input map

* Thu Feb  2 2006 Jens Petersen <petersen@redhat.com> - 1.3.1-1
- update to 1.3.1 release
  - add new icons to language subpackages
  - new common-cjk subpackage for CJK common files
  - new Swedish subpackage
  - exclude new pkgconfig file

* Fri Dec 16 2005 Jens Petersen <petersen@redhat.com> - 1.2.0-2
- import to Fedora Core

* Wed Nov  9 2005 Jens Petersen <petersen@redhat.com> - 1.2.0-1
- separate output datafiles to datafiles subpackage.

* Wed Oct  5 2005 Jens Petersen <petersen@redhat.com>
- initial packaging for Fedora Extras

* Sat Sep 24 2005 Jens Petersen <petersen@redhat.com>
- split .mim input tables into separate subpackages per language

* Sat Jan 15 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp>
- modify spec for fedora
