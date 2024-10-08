# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device ginkgo
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Redmi Note 8
%define rpm_device ginkgo
%define installable_zip 1

%define droid_target_aarch64 1

# Entries migrated from the old rpm/droid-hal-hammerhead.spec
%define enable_kernel_update 1

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

# want adreno quirks is required for browser at least, and other subtle issues
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
#define QCOM_BSP 1 \
%{nil}

%define straggler_files \
  /acct \
  /bugreports \
  /bt_firmware \
  /cache \
  /charger \
  /d \
  /dsp \
  /firmware \
  /odm \
  /oem \
  /persist \
  /product \
  /sdcard \
  /storage \
%{nil}


# On Android 8 the system partition is (intended to be) mounted on /.
%define makefstab_skip_entries / /system /vendor /dev/stune /dev/cpuset /sys/fs/pstore /dev/cpuctl

%include rpm/dhd/droid-hal-device.inc
