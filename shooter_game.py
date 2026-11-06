#Создай собственный Шутер!

from pygame import *
from random import randint

font.init()
mixer.init()

#cont1 += 1
#text_sum1 = text2 + str(cont1)
#print(text_sum1)
#count = font.render(text_sum1, True, (255, 255, 255))

abc = 0
globalABC = 0

globalABCd = 0

globalABCD = 0

bezpontovie = 0

valueMusic = 0.1

OCCHEN_KRUTAY_PEREMENNAY = 1

mixer.music.load('Egor_Letov-Rodina.ogg') #загружаем фоновую музыку
fire = mixer.Sound('blaster.ogg')

fire.set_volume(0.02) #выставляем громкость

abcde = 0

class GameSprite(sprite.Sprite): #создали класс родитель

    def __init__(self, player_image, player_x, player_y, player_speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_x,player_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

bullets = sprite.Group()
bbullets = sprite.Group() #создали группы

class Player(GameSprite):

    def update(self):
        global abc, valueMusic, OCCHEN_KRUTAY_PEREMENNAY
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT]:
            if self.rect.x >= 0:
                self.rect.x -= self.speed
        if key_pressed[K_RIGHT]:
            if self.rect.x <= 607:
                self.rect.x += self.speed
        if key_pressed[K_1]:
            if valueMusic <= 100:
                valueMusic += 0.01
                #print(valueMusic)
        if key_pressed[K_2]:
            if valueMusic >= 0:
                valueMusic -= 0.01
        if key_pressed[K_l]:
            OCCHEN_KRUTAY_PEREMENNAY += 1 
            print(OCCHEN_KRUTAY_PEREMENNAY)    
        if key_pressed[K_SPACE]:
            abc += 1
            if abc == 4:
                self.shot()
                abc = 0

    def shot(self):
        global globalABC
        if globalABC >= 6:
            bull = Bullet('cookie.png', 30, 30, 20, self.rect.centerx - 15, self.rect.top)
            bullets.add(bull)
            globalABC = 0
            fire.play()


class Enemy(GameSprite):
    
    def __init__(self, player_image, player_x, player_y, y=0):
        super().__init__(player_image, player_x, player_y, randint(1, 3), randint(0, 700), y)
        self.rect.x = randint(0, 500)
        self.player_speed = randint(1, 3)
    
    def update(self):
        global cont, false, count, cont1
        self.rect.y += self.player_speed
        if self.rect.y >= 500:
            cont += 1
            text_sum = text1 + str(cont)
            print(text_sum)
            false = font1.render(text_sum, True, (255, 255, 255))
            
            self.randomEn()
    
    def randomEn(self):
        self.rect.x = randint(0, 600)
        self.player_speed = randint(1, 3)  
        self.rect.y = -20


class Boss(GameSprite):

    def boss_fight(self, player):
        #for i in enemy:
        #    i.kill()
        #for i in asteroids:
        #    i.kill()
        self.shot()
        self.bred()
        

    def update(self):
        global abcde
        if abcde == 0:
            if self.rect.x <= 607:
                self.rect.x += self.speed
            else:
                abcde = 1
        elif abcde == 1: 
            if self.rect.x >= 0:   
                self.rect.x -= self.speed
            else:
                abcde = 0
            
    def shot(self):
        global globalABCd, globalABCD

        if globalABCD == bezpontovie:
            if globalABCd >= 6:
                bull = BossBullet('cookie.png', 30, 30, 20, self.rect.centerx - 15, self.rect.bottom)
                bbullets.add(bull)
                globalABCd = 0
                self.bred()
                fire.play()
        
    def bred(self):
        global bezpontovie, globalABCD
        bezpontovie = randint(0, 30)
        globalABCD = 0
    

class Bullet(GameSprite):
    
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

class BossBullet(GameSprite):

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.kill()
        


