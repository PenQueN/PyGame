import pygame

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

#สร้างสกรีนหรือกล่องสำหรับใส่เกม
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('My First Game by Unce Engineer')

#สร้างนาฬิกาของเกม
clock = pygame.time.Clock() 

class Player(pygame.sprite.Sprite): #ดึงความสามารถของ pygame มาใช้ใน class

    def __init__(self): #self คือตัวของมันเอง
        #ฟังก์ชั่นหลักที่มันจะรันทุกครั้งเมื่อีการเรียกใช้
        pygame.sprite.Sprite.__init__(self)
        
        #เอารูปภาพใส่
        img = r'C:\Users\thana.pentum\Desktop\Python\Training Python\Uncle Engineer\PyGame - 20 Week\EP3\aircraft.png'
        self.image   = pygame.image.load(img).convert_alpha()
        
        #self.image = pygame.Surface((50,50))
        #self.image.fill(GREEN)
        
        #สร้างสี่เหลี่ยม
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)

    def update(self):
        self.rect.y += 5
        if self.rect.bottom > HEIGHT + 92:
            self.rect.y = 0

# สร้างกลุ่ม Sprite
all_sprites = pygame.sprite.Group() #กล่องสำหรับเเก็บตัวละคร
Player = Player() #มาจาก class ด้านบนมาเก็บตัวแปร player สร้างตัวละครจากคลาส player
all_sprites.add(Player) #เพิ่ตัวละครเข้าไปในกลุ่ม


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
    

    #ขยับตัว sprite ได้แล้ว (sprite คือตัวละคร)
    all_sprites.update()


    #ใส่สี black ground ของเกม
    screen.fill(BLACK)  

    #นำตัวละครทั้งหมดมาวาดใส่เกม
    all_sprites.draw(screen)

    #ทำให้ pygame แสดงผล
    pygame.display.flip() 


pygame.quit() #ออกจากเกม



