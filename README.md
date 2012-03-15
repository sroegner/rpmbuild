# rpmbuild

Just a collection of random spec files intended for people who know what to do with them. They are usually tested on Centos 5.x and Fedora (both x86_64 only). I try to maintain a level of conformity with Red Hat/Fedora packaging standards using rpmlint but I rarely come out without any warnings.

## Building nodejs RPMs for Fedora/RedHat/CentOS/OEL

* download the source tarball from http://nodejs.org/dist
* make sure your machine has rpmbuild installed (yum install rpm-build)
* run rpmbuild like so:

  NODEJS_VERSION=0.6.10 rpmbuild -ba --clean --define "packager Your Name <your.name@example.com>" --define "_topdir ${PWD}/rpmbuild" rpmbuild/SPECS/nodejs.spec

You can add a dist attribute like this:

  NODEJS_VERSION=0.6.10 rpmbuild -ba --clean --define "dist .myorg.f16" --define "packager Your Name <your.name@example.com>" --define "_topdir ${PWD}/rpmbuild" rpmbuild/SPECS/nodejs.spec

Free for re-use.
