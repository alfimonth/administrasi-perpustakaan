import sqlite3
conn = sqlite3.connect('libdata.db')

# boot program
def create_db(db_name,t_h):
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS \
                '{}'({})".format(db_name,t_h))
        c.close()

print("Menghubungkan ke Database")
create_db("lock","activation INTEGER, password TEXT") 
create_db("nama_perpus","nama TEXT")
create_db("daftar_buku","title TEXT,writer TEXT, genre TEXT, width INTEGER, qty INTEGER, location TEXT, idbook TEXT" )
create_db("daftar_anggota","name TEXT,address TEXT, usia INTEGER, idmember TEXT, dt TEXT")
create_db("peminjaman","tanggal_peminjaman TEXT, judul_buku TEXT, peminjam TEXT, batas_pengembalian TEXT, status INTEGER, id_buku TEXT, id_peminjam TEXT")
print("Succes")

# Set default lock
print ("Menghubungkan ke Keamanan")
c = conn.cursor()
c.execute('''SELECT * FROM "lock"''')
lock=c.fetchall()
if lock == []:
        c.execute("INSERT INTO 'lock' VALUES(0,NULL)")
        conn.commit()
print("Succes")

# Set default Name
print("Menghubungkan ke Profil")
c.execute('''SELECT * FROM "nama_perpus"''')
l=c.fetchall()
if l == []:
        c.execute("INSERT INTO 'nama_perpus' VALUES ('X')")
        conn.commit()
c.close()
print("Succes")

# lock
def lock():
        c = conn.cursor()
        c.execute('''SELECT * FROM "lock"''')
        lock = c.fetchall()[0][0]
        c.close()
        return lock
        
def pw():
        c = conn.cursor()
        c.execute('''SELECT * FROM "lock"''')
        lock = c.fetchall()[0][1]
        c.close()
        return lock

def set_pw(x):
        print(x)
        c = conn.cursor()
        c.execute(f'''UPDATE "main"."lock" SET "password"='{x}' WHERE "_rowid_"="1"''')
        conn.commit()
        c.execute('''UPDATE "main"."lock" SET "activation"='1' WHERE "_rowid_"="1"''')
        conn.commit()
        c.close()

def off_lock():
        c= conn.cursor()
        c.execute('''UPDATE "main"."lock" SET "activation"='0' WHERE "_rowid_"="1"''')
        conn.commit()
        c.close()


# library name
def l_n():
        c = conn.cursor()
        c.execute('''SELECT * FROM "nama_perpus"''')
        l=c.fetchall()
        l_n=l[0][0]
        c.close()
        return l_n

def update_ln(x):
        c = conn.cursor()
        c.execute("UPDATE nama_perpus SET nama = '%s' WHERE _rowid_ IN ('1')"%(x))
        conn.commit()
        c.close

