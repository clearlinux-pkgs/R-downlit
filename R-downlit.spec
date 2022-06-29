#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-downlit
Version  : 0.4.1
Release  : 25
URL      : https://cran.r-project.org/src/contrib/downlit_0.4.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/downlit_0.4.1.tar.gz
Summary  : Syntax Highlighting and Automatic Linking
Group    : Development/Tools
License  : MIT
Requires: R-brio
Requires: R-desc
Requires: R-digest
Requires: R-evaluate
Requires: R-fansi
Requires: R-memoise
Requires: R-rlang
Requires: R-vctrs
Requires: R-withr
Requires: R-yaml
BuildRequires : R-brio
BuildRequires : R-desc
BuildRequires : R-digest
BuildRequires : R-evaluate
BuildRequires : R-fansi
BuildRequires : R-memoise
BuildRequires : R-rlang
BuildRequires : R-vctrs
BuildRequires : R-withr
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
needs of 'RMarkdown' packages like 'pkgdown', 'hugodown', and
    'bookdown'. It includes linking of function calls to their
    documentation on the web, and automatic translation of ANSI escapes in
    output to the equivalent HTML.

%prep
%setup -q -c -n downlit
cd %{_builddir}/downlit

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656099480

%install
export SOURCE_DATE_EPOCH=1656099480
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library downlit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library downlit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library downlit
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc downlit || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/downlit/DESCRIPTION
/usr/lib64/R/library/downlit/INDEX
/usr/lib64/R/library/downlit/LICENSE
/usr/lib64/R/library/downlit/Meta/Rd.rds
/usr/lib64/R/library/downlit/Meta/features.rds
/usr/lib64/R/library/downlit/Meta/hsearch.rds
/usr/lib64/R/library/downlit/Meta/links.rds
/usr/lib64/R/library/downlit/Meta/nsInfo.rds
/usr/lib64/R/library/downlit/Meta/package.rds
/usr/lib64/R/library/downlit/NAMESPACE
/usr/lib64/R/library/downlit/NEWS.md
/usr/lib64/R/library/downlit/R/downlit
/usr/lib64/R/library/downlit/R/downlit.rdb
/usr/lib64/R/library/downlit/R/downlit.rdx
/usr/lib64/R/library/downlit/WORDLIST
/usr/lib64/R/library/downlit/help/AnIndex
/usr/lib64/R/library/downlit/help/aliases.rds
/usr/lib64/R/library/downlit/help/downlit.rdb
/usr/lib64/R/library/downlit/help/downlit.rdx
/usr/lib64/R/library/downlit/help/paths.rds
/usr/lib64/R/library/downlit/html/00Index.html
/usr/lib64/R/library/downlit/html/R.css
/usr/lib64/R/library/downlit/tests/testthat.R
/usr/lib64/R/library/downlit/tests/testthat/_snaps/downlit-html.md
/usr/lib64/R/library/downlit/tests/testthat/_snaps/evaluate.md
/usr/lib64/R/library/downlit/tests/testthat/_snaps/highlight.md
/usr/lib64/R/library/downlit/tests/testthat/autolink.html
/usr/lib64/R/library/downlit/tests/testthat/fake-repo/src/contrib/PACKAGES
/usr/lib64/R/library/downlit/tests/testthat/index/DESCRIPTION
/usr/lib64/R/library/downlit/tests/testthat/index/LICENSE
/usr/lib64/R/library/downlit/tests/testthat/index/LICENSE.md
/usr/lib64/R/library/downlit/tests/testthat/index/NAMESPACE
/usr/lib64/R/library/downlit/tests/testthat/index/R/basic.R
/usr/lib64/R/library/downlit/tests/testthat/index/index.Rproj
/usr/lib64/R/library/downlit/tests/testthat/index/man/a.Rd
/usr/lib64/R/library/downlit/tests/testthat/index/man/b.Rd
/usr/lib64/R/library/downlit/tests/testthat/index/vignettes/test-1.Rmd
/usr/lib64/R/library/downlit/tests/testthat/index/vignettes/test-2.Rmd
/usr/lib64/R/library/downlit/tests/testthat/markdown-definition.md
/usr/lib64/R/library/downlit/tests/testthat/markdown-table.md
/usr/lib64/R/library/downlit/tests/testthat/test-article-index.R
/usr/lib64/R/library/downlit/tests/testthat/test-downlit-html.R
/usr/lib64/R/library/downlit/tests/testthat/test-downlit-html.txt
/usr/lib64/R/library/downlit/tests/testthat/test-downlit-md-v20.txt
/usr/lib64/R/library/downlit/tests/testthat/test-downlit-md-v21.txt
/usr/lib64/R/library/downlit/tests/testthat/test-downlit-md.R
/usr/lib64/R/library/downlit/tests/testthat/test-downlit-md.txt
/usr/lib64/R/library/downlit/tests/testthat/test-evaluate.R
/usr/lib64/R/library/downlit/tests/testthat/test-highlight.R
/usr/lib64/R/library/downlit/tests/testthat/test-highlight.txt
/usr/lib64/R/library/downlit/tests/testthat/test-link.R
/usr/lib64/R/library/downlit/tests/testthat/test-metadata.R
/usr/lib64/R/library/downlit/tests/testthat/test-packages.R
/usr/lib64/R/library/downlit/tests/testthat/test-topic-index.R
/usr/lib64/R/library/downlit/tests/testthat/test-utils.R
