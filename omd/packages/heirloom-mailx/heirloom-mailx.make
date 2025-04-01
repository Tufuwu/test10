HEIRLOOM_MAILX := heirloom-mailx
HEIRLOOM_MAILX_VERS := 12.5
HEIRLOOM_MAILX_DIR := heirloom-mailx-$(HEIRLOOM_MAILX_VERS)

HEIRLOOM_MAILX_PATCHING := $(BUILD_HELPER_DIR)/$(HEIRLOOM_MAILX_DIR)-patching
HEIRLOOM_MAILX_BUILD := $(BUILD_HELPER_DIR)/$(HEIRLOOM_MAILX_DIR)-build
HEIRLOOM_MAILX_INSTALL := $(BUILD_HELPER_DIR)/$(HEIRLOOM_MAILX_DIR)-install

#HEIRLOOM_MAILX_INSTALL_DIR := $(INTERMEDIATE_INSTALL_BASE)/$(HEIRLOOM_MAILX_DIR)
HEIRLOOM_MAILX_BUILD_DIR := $(PACKAGE_BUILD_DIR)/$(HEIRLOOM_MAILX_DIR)
#HEIRLOOM_MAILX_WORK_DIR := $(PACKAGE_WORK_DIR)/$(HEIRLOOM_MAILX_DIR)

$(HEIRLOOM_MAILX_BUILD): $(HEIRLOOM_MAILX_PATCHING)
	cd $(HEIRLOOM_MAILX_BUILD_DIR) && $(MAKE)
	$(TOUCH) $@

$(HEIRLOOM_MAILX_INSTALL): $(HEIRLOOM_MAILX_BUILD)
	install -m 755 $(HEIRLOOM_MAILX_BUILD_DIR)/mailx $(DESTDIR)$(OMD_ROOT)/bin/heirloom-mailx
	ln -sfn heirloom-mailx $(DESTDIR)$(OMD_ROOT)/bin/mail
	install -m 644 $(HEIRLOOM_MAILX_BUILD_DIR)/mailx.1 $(DESTDIR)$(OMD_ROOT)/share/man/man1/heirloom-mailx.1
	gzip -f $(DESTDIR)$(OMD_ROOT)/share/man/man1/heirloom-mailx.1
	$(TOUCH) $@
