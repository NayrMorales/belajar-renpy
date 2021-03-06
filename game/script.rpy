﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("RNDang")
define Kanade = Character("Rina")

# definisikan gambar karakter
image kanade = "rina/kisspng-gacha-resort-gacha-world-lunime-gacha-studio-anim-anime-gacha-5b627ce2d2a4d2.png"

#definiskan gambar background
image BGroom = "bg/bg1.png"

# The game starts here.

# menjalankan splash screen sebelum masuk menu
label splashscreen:
    scene black
    with Pause(1)

    show text "Jogja Bishoujo Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

#script jalannya game dimulai
label start:

    stop music

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #menampilan gambar bakcground
    scene BGroom

    #menampilkan text sesuai karakter
    e "Hallo World!"

    e "Kita baru saja mencoba mengubah bar story."
    
    e "Next, kita coba tampilkan gambar protagonis nya."

    #menampilkan karakter
    show kanade

    Kanade "Hallo dunia!"

    e "Dah muncul tuh gambarnya"

    e "Sampai jumpa!"

    # This ends the game.

    return
