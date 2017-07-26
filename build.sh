#!/bin/sh
# builds Pro/GPL release packages
rpmbuild --define "_topdir $(pwd)/rpmbuild" -bb rpmbuild/SPECS/virtualmin-release.spec
rpmbuild --define "_topdir $(pwd)/rpmbuild" -bb rpmbuild/SPECS/virtualmin-gpl-release.spec

signed=0
while [ $signed -eq 0 ]; do
	rpmsign -D '_gpg_name Virtualmin, Inc. (Package signing key for Virtualmin 6) <security@virtualmin.com>' --addsign rpmbuild/RPMS/noarch/*.rpm
	if [ $? -eq 0 ]; then
		signed=1
	fi
done

cwd=$(pwd)
gplrel=$(find . -name *gpl.noarch.rpm)
echo "Copying $gplrel to GPL repositories..."
cp $gplrel $HOME/result/vm/6/gpl/centos/6/i386
cp $gplrel $HOME/result/vm/6/gpl/centos/6/x86_64
cp $gplrel $HOME/result/vm/6/gpl/centos/7/x86_64
for i in "centos/6/i386 centos/6/x86_64 centos/7/x86_64"; do
	cd $HOME/result/vm/6/gpl/$i
	rm virtualmin-release-latest.noarch.rpm
	ln -s $(basename $gplrel) virtualmin-release-latest.noarch.rpm
done
cd $cwd
rm $gplrel

prorel=$(find . -name *.noarch.rpm)
echo "Copying $prorel to Pro repositories..."
cp $prorel $HOME/result/vm/6/centos/6/i386
cp $prorel $HOME/result/vm/6/centos/6/x86_64
cp $prorel $HOME/result/vm/6/centos/7/x86_64
for i in "centos/6/i386 centos/6/x86_64 centos/7/x86_64"; do
        cd $HOME/result/vm/6/$i
        rm virtualmin-release-latest.noarch.rpm
        ln -s $(basename $prorel) virtualmin-release-latest.noarch.rpm
done
cd $cwd
rm $prorel
