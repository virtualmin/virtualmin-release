#!/bin/sh
# builds Pro/GPL release packages
rpmbuild --define "_topdir $(pwd)/rpmbuild" -bb rpmbuild/SPECS/virtualmin-release.spec
rpmbuild --define "_topdir $(pwd)/rpmbuild" -bb rpmbuild/SPECS/virtualmin-gpl-release.spec

rpmsign -D '_gpg_name Virtualmin, Inc. (Package signing key for Virtualmin 6) <security@virtualmin.com>' --addsign rpmbuild/RPMS/noarch/*.rpm

