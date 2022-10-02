#!/bin/bash
lagi='Y'
while [ $lagi = 'Y' ] || [ $lagi = 'y' ]
do

echo -n "Masukkan angka yang kamu mau : "
read angka

if test `expr $angka % 2` -eq 0
then
        echo "$angka adalah bilangan genap"
else
        echo "angka adalah bilangan ganjil"
fi
echo -n "Mau coba lagi? (Y/T) : "
read lagi;

done
