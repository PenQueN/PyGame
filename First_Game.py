#pygame documentation
#https://devdocs.io/
#https://devdocs.io/pygame/?fbclid=IwAR3SuXSL6_LkawiXJbET6Unm4W9XPJc1ff1JwpBNFvKspSGY0xKV2PsVUKI
import pygame
import random


#เริ่มต้นโปรเจค pygame
pygame.init() 

#ค่า SETTTING นิยมใช้ตัวพิมพ์ใหญ่
# FPS per second
FPS = 30 
#ปรับความกว้าง
WIDTH = 800 
#ปรับความสูง
HEIGHT = 700 
#สร้างสี
BLACK = (0,0,0) 
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
#คะแนนเมื่อยิงโดน
SCORE = 0
#ชีวิต
LIVES = 3

#สร้างสกรีนหรือกล่องสำหรับใส่เกม
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('My First Game')

#background
bg = r'C:\Users\thana.pentum\Desktop\Python\Training Python\Uncle Engineer\PyGame - 20 Week\EP5\bg.gif'
background = pygame.image.load(bg).convert_alpha()
background_rect = background.get_rect()

#สร้างนาฬิกาของเกม
clock = pygame.time.Clock() 

class Enemy(pygame.sprite.Sprite): #ดึงความสามารถของ pygame มาใช้ใน class

    def __init__(self): #self คือตัวของมันเอง
        #ฟังก์ชั่นหลักที่มันจะรันทุกครั้งเมื่อีการเรียกใช้
        pygame.sprite.Sprite.__init__(self)
        
        #เอารูปภาพใส่
        img = r'C:\Users\thana.pentum\Desktop\Python\Training Python\Uncle Engineer\PyGame - 20 Week\EP5\aircraft.png'
        self.image   = pygame.image.load(img).convert_alpha() #convert alpha หมายถึงเอารูปภาพไปอยู่ใน pygame
        
        #self.image = pygame.Surface((50,50))
        #self.image.fill(GREEN)
        
        #สร้างสี่เหลี่ยม
        self.rect = self.image.get_rect()
        #สุ่มตำแหน่งแนวแกน x
        rand_x = random.randint(self.rect.width,WIDTH - self.rect.width)
        #ตำแหน่งจกาจุดศูนย์กลางของตัวละคร
        self.rect.center = (rand_x,0 - self.rect.height)

        #speed แนวแกน y
        self.speed_y = random.randint(1,10)

    def update(self):
        self.rect.y += self.speed_y #เพิ่ม Speed
        if self.rect.bottom > HEIGHT + self.rect.height:
            self.rect.y = 0
            #สุ่มตำแหน่งแนวแกน x
            rand_x = random.randint(self.rect.width,WIDTH - self.rect.width)
            self.rect.x = rand_x
            self.speed_y = random.randint(1,10)

class Player(pygame.sprite.Sprite): #ดึงความสามารถของ pygame มาใช้ใน class

    def __init__(self): #self คือตัวของมันเอง
        #ฟังก์ชั่นหลักที่มันจะรันทุกครั้งเมื่อีการเรียกใช้
        pygame.sprite.Sprite.__init__(self)
        
        #เอารูปภาพใส่
        img = r'C:\Users\thana.pentum\Desktop\Python\Training Python\Uncle Engineer\PyGame - 20 Week\EP5\bomber.png'
        self.image   = pygame.image.load(img).convert_alpha() #convert alpha หมายถึงเอารูปภาพไปอยู่ใน pygame

        #self.image = pygame.Surface((50,50))
        #self.image.fill(RED)

        #สร้างสี่เหลี่ยม
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT - self.rect.height)

        # Speed x
        self.speed_x = 0

    def update(self):
        #self.rect.y += 5
        self.speed_x = 0 #ใส่ 0 เพื่อที่ว่าเมื่อไหร่ที่กด คีย์บอร์ด  ถึงจะขยับ  ถ้าเอาบรรทัดนี้ออกก็วิ่งต่อเมื่อมีการกดเลย
        #ตรวจสอบว่ามีการกดปุ่มหรือไม่? ปุ่มอะไร?
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -20        
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 20
        
        self.rect.x += self.speed_x  #เพิ่มค่า Speed เข้าไปเมื่อมีการกด


        if self.rect.bottom > HEIGHT:
            self.rect.y = 0
    
    def shoot(self):
        bullet = Bullet(self.rect.centerx,self.rect.top) #center x คือ ให้กระสุนออกจากตัว center ของ player และ top คือยิงจากส่วนหัวของ player
        all_sprites.add(bullet) #add sprite เข้าไป
        group_bullet.add(bullet) #add sprite bullet เข้าใส่ group