class Asteroid(GameSprite):

    def __init__(self, player_image,  player_x, player_y, y=0):
        super().__init__(player_image, player_x, player_y, randint(2, 4), randint(0, 700), y)
        self.rect.x = randint(0, 500)
        self.player_speed = randint(2, 4)
    
    def update(self):
        self.rect.y += self.player_speed
        if self.rect.y >= 500:
            self.randomAs()
    
    def randomAs(self):
        self.rect.x = randint(0, 600)
        self.player_speed = randint(2, 4)
        self.rect.y = -20

cont = 0
cont1 = 0
cont2 = 3

window = display.set_mode((700, 500)) #количество пикселей по X и Y
display.set_caption('Шутер') #ставим название окна

background = transform.scale(image.load('yandex_house.jpg'), (700, 500))

player = Player('firefox_player_png.png', 100, 100, 10, 0, 400)

boss = Boss('boss_roskomndzor_png.png', 100, 100, 10, 0, 0)

enemy = sprite.Group()

enemy.add(Enemy('yandex_evil_png.png', 100, 60))
enemy.add(Enemy('yandex_evil_png.png', 100, 60))
enemy.add(Enemy('yandex_evil_png.png', 100, 60))
enemy.add(Enemy('yandex_evil_png.png', 100, 60))
enemy.add(Enemy('yandex_evil_png.png', 100, 60)) #создаем врагов

asteroids = sprite.Group()

asteroids.add(Asteroid('yandex_as2_png.png', 60, 60))
asteroids.add(Asteroid('yandex_as2_png.png', 60, 60))

text1 = 'Пропущенно:'
text2 = 'Счет:'
text3 = 'Уровень:'
text4 = 'HP:'
text5 = 'Лучший результат:'
text6 = ' уровень'

text_sum = ''
text_sum1 = ''
text_sum2 = ''
text_sum3 = ''
text_sum4 = ''

font1 = font.Font('Comic Sans MS.ttf', 20)

count = font1.render('Счет:', True, (255, 255, 255))
false = font1.render('Пропущенно:', True, (255, 255, 255))
count_wave = font1.render('Уровень:1', True, (255, 255, 255))
hPPlayer = font1.render('HP:', True, (255, 255, 255))
BR = font1.render('Лучший результат:', True, (255, 255, 255))

font2 = font.Font('Comic Sans MS.ttf', 80)

over = font2.render('Вы проиграли!', True, (255, 0, 0))
win = font2.render('Вы выиграли!', True, (0, 128, 0))

game = True #переменая которая отвечает за работу игры

clock = time.Clock()
fps = 60

fps_podchet = 0

finish = False

a = 0
b = 0
c = 0
d = 0
e = 0

mertvie = 0

gosudarstvo = 0

boss_counter = 0

mixer.music.play()

kill_count = 15

passenemy_count = 5

collideas_count = 3

hp_boss = 20

hp_player = 5

kill_count = 15
passenemy_count = 5
collideas_count = 3
hp_boss = 20
hp_player = 5

text_sum3 = text4 + str(hp_player)
print(cont1)
hPPlayer = font1.render(text_sum3, True, (255, 255, 255))
window.blit(hPPlayer, (0, 50))

print(kill_count, passenemy_count, collideas_count, hp_boss, hp_player)

with open('best_result.txt', 'r') as file:
    data1 = file.read()

text_sum4 = text5 + str(data1) + text6
BR = font1.render(text_sum4, True, (255, 255, 255))
window.blit(BR, (300, 0))

'''with open('best_result.txt', 'r') as file:
    data = file.read()
    if data == '':
        with open('best_result.txt', 'w') as file1:
            file1.write('1')

with open('best_result.txt', 'r') as file:
    data = file.read()
    if data:
        print(123673)
        text_sum4 = text5 + str(data) + text6
    else:
        with open('best_result.txt', 'w') as file1:
            file1.write('1')
    

BR = font1.render(text_sum4, True, (255, 255, 255))
window.blit(BR, (300, 50))'''

