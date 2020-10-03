import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Camon Game")

# 배경 이미지 불러오기
background = pygame.image.load('background.png')

# 이벤트 루프
running = True  # 게임이 진행중인가?

while running:
    for event in pygame.event.get():
        # 창 닫기 버튼 이벤트 발생
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((0, 255, 0)) # RGB 코드로 배경 칠하기
    screen.blit(background, (0, 0))  # 배경 그리기
    pygame.display.update()  # 게임 화면 다시 그리기

# pygame 종료
pygame.quit()
