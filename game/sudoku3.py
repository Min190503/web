import pygame

#font chữ
pygame.font.init()

#khởi tạo màn hình pygame 
screen = pygame.display.set_mode((500,700))

#Đặt caption cho màn hình pygame
pygame.display.set_caption("SUDOKU")

#Khởi tạo các giá trị
x =0
y =0
dif = 500/9
val = 0

#bảng sudoku
grid =[
		[7, 8, 0, 4, 0, 0, 1, 2, 0],
		[6, 0, 0, 0, 7, 5, 0, 0, 9],	
		[0, 0, 0, 6, 0, 1, 0, 7, 8],
		[0, 0, 1, 0, 5, 0, 9, 3, 0],
		[0, 0, 7, 0, 4, 0, 2, 6, 0],
		[9, 0, 4, 0, 6, 0, 0, 0, 5],
		[0, 7, 0, 3, 0, 0, 0, 1, 2],
		[1, 2, 0, 0, 0, 7, 4, 0, 0],
		[0, 4, 9, 2, 0, 6, 0, 0, 7]
	]

#inport các font chữ của pygame
font1 = pygame.font.SysFont("georgia", 36)
font2 = pygame.font.SysFont("georgia", 20)

#Lấy vị trí khi chọn
def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif

#vẽ viền xung quanh ô đang chọn
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7) 



#vẽ lưới sudoku
def draw():
    		
	for i in range (9):
		for j in range (9):
			if grid[i][j] != 0:
				cell_x = i * dif
				cell_y = j * dif
				pygame.draw.rect(screen, (0, 128, 128), (cell_x, cell_y, dif + 1, dif + 1)) #các ô có giá trị đã được điền sẽ được đổi thành màu xanh

				text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
				text_rect = text1.get_rect(center=(cell_x + dif // 2, cell_y + dif // 2))
				screen.blit(text1, text_rect)
	#Vẽ các đường lưới
	for i in range(10):
		if i % 3 == 0 :
			thick = 7
		else:
			thick = 1
		pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
		pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)	 


#vẽ giá trị val lên màn hình tại các vị trí tương ứng
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x*dif +15, y *dif + 15))

#báo lỗi khi nhập sai giá trị
def raise_error1():
    text1 = font1.render("Error!!!",1,(0,0,0))
    screen.blit(text1,(20,570))
def raise_error2():
    text1 = font1.render(" !!! Invalid value",1,(0,0,0))
    screen.blit(text1,(20,570))

#kiểm tra giá trị nhập vào có hợp lệ không
def valid(m,i,j,val):
    for it in range(9):
        if m[i][it] == val:
            return False
        if m[it][j] == val:
            return False
    it = i//3
    jt = j//3
    for i in range(it *3, it*3+3):
        for j in range(jt*3,jt*3+3):
            if m[i][j] == val:
                return False
    return True

#Thuật toán 
def solve(grid, i, j):
    	
	while grid[i][j]!= 0:
		if i<8:
			i+= 1
		elif i == 8 and j<8:
			i = 0
			j+= 1
		elif i == 8 and j == 8:
			return True
	pygame.event.pump() 
	for it in range(1, 10):
		if valid(grid, i, j, it)== True:
			grid[i][j]= it
			global x, y
			x = i
			y = j
			
			screen.fill((255, 255, 255))
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(20)
			if solve(grid, i, j)== 1:
				return True
			else:
				grid[i][j]= 0
			
			screen.fill((255, 255, 255))
		
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(10) 
	return False



def is_board_complete(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Kiểm tra xem có ô trống nào không
                return False
    return True
#Hiện thị thông báo sau khi kiểm tra
def check_solution():
	if is_board_complete(grid):
		if solve(grid, 0, 0):  
			text1 = font1.render("Sudoku board completed",1,(0,0,0))
			screen.blit(text1,(0,600))
            
		else:
			text1 = font1.render("Incorrect Sudoku solution",1,(0,0,0))
			screen.blit(text1,(10,600))
	else:
		text1 = font1.render("Sudoku board incomplete!!",1,(0,0,0))
		screen.blit(text1,(0,600))
	



#hiện thị nút
def instruction():
		text1 = font2.render("Press 'D' to reset/ Press 'R' to empty",1,(0,0,0))
		text2 = font2.render("Press Enter to check",1,(0,0,0))
		screen.blit(text1,(20,520))
		screen.blit(text2,(20,540))


def result():
	text1 = font1.render("",1,(0,0,0))
	screen.blit(text1, (20, 570)) 
run = True
flag1 = 0
flag2 = 0
flag3 = 0
rs = 0
error = 0

#chạy chương trình
while run:
	screen.fill((255,255,255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #khi người dùng chọn thoát
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN: # khi người dùng click chuột
			flag1 = 1
			pos = pygame.mouse.get_pos()
			get_cord(pos)

		if event.type == pygame.KEYDOWN: #khi người dùng bàn phím
			if event.key == pygame.K_LEFT:
				x-=1
				flag1 =1
			if event.key == pygame.K_RIGHT:
				x+=1
				flag1=1
			if event.key == pygame.K_UP:
				y-=1
				flag1 =1
			if event.key == pygame.K_DOWN:
				y+=1;
				flag1 =1
			if event.key == pygame.K_1:
				val = 1
			if event.key == pygame.K_2:
				val = 2
			if event.key == pygame.K_3:
				val = 3
			if event.key == pygame.K_4:
				val = 4
			if event.key == pygame.K_5:
				val = 5
			if event.key == pygame.K_6:
				val = 6
			if event.key == pygame.K_7:
				val = 7
			if event.key == pygame.K_8:
				val = 8
			if event.key == pygame.K_9:
				val = 9
			if event.key == pygame.K_RETURN: #chọn kiểm tra
				flag2 =1
			if event.key == pygame.K_m: #giải tự động
				flag3 = 1
			if event.key == pygame.K_r: #làm trống bảng
				rs = 0
				error = 0
				flag3 = 0
				grid =[
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0]
				]
    		#D để resert
			if event.key == pygame.K_d:
				rs = 0
				error = 0
				flag3 = 0
				grid =[
					[7, 8, 0, 4, 0, 0, 1, 2, 0],
					[6, 0, 0, 0, 7, 5, 0, 0, 9],
					[0, 0, 0, 6, 0, 1, 0, 7, 8],
					[0, 0, 7, 0, 4, 0, 2, 6, 0],
					[0, 0, 1, 0, 5, 0, 9, 3, 0],
					[9, 0, 4, 0, 6, 0, 0, 0, 5],
					[0, 7, 0, 3, 0, 0, 0, 1, 2],
					[1, 2, 0, 0, 0, 7, 4, 0, 0],
					[0, 4, 9, 2, 0, 6, 0, 0, 7]
				]
	if flag2 == 1:
		check_solution()
	if flag3 == 1:
		if solve(grid, 0, 0)== False:
			error = 1
		else:
			rs = 1
		flag3 = 0	
	if val != 0:		 
		draw_val(val)
		# print(x)
		# print(y)
		if valid(grid, int(x), int(y), val)== True:
			grid[int(x)][int(y)]= val
			flag1 = 0
		else:
			grid[int(x)][int(y)]= 0
			raise_error2() 
		val = 0

	if error == 1:
		raise_error1() 
	if rs == 1:
		result()	 
	draw() 
	if flag1 == 1:
		draw_box()	 
	instruction()
    		
    		
    			
	pygame.display.update() # cập nhật lại màn hình sau mỗi lần thay đổi
pygame.quit() # thoát khỏi chương trình