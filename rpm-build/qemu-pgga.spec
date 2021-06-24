Name:		qemu-pgga
Version:	6.0.0
Release:	0
Summary:	QEMU PGGA

License:	GNU General Public License
URL:		https://github.com/qemu

Requires:	glib2 bzip2 pixman ibaio zlib libxml2 libpmem ibnfs libseccomp libnfsidmap libcurl libcap-ng libzstd libiscsi libudev ncurses device-mapper-multipath librados libradosl brlapi SDL2 glusterfs-apilibpng libjpeg gtk3 librbd cyrus-sasl snappy lzo fuse3l libdrm

%description


%prep
%define _qemu_dir %(echo $PWD)


%install
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/qemu/keymaps
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/qemu/firmware
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/var/run
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/libexec
 
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/locale/bg/LC_MESSAGES
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/locale/de_DE/LC_MESSAGES
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/locale/fr_FR/LC_MESSAGES
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/locale/hu/LC_MESSAGES
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/locale/it/LC_MESSAGES
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/locale/sv/LC_MESSAGES
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/locale/tr/LC_MESSAGES
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/locale/zh_CN/LC_MESSAGES
  
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/16x16/apps
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/24x24/apps
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/32x32/apps
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/48x48/apps
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/64x64/apps
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/128x128/apps
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/256x256/apps
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/512x512/apps
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/32x32/apps
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/scalable/apps
%{__install} -d ${RPM_BUILD_ROOT}/usr/local/share/applications
  
%{__install} %{_qemu_dir}/trace/trace-events-all ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} %{_qemu_dir}/fsdev/virtfs-proxy-helper ${RPM_BUILD_ROOT}/usr/local/libexec
  
%{__install} %{_qemu_dir}/qemu-system-aarch64 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-alpha ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-arm ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-avr ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-cris ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-hppa ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-i386 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-m68k ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-microblazeel ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-microblaze ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-mips64el ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-mips64 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-mipsel ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-mips ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-nios2 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-or1k ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-ppc64 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-ppc ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-riscv32 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-riscv64 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-rx ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-s390x ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-sh4eb ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-sh4 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-sparc64 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-sparc ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-tricore ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-x86_64 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-xtensaeb ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-system-xtensa ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-aarch64_be ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-aarch64 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-alpha ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-armeb ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-arm ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-cris ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-hexagon ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-hppa ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-i386 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-m68k ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-microblazeel ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-microblaze ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-mips64el ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-mips64 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-mipsel ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-mips ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-mipsn32el ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-mipsn32 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-nios2 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-or1k ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-ppc64le ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-ppc64 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-ppc ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-riscv32 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-riscv64 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-s390x ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-sh4eb ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-sh4 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-sparc32plus ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-sparc64 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-sparc ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-x86_64 ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-xtensaeb ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-xtensa ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qga/qemu-ga ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-keymap ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-img ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-io ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-nbd ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/storage-daemon/qemu-storage-daemon ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/contrib/elf2dmp/elf2dmp ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-edid ${RPM_BUILD_ROOT}/usr/local/bin
%{__install} %{_qemu_dir}/qemu-bridge-helper ${RPM_BUILD_ROOT}/usr/local/libexec
%{__install} %{_qemu_dir}/qemu-pr-helper ${RPM_BUILD_ROOT}/usr/local/bin
  
%{__install} %{_qemu_dir}/tools/virtiofsd/virtiofsd ${RPM_BUILD_ROOT}/usr/local/libexec
  
