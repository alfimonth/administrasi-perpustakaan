def br(): # spsi
        print()
def next():
        print('\n'*50)

# input dan print tab
def tab_i(text,sep=':',w=25): # digunakan untuk membuat pertanyaan
        if sep == 'None':
                sep = ' '
        a = input(('{:<'+f'{w}'+'}').format(text)+sep+' ')
        return a

def tab_i_int(text,sep=':',w=25): # digunakan untuk membuat pertanyaan integer
        if sep == 'None':
                sep = ' '
        u = True
        while u == True:
                try:
                        a = int(input(('{:<'+f'{w}'+'}').format(text)+sep+' '))
                        u = False
                except ValueError:
                        br()
                        print("{:^100}".format('| Input harus angka |'))
                        br()
        return a

def tab_p(text,text2,sep=':',w=25): # digunakan untuk membuat pernyataan
        if sep == 'None':
                sep = ' '
        print(('{:<'+f'{w}'+'}').format(text)+sep,text2)

def nothing():
        br()
        print("{:^100}".format('| Pilihan tidak tersedia |'))
        br()

# header
def main_head(title,top='~',bot='~',w=100):
        print(top*w)
        br()
        print(('{:^'+f'{w}'+'}').format('PERPUSTAKAAN'))
        print(('{:^'+f'{w}'+'}').format(title))
        br()
        print(bot*w)

def head(title,top='~',bot='~',w=100):
        print(top*w)
        br()
        print(('{:^'+f'{w}'+'}').format(title))
        br()
        print(bot*w)

def info_box(center='',kiri='',kanan='',top='=',bot='=',w=100):
	print(top*w)
	print("{:<30}{:^40}{:>30}".format(kiri,center,kanan))
	print(bot*w)


# pilihan
def opt(opt,title='Pilihan', sep=':'):
        print(title+' |'+'\n'+opt)

def answer(quest='Jawab', sep=':', w=100):
        print('_'*w)
        a = input(quest+' '+sep+' ')
        return a

def kelompok_2():
	print("{:^100}".format("  _   __   _____    _        ______    __    __    ______    ______    _   __    ______  "))
	print("{:^100}".format(" | | / /  |  ___|  | |      |  __  |  |  \  /  |  |  __  |  |  __  |  | | / /   |____  | "))
	print("{:^100}".format(" | |/ /   | |___   | |      | |  | |  |   \/   |  | |__| |  | |  | |  | |/ /     ____| | "))
	print("{:^100}".format(" |   <    |  ___|  | |      | |  | |  | |\  /| |  |  ____|  | |  | |  |   <     |  ____| "))
	print("{:^100}".format(" | |\ \   | |___   | |___   | |__| |  | | \/ | |  | |       | |__| |  | |\ \    | |____  "))
	print("{:^100}".format(" |_| \_\  |_____|  |_____|  |______|  |_|    |_|  |_|       |______|  |_| \_\   |______| "))
