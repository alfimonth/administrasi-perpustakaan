from fungsi import *
import date
import database as db

def main_menu():
	next()
	main_head(db.l_n())
	info_box(date.tanggal,f"Jumlah buku = {db.jumlah_buku()}", f"Jumlah anggota = {db.jumlah_anggota()}")
	opt("1.Katalog\n2.Kenggotaan\n3.Peminjaman\n4.Pengaturan\n5.Keluar\n0.Refresh",'Menu')

	def  katalog():
		next()
		head('KATALOG')
		l = db.load_book()
		if l == []:
			print("'Belum Ada Buku'")
		else :
			# create terminal header table
			print("{:^3}|{:^20}|{:^15}|{:^11}|{:^7}|{:^6}|{:^20}|{:^10}".format('No.','Judul','Penulis','Jenis','Tebal','Jumlah','Letak','ID'))
			# create content of table
			print('='*100)
			for row in range (len(l)):
				print ("{:>3}|{:<20}|{:<15}|{:<11}|{:>7}|{:>6}|{:<20}|{:<10}".format(str(row+1)+'.',l[row][0], l[row][1], l[row][2], l[row][3], l[row][4], l[row][5], l[row][6]))
			
		br()
		opt("1.Tambah Buku\n2.Temukan Buku\n3.Hapus Buku\n4.Kosongkan Katalog\n0.Kembali")

		def add_book():
			next()
			head("Tambah Buku")
			nama_buku = tab_i('Judul')
			pengarang = tab_i('Penulis')
			tab_p("Jenis Buku",'1.Fiksi')
			tab_p('','2.NonFiksi',sep='None')
			pilihan = ''
			while pilihan == '':
				pilihan= tab_i("Pilih (1/2)")
				if pilihan == '1':
					jenis_buku = "Fiksi"					    	
				elif pilihan == '2':
					jenis_buku = "Non Fiksi"
				else:
					nothing()
					pilihan = ''

			w_buku = tab_i_int("Tebal Buku")
			q_buku = tab_i_int("Jumlah Buku")
			letak_buku = tab_i("Letak")
			# create id
			l_n = db.l_n()
			id_buku = (l_n[0]+nama_buku[0]+pengarang[0]+pilihan+str(w_buku))
			br()
			tab_p("ID terbuat",id_buku)
			# konfirmasi penambahan
			br()
			print("Apakah Anda yakin bahwa input sudah benar?")
			opt("1.Yakin\n2.Ubah input\n3.Batal tambah Buku")
			pilihan = ''
			while pilihan == '':
				pilihan = answer()
				if pilihan == '1':
					db.insert_book(nama_buku, pengarang, jenis_buku, w_buku, q_buku, letak_buku, id_buku)
					katalog()
				elif pilihan == '2':
					add_book()
				elif pilihan == '3':
					katalog()
				else:
					nothing()
					pilihan = ''
		
		def find_book():
			br()
			filter = input ("Masukan kata kunci Judul yang dicari : ")
			l = db.filter_book(filter)
			
			next()
			head(f"Hasil Pencarian untuk '{filter}'")
			if l == []:
				print("Tidak ada hasil yang ditemukan")
			else :
				# create terminal header table
				print("{:>3}|{:^20}|{:^15}|{:^11}|{:^7}|{:^6}|{:^20}|{:^10}".format('No.','Judul','Penulis','Jenis','Tebal','Jumlah','Letak','ID'))
				print('='*100)
				# create content of table
				for row in range(len(l)):
					print ("{:>3}|{:<20}|{:<15}|{:<11}|{:>7}|{:>6}|{:<20}|{:<10}".format(str(row+1)+'.',l[row ][1], l[row][2], l[row][3], l[row][5], l[row][5], l[row][6], l[row][7]))

			br()
			opt("0.Kembali")

			pilihan = ''
			while pilihan == '':
				pilihan = answer()
				if pilihan == '0':
					katalog()
				else:
					nothing()
					pilihan = ''

		def delete_book():
			br()
			w_d = input("Masukkan ID Buku yang akan dihapus : ") #will delete
			l=db.load_book()
			for i in range(len(l)):
				if l[i][6] == w_d :
					t_w_d = db.select_book(w_d)
					print(f"Apakah Anda yakin menghapus buku dengan Judul '{t_w_d[0][0]}'? (y/n)")
					pilihan = ''
					while pilihan == '':
						pilihan = answer()
						if pilihan == 'y':
							db.delete_book(w_d)
							katalog()
						elif pilihan == 'n':
							katalog()
						else:
							nothing()
							pilihan = ''
					break
				else :
					if i == len(l)-1:
						print("ID tidak ditemukan")
						opt("1.Masukkan ID lagi\n0.Kembali")
						pilihan = ''
						while pilihan == '':
							pilihan = answer()
							if pilihan == '1' :
								delete_book()
							elif pilihan == '0':
								katalog()
							else:
								nothing()
								pilihan = ''
		
		def clear_book():
			br()
			print("Apakah Anda yakin akan mengosongkan Katalog? (y/n)")
			pilihan = ''
			while pilihan == '':
				pilihan = answer()
				if pilihan == 'y':
					db.clear_book()
					katalog()
				elif pilihan == 'n':
					katalog()
				else:
					nothing()
					pilihan = ''

		pilihan = ''
		while pilihan == '':
			pilihan = answer()
			if pilihan == '0':
				main_menu()
			elif pilihan == '1':
				add_book()
			elif pilihan == '2':
				find_book()
			elif pilihan == '3':
				delete_book()
			elif pilihan == '4':
				clear_book()
			else:
				nothing()
				pilihan = ''

	def members():
		next()
		head('KEANGGOTAAN')
		l = db.members()
		if l == []:
			print("Belum Ada Anggota")
		else :
			# create terminal header table
			print("{:>3}|{:^20}|{:^15}|{:^11}|{:^7}|{:^6}".format('No.','Nama','Alamat','Umur','ID','Tanggal Mendaftar'))
			# create content of table
			print('='*100)
			for row in range(len(l)):
				print ("{:>3}|{:<20}|{:<15}|{:>11}|{:>7}|{:<6}".format(str(row+1)+'.',l[row ][0], l[row][1], l[row][2], l[row][3], l[row][4]))
				
		br()
		opt("1.Pendaftaran Anggota\n2.Temukan Anggota\n3.Hapus Anggota\n4.Kosongkan Anggota\n0.Kembali")
		
		def add_member():
			next()
			head("Pendaftaran Anggota")
			nama_anggota = tab_i ("Masukkan Nama")
			alamat_anggota = tab_i("Masukkan Alamat")
			umur_anggota = tab_i_int("Masukkan Umur")
			l_n=db.l_n()
			id_anggota = (l_n[0]+nama_anggota[0]+alamat_anggota[0]+str(umur_anggota))
			br()
			tab_p("ID terbuat",id_anggota)
			
			# Konfirmasi penambahan
			br()
			print("Apakah Anda yakin bahwa input sudah benar?")
			opt("1.Yakin\n2.Ubah input\n3.Batal daftar Anggota")
			pilihan = ''
			while pilihan == '':
				pilihan=answer()
				if pilihan == '1':
					tanggal = date.tanggal_only
					db.insert_members(nama_anggota, alamat_anggota, umur_anggota, id_anggota, tanggal)
					pilihan = members()
				elif pilihan == '2':
					pilihan = add_member()
				elif pilihan == '3':
					pilihan = members()
				else:
					nothing()
					pilihan = ''
		
		def find_member():
			br()
			filter = input ("Masukan kata ID Anggota yang dicari : ")
			l = db.filter_member(filter)
			next()
			head(f"Hasil Pencarian untuk '{filter}'")
			if l == []:
				print("Tidak ada hasil yang ditemukan")
			else :
				# create terminal header table
				print("{:>3}|{:^20}|{:^15}|{:^11}|{:^7}|{:^6}".format('No.','Nama','Alamat','Umur','ID','Tanggal Mendaftar'))
				# create content of table
				print('='*100)
				for row in range(len(l)):
					print ("{:>3}|{:<20}|{:<15}|{:<11}|{:>7}|{:>6}".format(str(row+1)+'.',l[row ][1], l[row][2], l[row][3], l[row][4], l[row][5]))
			br()
			opt("0.Kembali")

			pilihan = ''
			while pilihan == '':
				pilihan = answer()
				if pilihan == '0':
					members()
				else:
					nothing()
					pilihan = ''

		def delete_member():
			br()
			w_d = input("Masukkan ID Anggota yang akan dihapus : ")
			t_w_d = db.select_member(w_d)
			for i in range(len(l)):
				if l[i][3] == w_d :
					print(f"Apakah Anda yakin menghapus Anggota dengan Nama '{t_w_d[0][0]}'? (y/n)")
					pilihan = ''
					while pilihan == '':
						pilihan = answer()
						if pilihan == 'y':
							db.delete_members(w_d)
							members()
						elif pilihan == 'n':
							members()
						else:
							nothing()
							pilihan = ''
					break

				else :
					if i == len(l)-1:
						print("ID tidak ditemukan")
						opt("1.Masukkan ID lagi\n0.Kembali")
						pilihan = ''
						while pilihan == '':
							pilihan = answer()
							if pilihan == '1' :
								delete_member()
							elif pilihan == '0':
								members()
							else:
								nothing()
								pilihan = ''

		def clear_members():
			br()
			print("Apakah Anda yakin akan mengosongkan Anggota? (y/n)")
			pilihan = ''
			while pilihan == '':
				pilihan = answer()
				if pilihan == 'y':
					db.clear_members()
					members()
				elif pilihan == 'n':
					members()
				else:
					nothing()
					pilihan = ''
					
		pilihan = ''
		while pilihan == '':
			pilihan=answer()
			if pilihan == '0':
				main_menu()
			elif pilihan == '1':
				add_member()
			elif pilihan == '2':
				find_member()
			elif pilihan == '3':
				delete_member()
			elif pilihan == '4':
				clear_members()
			else:
				nothing()
				pilihan = ''

	def peminjaman(): 
		next()
		head('PEMINJAMAN')
		l= db.load_peminjaman()
		if l == []:
			print("Belum Ada Peminjaman")
		else :
			# create terminal header table
			print("{:>3}|{:^19}|{:^19}|{:^15}|{:^19}|{:^15}".format('No.','Awal Peminjaman','Judul','Peminjam','Batas Pengembalian','Status'))
			# create content of table
			print('='*100)
			for row in range(len(l)):
				if l[row][4] == 1:
					status = 'Belum Dikembalikan'
				elif l[row][4] == 2:
					status = 'Sudah Dikembalikan'
				print ("{:>3}|{:<19}|{:<19}|{:<15}|{:<19}|{:<20}".format(str(row+1)+'.',l[row][0], l[row][1], l[row][2], l[row][3], status))
				
		br()
		opt("1.Pinjam Buku\n2.Kembalikan Buku\n0.Kembali")

		def pinjam():
			# ID buku
			l_b = db.load_book()
			if l_b==[]:
				br()
				print("Tidak ada Buku untuk dipinjam")
				br()
				opt("1.Ke Katalog\n0.Kembali")
				pilihan = ''
				while pilihan == '':
					pilihan = answer()
					if pilihan == '0':
						peminjaman()
					elif pilihan == '1':
						katalog()
					else:
						nothing()
						pilihan = ''
			else :
				l_m = db.members()
				if l_m == []:
					br()
					print("Tidak ada Anggota\nPerlu menjadi Anggota untuk meminjam Buku")
					br()
					opt("1.Ke Anggota\n0.Kembali")
					pilihan= ''
					while pilihan == '':
						pilihan = answer()
						if pilihan == '0':
							peminjaman()
						elif pilihan == '1':
							members()
						else:
							nothing()
							pilihan = ''

				else:
					br()
					k_b = tab_i("Masukkan ID Buku")
					for i in range(len(l_b)):
						if l_b[i][6] == k_b :
							n_b = db.select_book(k_b)
							# Id anggota
							input_idm = True
							while input_idm == True:
								k_m= tab_i('Masukkan ID Anggota')
								for i in range(len(l_m)):
									if l_m[i][3] == k_m:
										# struk peminjaman
										l_n = db.l_n()
										next()
										print('^'*50)
										print("{:^50}".format('PERPUSTAKAAN')+"\n"+"{:^50}".format(l_n))
										br()
										print('================ STRUK PEMINJAMAN ================')
										n_a = db.select_member(k_m)
										br()
										tab_p("Judul Buku",n_b[0][0])
										tab_p("Peminjam",n_a[0][0])
										tab_p("Meminjam pada",date.tanggal)
										w_buku = db.width_book(k_b)
										tab_p("Tebal Buku",str(w_buku)+' lembar')

										if w_buku < 100 :
											x = 5
										elif 100 <= w_buku < 500  :
											x = 7			
										elif 500 <= w_buku < 1000  :
											x = 14
										else:
											x = 30	
										
										tab_p("Waktu Peminjaman",f"{x} hari")
										
										batas_p = date.batas_p(x)
										tab_p("Batas Pengembalian",batas_p)
										br()
										print('='*50)
										br()
										print("{:^50}".format("Buku yang sudah dipinjam harus dikembalikan")+'\n'+"{:^50}".format("tepat waktu"))
										br()
										print('^'*50)
										br()
										print("Konfirmasi Peminjaman")
										opt('1.Konfirmasi\n0.Batal Pinjam')
										pilihan = ''
										while pilihan == '':
												pilihan = answer()
												if pilihan == '1' :
													tanggal=date.tanggal
													db.insert_peminjaman(tanggal,n_b[0][0],n_a[0][0],batas_p,k_b,k_m)
													qty = db.q_buku(k_b)
													db.update_qbook(qty,k_b)
													peminjaman()														
												elif pilihan == '0':
													peminjaman()
												else:
													nothing()
													pilihan = ''

									else :
										if i == len(l_m)-1:
											br()
											print("ID anggota tidak ditemukan")
											opt("1.Masukkan ID lagi\n0.Kembali")
											pilihan = ''
											while pilihan == '':
												pilihan = answer()
												if pilihan == '1' :
													br()
													input_idm = True
												elif pilihan == '0':
													peminjaman()
												else:
													nothing()
													pilihan = ''
							break	
			
						else :
							if i == len(l_b)-1:
								br()
								print("ID tidak ditemukan")
								opt("1.Masukkan ID lagi\n0.Kembali")
								pilihan = ''
								while pilihan == '':
									pilihan = answer()
									if pilihan == '1' :
										pinjam()
									elif pilihan == '0':
										peminjaman()
									else:
										nothing()
										pilihan = '' 
	
		def kembalikan():
			l_p = db.load_peminjaman()
			if l_p==[]:
				br()
				print("Belum ada Peminjaman")
				br()
				opt("0.Kembali")
				pilihan = ''
				while pilihan == '':
					pilihan = answer()
					if pilihan == '0':
						peminjaman()
					else:
						nothing()
						pilihan = ''
			else :
				br()
				k_b = tab_i("Masukkan ID Buku")
				for i in range(len(l_p)):
					if l_p[i][5] == k_b :
						loc_b = i
						n_b = db.select_book(k_b)[0][0]
						# Id anggota
						input_idm = True
						while input_idm == True:
							k_m= tab_i('Masukkan ID Anggota')
						
							if l_p[loc_b][6] == k_m:
								n_a = db.select_member(k_m)[0][0]
								print(f"Anggota bernama {n_a} akan mengembalikan Buku yang berjudul {n_b}? (y/n)")
								pilihan = ''
								while pilihan == '':
										pilihan = answer()
										if pilihan == 'y' :
											db.kembali(k_b)
											
											
											peminjaman()														
										elif pilihan == 'n':
											peminjaman()
										else:
											nothing()
											pilihan = ''

							else :
							
								br()
								print("ID anggota tidak ditemukan")
								opt("1.Masukkan ID lagi\n0.Kembali")
								pilihan = ''
								while pilihan == '':
									pilihan = answer()
									if pilihan == '1' :
										br()
										input_idm = True
									elif pilihan == '0':
										peminjaman()
									else:
										nothing()
										pilihan = ''
				
						break	
		
					else :
						if i == len(l_p)-1:
							br()
							print("ID tidak ditemukan")
							opt("1.Masukkan ID lagi\n0.Kembali")
							pilihan = ''
							while pilihan == '':
								pilihan = answer()
								if pilihan == '1' :
									kembalikan()
								elif pilihan == '0':
									peminjaman()
								else:
									nothing()
									pilihan = '' 


		pilihan = ''
		while pilihan == '':
			pilihan = answer()
			if pilihan == '0':
				main_menu()
			elif pilihan == '1': 
				pinjam()
			elif pilihan == '2':
				kembalikan()
			else:
				nothing()
				pilihan = ''
				
	def settings():
		next()
		head('PENGATURAN')
		opt("1.Ubah Nama Perpustakaan\n2.Keamanan\n3.About Us\n0.Kembali")

		def change_name():
			next()
			head('Ubah Nama Perpustakaan')
			l_n = db.l_n()
			print(f"Nama Perpustakaan : {l_n}")
			opt("1.Ganti Nama\n2.Reset Nama\n0.Kembali")
			pilihan = ''
			while pilihan == '':
				pilihan=answer()
				if pilihan == '0':
					settings()
				# Pilihan-1 mengatur nama
				elif pilihan == '1':
					br()
					new_ln = input("Masukkan nama baru perpustakaan : ")
					db.update_ln(new_ln)
					change_name()
				# Reset nama
				elif pilihan == '2':
					new_ln = 'X'
					db.update_ln(new_ln)
					change_name()
				else :
					nothing()
					pilihan = ''
		def security():
			next()
			head('KEAMANAN')
			s_c = db.lock()
			pw = db.pw()
			
			if s_c == 0 :
				status = 'Off'
			else :
				status = 'On'
			print(f"Status Keamanan : {status}")
			opt("1.On/Off\n2.Ubah Sandi\n0.Kembali")	
			pilihan = ''
			while pilihan == '':
				pilihan=answer()
				if pilihan == '0':
					settings()
				elif pilihan == '1' : # Menghidupkan keamanan
					if status == 'Off' :
						br()
						new_pw = input("Atur sandi : ")
						db.set_pw(new_pw)
						security()
					else : # Matikan keamanan
						print('Apakah anda yakin ingin menonaktifkan keamanan? (y/n)')
						pilihan = ''
						while pilihan == '':
							pilihan = answer()
							if pilihan == 'y':
								db.off_lock()
								security()
							elif pilihan == 'n':
								security()
							else:
								nothing()
								pilihan = ''

				elif pilihan == '2':
					if status == 'Off':
						br()
						print("Untuk mengubah sandi aktifkan keamanan terlebih dahulu")
						br()
						pilihan=''
					else :
						sandi = False
						while sandi == False :
							old_pw = input("Masukkan Sandi Lama : ")
							if old_pw != pw:
								print("Sandi Salah")
							else :
								sandi = True
								new_pw = input("Masukkan Sandi Baru : ")
								db.set_pw(new_pw)
								print (new_pw)
								print (pw)
								security()
				else :
					nothing()
					pilihan = ''

		def about_us():
			next()
			head('ABOUT US')
			kelompok_2()
			br()
			print('{:^100}'.format('Alfi-Hamonangan-Hikari-Rifky-Zakky'))
			br()
			opt('0.Kembali')
			pilihan = ''
			while pilihan == '':
				pilihan = answer()
				if pilihan == '0':
					settings()					
				else :
					nothing()
					pilihan = ''

		pilihan = ''
		while pilihan == '':
			pilihan = answer()
			if pilihan == '0':
				main_menu()
			elif pilihan == '1':
				change_name()
			elif pilihan == '2':
				security()
			elif pilihan == '3':
				about_us()
			else:
				nothing()
				pilihan = ''
				
	pilihan = ''
	while pilihan == '':
		pilihan = answer()
		if pilihan == '1':
			katalog()
		elif pilihan == '2':
			members()
		elif pilihan == '3':
			peminjaman()
		elif pilihan == '4':
			settings()
		elif pilihan == '5':
			exit()
		elif pilihan == '0':
			main_menu()
		else:
			nothing()
			pilihan = ''

def lockscreen(): # lockscreen
	lock = db.lock()
	
	if lock == 0 : # keamanan off
		main_menu()
		
	else : # keamanan on
		pw = db.pw()
		next()
		head("Program Administrasi Perpustakaan")
		sandi = False
		while sandi == False :
			in_pw = input("Masukkan Sandi Untuk Masuk : ")
			
			if in_pw != pw: # sandi salah
				br()
				print("{:^100}".format("| Sandi Salah |"))
				br()

			else : # sandi benar
				sandi = True
				main_menu()

if __name__ == '__main__':
	lockscreen()