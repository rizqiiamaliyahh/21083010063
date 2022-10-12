#!/bin/bash

#deklarasi array indirect declaration
distroLinuxDekstop[0]=BlankOn
distroLinuxDekstop[1]=Ubuntu
distroLinuxDekstop[2]=Debian
distroLinuxDekstop[3]=ArchLinux
distroLinuxDekstop[4]=LinuxMint

distroLinuxServer[1]=UbuntuServer
distroLinuxServer[2]=CentOS
distroLinuxServer[3]=FedoraServer

#cara mengambil nilai array
echo ${distroLinuxDekstop[*]}
echo ${distroLinuxServer[*]}
