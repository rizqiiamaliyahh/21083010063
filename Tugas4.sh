#!/bin/bash

i=1;
echo -n "Masukkan Angka: "
read x
until [ $i -gt $x ];
do
  echo -n $i "
";
let i=$i+2
done
