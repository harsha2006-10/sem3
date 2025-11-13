import time

song_data =[
    ("Meri aashiqui ab tum hi ho", 41.50),
    # --- Instrumental Break (42.00 - 1:04) ---
    ("Tera mera rishta hai kaisa", 105.00), # 1:45
    ("Ik pal door gawara nahi", 109.00), # 1:49
    ("Tere liye har roz hai jeete", 114.50), # 1:54.5
    ("Tujhko diya mera waqt sabhi", 118.50), # 1:58.5
    ("Koi lamha mera na ho tere bina", 123.00), # 2:03.0
    ("Har saans pe naam tera", 127.00), # 2:07.0
    ("Kyunki tum hi ho", 131.00), # 2:11.0
    ("Ab tum hi ho", 133.50), # 2:13.5
    ("Zindagi ab tum hi ho", 136.50), # 2:16.5
    ("Chain bhi, mera dard bhi", 140.00), # 2:20.0
    ("Meri aashiqui ab tum hi ho", 142.50), # 2:22.5
    # --- Bridge/Interlude (2:23 - 2:42) ---
    ("Tere liye hi jiyaa main", 163.00), # 2:43.0
    ("Khud ko jo yun de diya hai", 166.50), # 2:46.5
    ("Teri wafaa ne mujhko sambhala", 172.00), # 2:52.0
    ("Saare ghamon ko dil se nikala", 176.50), # 2:56.5
    ("Tere saath mera hai naseeb judaa", 181.00), # 3:01.0
    ("Tujhe paake adhoora naa raha... Hmm...", 185.00), # 3:05.0
    ("Kyunki tum hi ho", 206.00), # 3:26.0
    ("Ab tum hi ho", 208.50), # 3:28.5
    ("Zindagi ab tum hi ho", 211.50), # 3:31.5
    ("Chain bhi, mera dard bhi", 215.00), # 3:35.0
    ("Meri aashiqui ab tum hi ho", 217.50), # 3:37.5
    # --- Final Instrumental/Fade Out (3:38 - 4:22) ---
    ("Tum Hi Ho...", 260.00) # Final fade around 4:20
]

print("Starting song lyrics display...")

for i in range(1, len(song_data)):
    current_lyric, current_time = song_data[i]
    _, prev_time = song_data[i-1]

    time_to_wait = current_time - prev_time
    time.sleep(time_to_wait)
    
    print(current_lyric)

print("Song ended.")