# katalog
def insert_book(nama_buku, pengarang, jenis_buku, w_buku, q_buku, letak_buku, id_buku):
        c = conn.cursor()
        c.execute("INSERT INTO daftar_buku VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(nama_buku, pengarang, jenis_buku, w_buku, q_buku, letak_buku, id_buku))
        conn.commit()
        c.close()

def load_book():
        c = conn.cursor()
        c.execute('''SELECT * FROM "daftar_buku" ORDER BY "title" ASC''')
        katalog=c.fetchall()
        c.close()
        return katalog

def select_book(x):
        c = conn.cursor()
        c.execute(f"SELECT title FROM daftar_buku WHERE idbook = '{x}'")
        select=c.fetchall()
        c.close()
        return select

def delete_book(x):
        c = conn.cursor()
        c.execute(f"DELETE FROM daftar_buku WHERE idbook = '{x}'")
        conn.commit()
        c.close()

def jumlah_buku():
        c = conn.cursor()
        c.execute('''SELECT qty FROM "daftar_buku"''')
        q_b= c.fetchall()
        q_buku=0
        for i in range(len(q_b)):
                q_buku = q_buku+q_b[i][0]
        return q_buku

def filter_book(x):
        c = conn.cursor()
        c.execute('''SELECT "_rowid_",* FROM "main"."daftar_buku" WHERE "title" LIKE '%{}%' ORDER by title ASC'''.format(x))
        l=c.fetchall()
        c.close()
        return l

def clear_book():
        c = conn.cursor()
        c.execute('''DELETE FROM "daftar_buku"''')
        conn.commit()
        c.close()
def width_book(x):
        c = conn.cursor()
        c.execute(f"SELECT width FROM daftar_buku WHERE idbook = '{x}'")
        l = c.fetchall()[0][0]
        c.close()
        return l
def q_buku(x):
        c =conn.cursor()
        c.execute(f"SELECT qty FROM daftar_buku WHERE idbook = '{x}'")
        l = c.fetchall()[0][0]-1
        c.close()
        return l

# keanggotaan
def insert_members(nama_anggota, alamat_anggota, umur_anggota, id_anggota, tanggal):
        c = conn.cursor()
        c.execute('''INSERT INTO daftar_anggota VALUES('{}', '{}', '{}', '{}', "{}")'''.format(nama_anggota, alamat_anggota, umur_anggota, id_anggota, tanggal))
        print('ya')
        conn.commit()
        print('ya')
        c.close()

def members():
        c = conn.cursor()
        c.execute('''SELECT * FROM "daftar_anggota" ORDER BY "title" ASC''')
        l=c.fetchall()
        c.close()
        return l

def filter_member(x):
        c = conn.cursor()
        c.execute(f'''SELECT "_rowid_",* FROM "main"."daftar_anggota" WHERE "idmember" LIKE '%{x}%' ORDER by name ASC''')
        l=c.fetchall()
        c.close()
        return l

def select_member(x):
        c = conn.cursor()
        c.execute(f"SELECT name FROM daftar_anggota WHERE idmember = '{x}'")
        l=c.fetchall()
        c.close
        return l

def delete_members(x):
        c = conn.cursor()
        c.execute(f"DELETE FROM daftar_anggota WHERE idmember = '{x}'")
        conn.commit()
        c.close()

def clear_members():
        c = conn.cursor()
        c.execute('''DELETE FROM "daftar_anggota"''')
        conn.commit()
        c.close()

def jumlah_anggota():					
        c = conn.cursor()
        c.execute('''SELECT idmember FROM "daftar_anggota"''')
        q_a = c.fetchall()
        q_member=len(q_a)
        c.close()
        return q_member

# peminjaman
def load_peminjaman():
        c = conn.cursor()
        c.execute('''SELECT * FROM "peminjaman" ORDER BY "tanggal_peminjaman" ASC''')
        l=c.fetchall()
        c.close()
        return l

def insert_peminjaman(tanggal,n_b,n_a,batas_p,k_b,k_m):
        c = conn.cursor()
        c.execute('''INSERT INTO peminjaman VALUES("{}", "{}", "{}", "{}","{}","{}","{}")'''.format(tanggal,n_b,n_a,batas_p,1,k_b,k_m))
        conn.commit()
        c.close

def update_qbook(x,y):
        c= conn.cursor()
        c.execute(f"UPDATE daftar_buku SET qty = {x} WHERE idbook = '{y}'")
        conn.commit()
        c.close()

def kembali(k_b):
        c = conn.cursor()
        c.execute(f"UPDATE peminjaman SET status =2 WHERE id_buku = '{k_b}'")
        conn.commit()
        c.execute(f"SELECT qty FROM daftar_buku WHERE idbook = '{k_b}'")
        q_buku = c.fetchall()
        qty = q_buku[0][0]+1
        c.execute(f"UPDATE daftar_buku SET qty = {qty} WHERE idbook = '{k_b}'")
        conn.commit()
        c.close()

# ^_^