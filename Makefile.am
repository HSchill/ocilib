# Copyright (c) 2007-2016 Vincent ROGIER <vince.rogier@ocilib.net>
#  
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without 
# modifications, as long as this notice is preserved.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

ACLOCAL_AMFLAGS = -I m4
EXTRA_DIST = doc/html reconf configure VERSION acocilib.m4
SUBDIRS = doc/html src demo
DISTCLEANFILES = *~ \#*\#
MAINTAINERCLEANFILES = \
Makefile Makefile.in config.cache config.log config.h.in \
libtool acinclude.m4 aclocal.m4 acocilib.m4 configure stamp-h.in

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = ocilib.pc

rpmroot = $(shell grep %_topdir ~/.rpmmacros |sed 's/\%_topdir[ \t]*//g' |sed 's/\%(echo \(.*\))/\1/g')
SRCS = $(rpmroot)/SOURCES
SPEC = rpm/$(PACKAGE_NAME).spec
release = $(shell git describe --long --dirty --tags |cut -d '-' -f 2)
pkgname = $(PACKAGE_NAME)-$(PACKAGE_VERSION)-$(release)
tarname = $(pkgname).tar.gz

all: config.h
	$(MAKE) $(AM_MAKEFLAGS) all-recursive

$(tarname):
	git archive --format=tar --prefix=$(PACKAGE_NAME)-$(PACKAGE_VERSION)/ v$(PACKAGE_VERSION) | gzip >$@;

tar: $(tarname)

rpm: $(tarname)
	cp $(tarname) $(SRCS)/
	rpmbuild -ba $(SPEC) --define "package_version $(PACKAGE_VERSION)" --define "pack_rel $(release)"

