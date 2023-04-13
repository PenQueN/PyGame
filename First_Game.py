#pygame documentation
#https://devdocs.io/
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

#สร้างสกรีนหรือกล่องสำหรับใส่เกม
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('My First Game')

#สร้างนาฬิกาของเกม
clock = pygame.time.Clock() 

class Enemy(pygame.sprite.Sprite): #ดึงความสามารถของ pygame มาใช้ใน class

    def __init__(self): #self คือตัวของมันเอง
        #ฟังก์ชั่นหลักที่มันจะรันทุกครั้งเมื่อีการเรียกใช้
        pygame.sprite.Sprite.__init__(self)
        
        #เอารูปภาพใส่
        img = r'C:\Users\thana.pentum\Desktop\Python\Training Python\Uncle Engineer\PyGame - 20 Week\EP4\aircraft.png'
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
        img = r'C:\Users\thana.pentum\Desktop\Python\Training Python\Uncle Engineer\PyGame - 20 Week\EP4\bomber.png'
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



# สร้างกลุ่ม Sprite
all_sprites = pygame.sprite.Group() #กล่องสำหรับเก็บตัวละครบทุกตัว

# Player
Player = Player() #มาจาก class ด้านบนมาเก็บตัวแปร player สร้างตัวละครจากคลาส player
all_sprites.add(Player) #เพิ่ตัวละครเข้าไปในกลุ่ม

# Enemy
for i in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)



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

    #ใส่สี black ground ของเกม
    screen.fill(BLACK)  

    #นำตัวละครทั้งหมดมาวาดใส่เกม
    all_sprites.draw(screen)

    #ทำให้ pygame แสดงผล
    pygame.display.flip() 


pygame.quit() #ออกจากเกม



