# virtualmin-release
Repository configuration file for CentOS, RHEL, and Fedora systems

Run ./build.sh in the base of the directory, and it'll use rpmbuild to build two virtualmin-release files.

If you're not running it on our build system, you'll need to edit build.sh to use a different key to sign to packages. (But, this repo is probably only useful for those of us who build/maintain the Virtualmin installer and repositories.)
