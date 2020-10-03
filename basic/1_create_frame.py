import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Camon Game")

# 이벤트 루프
running = True  # 게임이 진행중인가?

while running:
    for event in pygame.event.get():
        # 창 닫기 버튼 이벤트 발생
        if event.type == pygame.QUIT:
            running = False

# pygame 종료
pygame.quit()