# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Protagonis")
define Rina = Character("Rina")
define Kanade = Character("Kanade")
define Mira = Character("Mira")

# definisikan gambar karakter
image rina = "rina/kisspng-gacha-resort-gacha-world-lunime-gacha-studio-anim-anime-gacha-5b627ce2d2a4d2.png"
image mira = "mira/anime-png-30700.png"

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
    "Di siang itu."

    "Aku sedang tidur siang di bawah pohon besar dekat pekarangan rumah."

    show rina

    Rina "Ngapain lu disitu?"

    Rina "Bangun uy! Dasar pemalas."
    
    "Rina. Gadis kota yang juga teman masa kecil ku saat masih SD."

    menu:

        "Mencoba bangun.":

            jump bangun

        "Mencoba tidur kembali.":

            jump tidur


    #menampilkan karakter

label bangun:

    e "Apaan sih. Gangguan orang tidur aja."

    Rina "Hihi... Dah siang masih aja molor. Sini bantuin aku gelar tikar di sini."

    e "Mau ngapain gelar tikar di sini?"

    Rina "Buat jualan.. Ya buat duduk lah, dasar ga peka!"

    Rina "Tidur kok nggak beralas tikar."

    e "Menyatu dengan alam itu juga bagian dari rasa syukur, Rin."

    Rina "Gitu aja terus"

    "Dan kami pun menikmati siang hari nan sejuk bersama."

    "{b}Good Ending{/b}."

    return  

label tidur:

    Rina "Dasar, pemalas!"

    "Dan si Rina pergi dan aku terlelap dengan mimpi indahku."

    "{b}Bad Ending{/b}."

    # This ends the game.

    return
