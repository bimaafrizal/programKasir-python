# -*- coding: utf-8 -*-
"""programKasirKemuning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x3AledLnT-E3OfEtBJzDLEJeRWhzx3wW
"""

import pandas as pd

menu = ['Sate Kelinci', 'Sop Buntut Iga', 'Sego Tumpang', 'Soto Ayam', 'Tempe Mendoan', 'Molen Tawangmangu', 'Tahu Petis', 'ES Teh', 'Es Jeruk', 'Kopi']
harga = [15000, 25000, 10000, 7000, 5000, 5000, 5000, 2000, 3000, 5000]
listPesanan = []
totalHarga = []
jumlahPesanan = []

statusExit = True
while(statusExit):
  print("=" * 10 + "Program Kasir Kelompok Dua" + "=" * 15)
  print("")
  print("Pilih mode:")
  print("1.Tambah Data\n2.Transaksi\n3.Nota\n4.Exit\n")
  pilihan = int(input("Masukan pilhan anda: "))
  print("")

  if(pilihan == 1):
    #masukan baru menu
    menuTambah = input("Masukan menu baru! ")
    hargaTambah = int(input("Masukan harganya! "))
    menu.append(menuTambah)
    harga.append(hargaTambah)
    
  if(pilihan == 2):
    #merubah index mulai dari 1
    gantiIndexMenu = []
    gantiIndexHarga = []
    gantiPesanan = []

    for i in range(1,len(menu)+1):
      gantiIndexMenu.append(i)
    for i in range(1,len(menu)+1):
      gantiIndexHarga.append(i)

    gantiIndex = pd.Series(menu, gantiIndexMenu)
    gantiIndex2 = pd.Series(harga, gantiIndexHarga)
    
    #menampilkan menu
    print("DAFTAR MENU")
    for i in range(1,len(menu)+1):
      print(i, gantiIndex[i], gantiIndex2[i])
      print("")

    # menyimpan pesanan
    pesanan = int(input("Masukan pesanan "))
    jumlah = int(input("Masukan Jumlah pesanan "))    
    listPesanan.append(gantiIndex[pesanan])
    jumlahPesanan.append(jumlah)  
    totalHarga.append(jumlah * gantiIndex2[pesanan])

    #merubah index pesanan
    gantiTotalHarga = []
    for i in range(1,len(totalHarga)+1):
      gantiPesanan.append(i)

    gantiIndexPesanan = pd.Series(jumlah, gantiPesanan)
    gantiListPesanan = pd.Series(listPesanan, gantiPesanan) 
    gantiTotalHarga =   pd.Series(totalHarga, gantiPesanan) 

    print("")

  if(pilihan == 3):
    pelanggan  = input("Masukan nama pelanggan: ")
    print("Jumlah yang harus dibayarkan :", sum(totalHarga))
    uangMasuk = int(input("Uang Masuk Pelanggan: "))

    jumlahBayar = 0

    for item in totalHarga:
      jumlahBayar += item    
    
    kembalian = uangMasuk - jumlahBayar

    print("\n===========================")
    print("======= S T R U K   B E L I =====")
    print("===========================")
    print ("Nama         :",pelanggan)
    print("Pesanan :")
    for i in range(1, len(gantiPesanan)+1):
      print(i, gantiListPesanan[i], gantiIndexPesanan[i], totalHarga[i-1])
       
    print ("Tagihan       : Rp.",sum(totalHarga))
    print ("Uang          : Rp.",uangMasuk)
    print ("Kembalian     : Rp.",kembalian)
    print("===========================")
    print("===========================")
    
  
  if(pilihan == 4):
    break
