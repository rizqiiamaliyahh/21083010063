#!/bin/bash

#deklarasi array compund assignment
distroLinuxDekstop=('BlankOn' 'Ubuntu' 'Debian' 'ArchLinux' 'LinuxMint')
distroLinuxServer=('UbuntuServer' 'CentOS' 'FedoraServer')

#cara mengambil nilai array
echo ${distroLinuxDekstop[*]}
echo ${distroLinuxServer[*]}