class Bullet(pygame.sprite.Sprite): #ดึงความสามารถของ pygame มาใช้ใน class

    def __init__(self,x,y): #self คือตัวของมันเอง x,y เพื่อมากำหนด location ของ bullet
        #ฟังก์ชั่นหลักที่มันจะรันทุกครั้งเมื่อีการเรียกใช้
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((10,10))
        self.image.fill(RED)

        #สร้างสี่เหลี่ยม
        self.rect = self.image.get_rect()
        self.rect.centerx = x  # x = center ของเครื่องบิน
        self.rect.bottom = y   # y = จุด TOP ของเครื่องบิน

        # Speed y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y 

        #ในกรณีกระสุนออกจากทะลุจอ  ให้ลบกระสุนออก y < 0
        if self.rect.y < 0:
            self.kill() #function พิเศษในการลบ sprite


# Score
font_name = pygame.font.match_font('arial')
def draw_text(screen,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x,y)
    screen.blit(text_surface,text_rect)

#draw_text(screen,'SCORE:100',30,WIDTH-100,10)


# สร้างกลุ่ม Sprite
all_sprites = pygame.sprite.Group() #กล่องสำหรับเก็บตัวละครบทุกตัว
group_enemy = pygame.sprite.Group() #กล่องสำหรับเก็บศัตรู
group_bullet = pygame.sprite.Group() #กล่องสำหรับเก็บลูกกระสุน


# Player
Player = Player() #มาจาก class ด้านบนมาเก็บตัวแปร player สร้างตัวละครจากคลาส player
all_sprites.add(Player) #เพิ่มตัวละครเข้าไปในกลุ่ม

# Enemy
for i in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    group_enemy.add(enemy)



#สถานะของเกม
running = True 

while running: #ถ้าเป็นจริง จะรันเรื่อย ๆ
    #สั่งให้เกมรันตามเฟรมเรด
    clock.tick(FPS)
    #ตรวจสอบว่าเราปิดเกมแล้วหรือยัง ?
    #ถ้าหากเรากดกากบาท  จะสั่งให้ตัวแปร running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #เมื่อ player กด spacebar
                Player.shoot()  #ให้ player ยิง
    

    #ขยับตัว sprite ได้แล้ว (sprite คือตัวละคร)
    all_sprites.update()

    #ตรวจสอบการชนกันของ Sprite ด้วยฟังก์ชั่น Collide
    collide = pygame.sprite.spritecollide(Player,group_enemy,True) #False คือเวลา sprite ชนกันจะไม่หายไปถ้าเป็น True จะหายไป
    print(collide)
    if collide:
        LIVES -= 1

    if collide and LIVES == 0:
        #หากมีการชนกัน  จะปิดโปรแกรมทันที
        running = False

    
    #bullet collission
    hits = pygame.sprite.groupcollide(group_bullet,group_enemy,True,True)  #False คือเวลา sprite ชนกันจะไม่หายไปถ้าเป็น True จะหายไป
    print('Bullet:',hits)
    #แก้เรื่อง eneme โดยยิงแล้วหายไปหมด
    for h in hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        group_enemy.add(enemy)
        #เพิ่ม Score
        SCORE += 10




    #ใส่สี black ground ของเกม
    screen.fill(BLACK)  
    #ใส่ background ที่เราใส่เข้ามา
    screen.blit(background,background_rect)

    draw_text(screen,'SCORE: {}'.format(SCORE), 30, WIDTH-300, 10)
    draw_text(screen,'LIVES: {}'.format(LIVES), 30, WIDTH-100, 10)    

    #นำตัวละครทั้งหมดมาวาดใส่เกม
    all_sprites.draw(screen)

    #ทำให้ pygame แสดงผล
    pygame.display.flip() 

#ออกจากเกม
pygame.quit() 



