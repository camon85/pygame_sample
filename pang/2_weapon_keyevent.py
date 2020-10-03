import os
import pygame

##########################################################################
# 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Camon Pang")

# FPS
clock = pygame.time.Clock()
##########################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__)  # 현재 파일의 위치
image_path = os.path.join(current_path, 'images')  # 이미지 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, 'background.png'))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, 'stage.png'))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, 'character.png'))
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - character_width / 2  # 화면 중앙에 위치
character_y_pos = screen_height - character_height - stage_height  # 화면 가장 아래에 위치

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, 'weapon.png'))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트  크기

# 총 시간
total_time = 99

# 시작 시간
start_ticks = pygame.time.get_ticks()  # 현재 tick 을 받아옴

# 이벤트 루프
running = True  # 게임이 진행중인가?

while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        # 창 닫기 버튼 이벤트 발생
        if event.type == pygame.QUIT:
            running = False  # 게임이 진행중이 아님

        # 키가 눌러졌는지 확인
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:  # 무기 발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        # 방향키를 떼면 멈춤
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    # 무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]  # 무기 위치를 위로 올림

    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))  # 배경

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))  # 무기

    screen.blit(stage, (0, screen_height - stage_height))  # 스테이지
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터

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
