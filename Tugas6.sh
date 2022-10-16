#!/bin/bash

echo "Banyaknya nilai IPS yang akan dimasukkan:"
read jumlah_data_IPS

jumlah=0;
ipk_mhs=0;

for ((i=1; i<=jumlah_data_IPS; i++))
do
        echo "Nilai ke $i: "
        read tulis[$i]
        let jumlah=$jumlah+${tulis[i]};
        let ipk_mhs=$jumlah/$jumlah_data_IPS;
done

echo "IPS mhs: " $jumlah/$jumlah_data_IPS
echo "IPK mhs: " $ipk_mhs
