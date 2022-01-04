from datetime import date, timedelta

def day_to_id(days): 
	if days == 'Sunday':
		d_id = 'Minggu'
	elif days == 'Monday':
		d_id = 'Senin'
	elif days == 'Tuesday':
		d_id = 'Selasa'
	elif days == 'Wednesday':
		d_id = 'Rabu'
	elif days == 'Thursday':
		d_id = 'Kamis'
	elif days == 'Friday':
		d_id = 'Jum\'at'
	elif days == 'Saturday':
		d_id = 'Sabtu'
	return d_id
        
now = date.today()
day = f"{now:%A}"
hari_id=day_to_id(day)
tanggal =f"{hari_id}, {now:%d-%m-%Y}"
tanggal_only = f"{now:%d-%m-%Y}"

def batas_p(x):
	waktu_peminjaman = timedelta(days=x)
	t_p = date.today() + waktu_peminjaman
	day = f"{t_p:%A}"
	hari_id = day_to_id(day)
	batas_p = f"{hari_id}, {t_p:%d-%m-%Y}"
	return batas_p
