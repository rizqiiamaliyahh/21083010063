#!/bin/bash

# Mendeklarasikan fungsi
nama() {
    echo "Siapa namamu?"
    read nama
    npm
}
npm() {
    echo "Sebutkan npm mu"
    read npm
    echo -e "Hai $nama dengan npm $npm, selamat datang \n di sistem operasi yang seru ini ya!"
}

# Memanggil fungsi
nama
