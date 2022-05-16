#!/bin/sh
# builds Pro/GPL release packages
rpmbuild --define "_topdir $(pwd)/rpmbuild" -bb rpmbuild/SPECS/virtualmin-pro-release.spec
rpmbuild --define "_topdir $(pwd)/rpmbuild" -bb rpmbuild/SPECS/virtualmin-gpl-release.spec

rpmsign -D '_gpg_name Virtualmin, Inc. (Package signing key for Virtualmin 7) <security@virtualmin.com>' --addsign rpmbuild/RPMS/noarch/*.rpm

cwd=$(pwd)
echo "Copying to repository..."
# GPL
gplrel=$(find . -name 'virtualmin-gpl-release*.noarch.rpm')
cp "$gplrel" "$HOME/result/vm/7/rpm/"
echo "Adding links..."
cd "$HOME/result/vm/7/rpm/" || exit 1
rm virtualmin-gpl-release.noarch.rpm
gplpackage=$(basename "$gplrel")
ln -s "$gplpackage" virtualmin-gpl-release.noarch.rpm
cd "$cwd" || exit 1
rm "$gplrel"

# Pro
prorel=$(find . -name 'virtualmin-pro-release*.noarch.rpm')
cp "$prorel" "$HOME/result/vm/7/rpm/"
echo "Adding links..."
cd "$HOME/result/vm/7/rpm/" || exit 1
rm virtualmin-pro-release.noarch.rpm
propackage=$(basename "$prorel")
ln -s "$propackage" virtualmin-pro-release.noarch.rpm
cd "$cwd" || exit 1 
rm "$prorel"

