def changeformat():
    import subprocess
    import os
    from pydub import AudioSegment
    from pydub.playback import play
    path=r"D:\视频素材\音乐\Take Me To Your Heart.mp3"
    FFMPEG_PATH = r"D:\PYTHON\ffmpeg\bin\ffmpeg.exe"
    FFPLAY_PATH = r"D:\PYTHON\ffmpeg\bin\ffplay.exe"
    AudioSegment.converter = FFMPEG_PATH
    AudioSegment.ffmpeg = FFMPEG_PATH
    AudioSegment.ffplay = FFPLAY_PATH
    tempd='./tmp_music'
    os.makedirs(tempd,exist_ok=True )
    new=AudioSegment.from_file(path)
    subprocess.run([
        FFPLAY_PATH,
        "-autoexit",
        # "-nodisp",
        path
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output_wav=os.path.join(tempd,'bg_tmtyh.ogg')
    new.export(output_wav,format="ogg")
if __name__=="__main__":
    changeformat()


from pygame.locals import *
def palymusic():
    import pygame
    import sys
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load(r"D:\pycharm\tmp_music\bg_tmtyh.ogg")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()
    sd1 = pygame.mixer.Sound(r"D:\pycharm\tmp_music\soud.ogg")
    sd1.set_volume(0.1)
    sd2 = pygame.mixer.Sound(r"D:\pycharm\tmp_music\newnice.wav")
    sd2.set_volume(0.1)

    bg_size = width, height = 600, 300
    win = pygame.display.set_mode(bg_size)
    pygame.display.set_caption('Music qlok Taco')

    pause = False

    pause_image = pygame.image.load(r"D:\pycharm\tmp_music\zt.png")
    play_image = pygame.image.load(r"D:\pycharm\tmp_music\bf.png")
    pause_rect = pause_image.get_rect()
    pause_rect.left, pause_rect.top = (width - pause_rect.width) // 2, (height - pause_rect.height) // 2

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    sd1.play()
                if event.button == 3:
                    sd2.play()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pause = not pause
        win.fill((255, 255, 255))

        if pause:
            win.blit(pause_image, pause_rect)
            pygame.mixer.music.pause()
        else:
            win.blit(play_image, pause_rect)
            pygame.mixer.music.unpause()
        pygame.display.update()
        clock.tick(60)
palymusic()