while game: #цикл отображение fps

    '''with open('best_result.txt', 'r') as file:
        data = file.read()
        try:
            if int(data) >= 1:
                text_sum4 = text5 + str(data) + text6
        except:
            with open('best_result.txt', 'w') as file1:
                file1.write('1')

    BR = font1.render(text_sum4, True, (255, 255, 255))
    window.blit(BR, (300, 50))'''

    mixer.music.set_volume(valueMusic)
    '''if OCCHEN_KRUTAY_PEREMENNAY >= 2:
        kill_count += 20
        hp_boss += 25
        if passenemy_count >= 2:
            passenemy_count -= 1
        if collideas_count != 3:
            collideas_count -= 1
        if hp_player != 1:
            hp_player -1
        print(kill_count, passenemy_count, collideas_count, hp_boss, hp_player)
    elif OCCHEN_KRUTAY_PEREMENNAY == 2:
        kill_count = 30
        passenemy_count = 3
        collideas_count = 2
        hp_boss = 45
        hp_player = 3
    elif OCCHEN_KRUTAY_PEREMENNAY == 3:
        kill_count = 45
        passenemy_count = 2
        collideas_count = 1
        hp_boss = 80
        hp_player = 1'''

    globalABC += 1
    globalABCd += 1
    globalABCD += 1
    clock.tick(fps)
    
    window.blit(background, (0,0))

    if finish != True:
        if e == 0:
            player.update()
            player.reset()
            enemy.update()
            enemy.draw(window)
            bullets.update()
            bullets.draw(window)
            asteroids.update()
            asteroids.draw(window)
        player_collide = sprite.spritecollide(player, enemy, False)
        bullets_collide = sprite.groupcollide(enemy, bullets, False, True)
        asteroids_collide = sprite.spritecollide(player, asteroids, False)


        if player_collide:
            finish = True
            b = 1
            for i in enemy:
                i.randomEn()


        elif bullets_collide:
            cont1 += 1
            text_sum1 = text2 + str(cont1)
            print(cont1)
            count = font1.render(text_sum1, True, (255, 255, 255))
            

            if cont1 == kill_count:
                finish = True
                #cont1 = 0
                window.blit(count, (0, 70))
                boss_counter += 1
                if boss_counter == 0:
                    window.blit(over, (100, 200))
                    boss.boss_fight(player) #вызываю босса
                    b = 0
                    e = 1

            for i in bullets_collide:
                i.randomEn()


        elif cont >= passenemy_count:
            finish = True
            cont = 0
            cont1 = 0
            window.blit(false, (0, 90))
            b = 1

            for i in enemy:
                i.randomEn()


        if asteroids_collide:
            d += 1
            cont2 -= 1

            for i in asteroids_collide:
                i.randomAs()


            if d == collideas_count:
                finish = True
                b = 1
                for i in asteroids:
                    i.randomAs()
                d = 0


    else:


        if b == 0:
            cont = 0
            #cont1 = 0

            player.update()
            player.reset()
            boss.update()
            boss.reset()
            bullets.update()
            bullets.draw(window)

            bbullets.update()
            bbullets.draw(window)

            boss_collide = sprite.spritecollide(boss, bullets, True)
            player_bbcolide = sprite.spritecollide(player, bbullets, True)

            if boss_collide:
                mertvie += 1
                cont1 += 1
                text_sum1 = text2 + str(cont1)
                print(cont1)
                count = font1.render(text_sum1, True, (255, 255, 255))


            if player_bbcolide:
                gosudarstvo += 1
                text_sum3 = text4 + str(hp_player - gosudarstvo)
                print(cont1)
                hPPlayer = font1.render(text_sum3, True, (255, 255, 255))
                window.blit(hPPlayer, (0, 50))
                print(gosudarstvo)

            if mertvie == hp_boss:
                b = 2
                kill_count += 20
                hp_boss += 25
                if passenemy_count >= 2:
                    passenemy_count -= 1
                if collideas_count != 3:
                    collideas_count -= 1
                if hp_player != 1:
                    hp_player -= 1
                    text_sum3 = text4 + str(hp_player)
                    hPPlayer = font1.render(text_sum3, True, (255, 255, 255))
                    window.blit(hPPlayer, (0, 50))
                print(kill_count, passenemy_count, collideas_count, hp_boss, hp_player)
                mertvie = 0

            if gosudarstvo == hp_player:
                b = 1
                gosudarstvo = 0

            for i in enemy:
                i.randomEn()
            boss.boss_fight(player)


        if b == 1:
            cont = 0
            cont1 = 0
            OCCHEN_KRUTAY_PEREMENNAY = 1
            kill_count = 15
            passenemy_count = 5
            collideas_count = 3
            hp_boss = 20
            hp_player = 5
            window.blit(over, (100, 200))
            text_sum3 = text4 + str(hp_player)
            hPPlayer = font1.render(text_sum3, True, (255, 255, 255))
            window.blit(hPPlayer, (0, 50))

            for i in enemy:
                i.randomEn()
            a += 1


            if a == 60:
                player.rect.x = 0
                player.rect.y = 400
                count = font1.render('Счет:', True, (255, 255, 255))
                false = font1.render('Пропущенно:', True, (255, 255, 255))
                finish = False
                a = 0
                b = 0
                e = 0
                
                print('Это оччень крутая переменная', OCCHEN_KRUTAY_PEREMENNAY)
                text_sum2 = text3 + str(OCCHEN_KRUTAY_PEREMENNAY)
                count_wave = font1.render(text_sum2, True, (255, 255, 255))
                window.blit(count_wave, (0, 110))

                #text_sum4 = text5 + str(OCCHEN_KRUTAY_PEREMENNAY) + text6

                #BR = font1.render(text_sum4, True, (255, 255, 255))
                #window.blit(BR, (300, 50))
                 
        
        if b == 2:
            cont = 0
            cont1 = 0
            window.blit(win, (100, 200))
            

            a += 1


            if a == 60:
                player.rect.x = 0
                player.rect.y = 400
                count = font1.render('Счет:', True, (255, 255, 255))
                false = font1.render('Пропущенно:', True, (255, 255, 255))
                OCCHEN_KRUTAY_PEREMENNAY += 1
                finish = False
                a = 0
                b = 0
                
                text_sum3 = text4 + str(hp_player)
                hPPlayer = font1.render(text_sum3, True, (255, 255, 255))
                window.blit(hPPlayer, (0, 50))

                text_sum2 = text3 + str(OCCHEN_KRUTAY_PEREMENNAY)

                with open('best_result.txt', 'r') as file:
                    data = file.read()
                    #try:
                    #with open('best_result.txt', 'w') as file2:
                            #file2.write(str(OCCHEN_KRUTAY_PEREMENNAY))
                if data != '':
                    if int(data) < int(OCCHEN_KRUTAY_PEREMENNAY):
                        with open('best_result.txt', 'w') as file2:
                            file2.write(str(OCCHEN_KRUTAY_PEREMENNAY))
                else:
                    with open('best_result.txt', 'w') as file3:
                            file3.write(str(OCCHEN_KRUTAY_PEREMENNAY))
                    #except:
                        #print(123)
                    #data = file.read()
                with open('best_result.txt', 'r') as file:
                    data = file.read()
                text_sum4 = text5 + str(data) + text6
                BR = font1.render(text_sum4, True, (255, 255, 255))
                window.blit(BR, (300, 0))

                count_wave = font1.render(text_sum2, True, (255, 255, 255))
                window.blit(count_wave, (0, 110))

    window.blit(count, (0, 70))
    window.blit(false, (0, 90))
    window.blit(count_wave, (0, 110))
    window.blit(hPPlayer, (0, 50))
    window.blit(BR, (300, 0))

    display.update()

    for i in event.get():
        if i.type == QUIT:
            game = False