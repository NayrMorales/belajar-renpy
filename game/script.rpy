# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Kanade")

# definisikan gambar karakter
image kanade = "kanade/random_girl.png"

#definiskan gambar background
image BGroom = "bg/bg1.png"

# The game starts here.

# menjalankan splash screen sebelum masuk menu
label splashscreen:
    scene black
    with Pause(1)

    show text "American Bishoujo Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

#script jalannya game dimulai
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #menampilan gambar bakcground
    scene BGroom room

    #menampilkan text sesuai karakter
    e "Hallo World!"

    e "Kita baru saja mencoba mengubah bar story."
    
    e "Next, kita coba ganti gambar protagonis nya."

    #menampilkan karakter
    show kanade

    e "Dah muncul tuh gambarnya"

    e "Sampai jumpa!"

    # This ends the game.

    return
