import os
from random import choice

# print(parsekata)
print(' \U0000269D' * 14)
print('|| WELCOME IN TEBAK KATA \U0001F64B ||')
print(' \U0000269D' * 14)
print('\n')

def pilihan():
   print('Kamu akan menebak sebuah suku yang ada di Indonesia!')

suku = ['jawa',
        'sunda',
        'batak',
        'bugis',
        'asmat',
        'ambon',
        'dayak',
        'bali'] 
kata = choice(suku)

pilihan()
pilih = input('Apakah kamu yakin dapat mengerjakannya?')
print('\n')

nyawa = 5
GameOver = False
tebakan = []
hasil = [u' \U00002A02'] * len(kata)

while not GameOver:
  print('Kesempatan : {}'.format(u' \u2665'*nyawa))

  hidden_word = ''.join(hasil)
  print('Tebak kata berikut : {}'.format(hidden_word))
  print('Ketik "exit" untuk berhenti bermain')
  huruf = input('Tebak 1 huruf :').lower()

  if huruf == 'exit':
    print('Thanks for playing, good bye!\n')
    GameOver == True
  elif huruf in kata and huruf not in tebakan:
    print("It's true!\U0001F973\U0001F919\n")
    for i in range(len(kata)):
      if kata[i] == huruf:
        hasil[i] = huruf
  elif huruf in tebakan:
    print('Huruf sudah ditebak sebelumnya, coba lagi.\n')
  else:
    nyawa -= 1
    print('Tebakanmu salah.\U0001F641\U0001F62D\n')

  if huruf not in tebakan:
    tebakan.append(huruf)

  if nyawa == 1:
    print('Ini kesempatan terakhirmu')
  elif nyawa <= 0:
    print('Kesempatanmu telah habis, game over!')
    print('\U0001F44E' * 10)
    print('HA' * 20 + '!')
    GameOver = True
  elif kata == ''.join(hasil):
    print('Kamu berhasil menebak kata : {}'.format(''.join(hasil)))
    GameOver = True
