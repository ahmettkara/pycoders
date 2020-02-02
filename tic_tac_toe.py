print("""Welcome to Tic-Tac-Toe Game! The numeric keypad is as follows:\n
 1   2   3
 4   5   6
 7   8   9 \n""")

game_board=[
["___"]*3,
["___"]*3,
["___"]*3]

#game_board listesinin icinde 3 liste, ve her bir listenin içinde de 3 tane eleman olacak.

for i in game_board:
    print(*i)

k=1
keypad={}
#'k' degiskeni game_board'da bulunan koordinatları 'numeric keypad' seklinde olusturmak icin kullanılacak.
coordinats=list(range(3))
for i in coordinats:
    for j in coordinats:
        keypad[k]=[i,j]
        k+=1
### Bu dongu ile; {1: [0, 0], 2: [0, 1], 3: [0, 2] ...} seklinde sozluk olusacak.

winning_situation=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
# oyunda 8 tane kazanma durumu var.
x_coordinats=[]
o_coordinats=[]
all_coordinats=list(range(1,10))
#girilen numaralar all_coordinats listesinden cıkarılacak,
#'x' oyuncusunun numaraları 'x_coordinats' listesine, o oyuncusunun numaraları 'o_coordinats' listesine eklenecek.

for_logic_move=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
corners=[1,3,7,9]
middle=5
#bu listeler bilgisayarın akıllı hamleleri icin kullanılacak.

import random
turn=random.choice(["User", "Computer"])
move=random.choice([" X ", " O "])
print(f"\nIt is {turn}s turn and play with '{move}'\n")
#oyuna kimin, hangi hamle ile baslayacagini belirleyecek.

a=0
while a<9:
# toplam 9 hamle icin dongu kuruldu.
    if turn=="User":
        num = int(input("Enter a number: "))

    elif turn == "Computer":
        attack_move = []
        defence_move = []

#sira bilgisayarda iken game_board'daki duruma bakacak, varsa oyunu kazandıracak hamleleri attack_move listesinde,
#oyunu kaybetmemek icin yapılacak hamleleri ise defence_move listesinde tutacak.

        for l in for_logic_move:
            smart_x_for_comp = []
            smart_o_for_comp = []

            for m in l:
                if m in x_coordinats:
                    smart_x_for_comp += [m]
                if m in o_coordinats:
                    smart_o_for_comp += [m]

# her bir kazanma ihtimalinin icinde 2 tane 'X' veya 2 tane 'O' varsa,
# hamlesini; kazanma veya kaybetmeme ihtimallerine gore, o ihtimalin icindeki 3. koordinata yapması sağlanacak.

            if len(smart_x_for_comp) == len(l) - 1 and move == " X ":
# Game_board'da kazanma ihtimali bulunan 2 tane 'X' varsa ve bilgisayar 'X' ile oynuyor ise.
                for z in smart_x_for_comp:
                    l.remove(z)
                if l[0] in all_coordinats:
                    attack_move += [l[0]]

            elif len(smart_o_for_comp) == len(l) - 1 and move == " O ":
# Game_board'da kazanma ihtimali bulunan 2 tane 'O' varsa ve bilgisayar 'O' ile oynuyor ise.
                for z in smart_o_for_comp:
                    l.remove(z)
                if l[0] in all_coordinats:
                    attack_move += [l[0]]

            elif len(smart_x_for_comp) == len(l) - 1 and move == " O ":
# Game_board'da kazanma ihtimali bulunan 2 tane 'X' varsa ve bilgisayar 'O' ile oynuyor ise.
                for z in smart_x_for_comp:
                    l.remove(z)
                if l[0] in all_coordinats:
                    defence_move += [l[0]]

            elif len(smart_o_for_comp) == len(l) - 1 and move == " X ":
# Game_board'da kazanma ihtimali bulunan 2 tane 'O' varsa ve bilgisayar 'X' ile oynuyor ise.
                for z in smart_o_for_comp:
                    l.remove(z)
                if l[0] in all_coordinats:
                    defence_move += [l[0]]

        if len(attack_move) > 0:
            num = attack_move[0]
            attack_move.clear()
            defence_move.clear()
#Eger oyunu kazandıracak bir tane bile hamle varsa, hamleyi once oraya yapacak.

        elif len(attack_move) == 0 and len(defence_move) > 0:
            num = defence_move[0]
            attack_move.clear()
            defence_move.clear()
#Eger kazanma hamlesi yoksa savunma gerekiyor mu ona bakacak. Gerekiyorsa savunma hamlesini yapacak.

        else:
            if len(all_coordinats) == 9 or \
                    ((len(all_coordinats) == 7 or len(all_coordinats) == 8) and middle not in all_coordinats):

                for i in corners:
                    if i in all_coordinats:
                        num = random.choice(corners)
                        break
# ilk olarak koselerden oynayacak.

            elif (len(all_coordinats) == 8 or len(all_coordinats) == 7) and middle in all_coordinats:
                num = middle
# ikinci oncelik ortaya hamle yapmak olacak.

            else:
                num = random.choice(all_coordinats)
# yukaridaki hicbir sart ve ihtimal yoksa rastgele oynayacak.

    if num in all_coordinats:
        all_coordinats.remove(num)
# kullanıcı/bilgisayar tarafından numara girildikten sonra, girilen her numara, all_coordinats listesinden çıkarılacak.

        if move == " X ":
            x_coordinats.append(num)
        elif move == " O ":
            o_coordinats.append(num)
# girilen numaralar 'X' ise x_coordinats'da, 'O' ise o_coordinats'da toplanacak.

        for i in game_board:
            game_board[keypad[num][0]][keypad[num][1]] = move
# girilen numara game_board'un koordinatlarına islenecek.
# (keypad[num] un karşılığında; örneğin; keypad[1] icin [0,0], keypad[2] icin [0,1] tanımlı.)
            print(*i)
        print("\n")
        a+=1
#'a' degiskeni while dongusunun sayacı olarak tutulacak.

        for i in winning_situation:
            win_check_for_x = []
            win_check_for_o = []
# x_coordinats ve o_coordinats listeleri, winning_situation listesinin icinde bulunan listelerle karsılastırılacak ve
# winning_situation'daki listelerden birinin elemanları, x_coordinats veya o_coordinats'ın icinde ise oyun kazanilacak.

            for j in i:
                if j in x_coordinats:
                    win_check_for_x += [j]
                    if len(win_check_for_x) == len(i):
                        print("***** XXX WON! *****")
                        a=10

                if j in o_coordinats:
                    win_check_for_o += [j]
                    if len(win_check_for_o) == len(i):
                        print("***** OOO WON! *****")
                        a = 10

        if len(all_coordinats)==0 and a != 10:
            print("DRAW!")
# game_board'da bos yer kalmadıysa beraberlik yazacak.

    else:
        continue
#Eger oyuncu yanlıs bir giris yaptıysa asagı satırlara gecip sırayı ve hamleleri değiştirmemesini saglayacak.
#Basa dönüp hangi oyuncu hangi hamle ile oynuyorsa ondan tekrar giris yapmasını isteyecek. Gecerli hamle girildiyse
#yukaridaki islemler tamamlandiktan sonra asagıya gecip sıranın diger oyuncuya ve diger hamleye geçmesini saglayacak.

    if move==" X ":
        move=" O "
    elif move==" O ":
        move=" X "
    if turn== "User":
        turn="Computer"
    elif turn=="Computer":
        turn="User"


