import simpleaudio as sa
import time

print("To jest program Pomodoro. \nPierwszy dźwięk ma zachęcać do wypicia szklanki wody, \
a drugi zaprasza do dalszej pracy.")
total_breaks = input("Ile jednostek Pomodoro? ")
total_breaks = int(total_breaks)
breaks_count = 0

print("Ten program zaczyna się o " + time.ctime())
while True:
    time.sleep(1500)
    wave_obj = sa.WaveObject.from_wave_file("C:\\Users\\Magda\\Desktop\\simple\\nalewanie_wody.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    time.sleep(300)
    wave_obj1 = sa.WaveObject.from_wave_file("C:\\Users\\Magda\\Desktop\\simple\\pisanie.wav")
    play_obj1 = wave_obj1.play()
    play_obj1.wait_done()
    breaks_count += 1
    if breaks_count >= total_breaks:
        break