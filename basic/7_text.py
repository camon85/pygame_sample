import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Camon Game")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load('background.png')

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load('character.png')
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - character_width / 2  # 화면 중앙에 위치
character_y_pos = screen_height - character_height  # 화면 가장 아래에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 캐릭터
enemy = pygame.image.load('enemy.png')
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]  # 캐릭터의 가로 크기
enemy_height = enemy_size[1]  # 캐릭터의 세로 크기
enemy_x_pos = screen_width / 2 - enemy_width / 2  # 화면 중앙에 위치
enemy_y_pos = screen_height / 2 - enemy_height / 2  # 화면 가장 아래에 위치

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트  크기

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()  # 현재 tick 을 받아옴

# 이벤트 루프
running = True  # 게임이 진행중인가?

while running:
    dt = clock.tick(60)  # 게임 화면의 초당 프레임 수를 설정
    # print("fps: " + str(clock.get_fps()))
    for event in pygame.event.get():
        # 창 닫기 버튼 이벤트 발생
        if event.type == pygame.QUIT:
            running = False  # 게임이 진행중이 아님

        # 키가 눌러졌는지 확인
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로로
                to_x += character_speed
            elif event.key == pygame.K_UP:  # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                to_y += character_speed

        # 방향키를 떼면 멈춤
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌 했어요")
        running = False

    # 배경 그리기
    screen.blit(background, (0, 0))

    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    # 적 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 경과 시간 계산 1000으로 나누어 초 단위로 표시
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    # 출력할 글자, 안티엘리어싱 True, 글자 색상
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))

    screen.blit(timer, (10, 10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False
        
    # 게임 화면 다시 그리기
    pygame.display.update()

# 잠시 대기
pygame.time.delay(2000)

# pygame 종료
pygame.quit()