%{__install} %{_qemu_dir}/pc-bios/*.fd ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} %{_qemu_dir}/pc-bios/keymaps/* ${RPM_BUILD_ROOT}/usr/local/share/qemu/keymaps
  
%{__install} /root/qemu/build/po/bg.gmo ${RPM_BUILD_ROOT}/usr/local/share/locale/bg/LC_MESSAGES/qemu.mo
%{__install} /root/qemu/build/po/de_DE.gmo ${RPM_BUILD_ROOT}/usr/local/share/locale/de_DE/LC_MESSAGES/qemu.mo
%{__install} /root/qemu/build/po/fr_FR.gmo ${RPM_BUILD_ROOT}/usr/local/share/locale/fr_FR/LC_MESSAGES/qemu.mo
%{__install} /root/qemu/build/po/hu.gmo ${RPM_BUILD_ROOT}/usr/local/share/locale/hu/LC_MESSAGES/qemu.mo
%{__install} /root/qemu/build/po/it.gmo ${RPM_BUILD_ROOT}/usr/local/share/locale/it/LC_MESSAGES/qemu.mo
%{__install} /root/qemu/build/po/sv.gmo ${RPM_BUILD_ROOT}/usr/local/share/locale/sv/LC_MESSAGES/qemu.mo
%{__install} /root/qemu/build/po/tr.gmo ${RPM_BUILD_ROOT}/usr/local/share/locale/tr/LC_MESSAGES/qemu.mo
%{__install} /root/qemu/build/po/zh_CN.gmo ${RPM_BUILD_ROOT}/usr/local/share/locale/zh_CN/LC_MESSAGES/qemu.mo
  
%{__install} /root/qemu/ui/icons/qemu_16x16.png ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/16x16/apps
%{__install} /root/qemu/ui/icons/qemu_24x24.png ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/24x24/apps
%{__install} /root/qemu/ui/icons/qemu_32x32.png ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/32x32/apps
%{__install} /root/qemu/ui/icons/qemu_48x48.png ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/48x48/apps
%{__install} /root/qemu/ui/icons/qemu_64x64.png ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/64x64/apps
%{__install} /root/qemu/ui/icons/qemu_128x128.png ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/128x128/apps
%{__install} /root/qemu/ui/icons/qemu_256x256.png ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/256x256/apps
%{__install} /root/qemu/ui/icons/qemu_512x512.png ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/512x512/apps
%{__install} /root/qemu/ui/icons/qemu_32x32.bmp ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/32x32/apps
%{__install} /root/qemu/ui/icons/qemu.svg ${RPM_BUILD_ROOT}/usr/local/share/icons/hicolor/scalable/apps
%{__install} /root/qemu/ui/qemu.desktop ${RPM_BUILD_ROOT}/usr/local/share/applications
  
%{__install} /root/qemu/build/tools/virtiofsd/50-qemu-virtiofsd.json ${RPM_BUILD_ROOT}/usr/local/share/qemu/vhost-user
  
%{__install} /root/qemu/pc-bios/bios.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/bios-256k.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/bios-microvm.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/qboot.rom ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/sgabios.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/vgabios.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/vgabios-cirrus.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/vgabios-stdvga.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/vgabios-vmware.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/vgabios-qxl.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/vgabios-virtio.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/vgabios-ramfb.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/vgabios-bochs-display.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/vgabios-ati.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/openbios-sparc32 ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/openbios-sparc64 ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/openbios-ppc ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/QEMU,tcx.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/QEMU,cgthree.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/pxe-e1000.rom ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/pxe-eepro100.rom ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/pxe-ne2k_pci.rom ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/pxe-pcnet.rom ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/pxe-rtl8139.rom ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/pxe-virtio.rom ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/efi-e1000.rom ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/efi-eepro100.rom ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/efi-ne2k_pci.rom ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/efi-pcnet.rom ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/efi-rtl8139.rom ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/efi-virtio.rom ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/efi-e1000e.rom ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/efi-vmxnet3.rom ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/qemu-nsis.bmp ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/bamboo.dtb ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/canyonlands.dtb ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/petalogix-s3adsp1800.dtb ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/petalogix-ml605.dtb ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/multiboot.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/linuxboot.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/linuxboot_dma.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/kvmvapic.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/pvh.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/s390-ccw.img ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/s390-netboot.img ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/slof.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/skiboot.lid ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/palcode-clipper ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/u-boot.e500 ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/u-boot-sam460-20100605.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/qemu_vga.ndrv ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/edk2-licenses.txt ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/hppa-firmware.img ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/opensbi-riscv32-generic-fw_dynamic.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/opensbi-riscv64-generic-fw_dynamic.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/opensbi-riscv32-generic-fw_dynamic.elf ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/opensbi-riscv64-generic-fw_dynamic.elf ${RPM_BUILD_ROOT}/usr/local/share/qemu
%{__install} /root/qemu/pc-bios/npcm7xx_bootrom.bin ${RPM_BUILD_ROOT}/usr/local/share/qemu
  
%{__install} /root/qemu/build/pc-bios/descriptors/50-edk2-i386-secure.json ${RPM_BUILD_ROOT}/usr/local/share/qemu/firmware
%{__install} /root/qemu/build/pc-bios/descriptors/50-edk2-x86_64-secure.json ${RPM_BUILD_ROOT}/usr/local/share/qemu/firmware
%{__install} /root/qemu/build/pc-bios/descriptors/60-edk2-aarch64.json ${RPM_BUILD_ROOT}/usr/local/share/qemu/firmware
%{__install} /root/qemu/build/pc-bios/descriptors/60-edk2-arm.json ${RPM_BUILD_ROOT}/usr/local/share/qemu/firmware
%{__install} /root/qemu/build/pc-bios/descriptors/60-edk2-i386.json ${RPM_BUILD_ROOT}/usr/local/share/qemu/firmware
%{__install} /root/qemu/build/pc-bios/descriptors/60-edk2-x86_64.json ${RPM_BUILD_ROOT}/usr/local/share/qemu/firmware
%{__install} /root/qemu/pc-bios/keymaps/sl ${RPM_BUILD_ROOT}/usr/local/share/qemu/keymaps
%{__install} /root/qemu/pc-bios/keymaps/sv ${RPM_BUILD_ROOT}/usr/local/share/qemu/keymaps


%files
%defattr(-, root, root)
/usr/local/share
/usr/local/bin
/usr/local/libexec
/usr/local/var/run
