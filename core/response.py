import random

class Respond:
    @staticmethod
    def hai():
        rspnd = [
            "Hai 👋, Apa kabar?",
            "Apa kabar ? 😊",
            "Hey 🙌, senang bertemu denganmu!",
            "Hei, harimu menyenangkan kan? 😄",
            "Halo! Ada yang bisa aku bantu? 🤖",
            "Selamat datang! 🥳",
            "Wah, akhirnya kita ngobrol juga! 😁",
            "Kamu datang juga! Keren! 🚀",
            "Hai! Semangat terus ya! 💪",
            "Kamu luar biasa hari ini! ✨",
            "Aku senang kamu datang! 🫶",
            "Aku siap bantu kamu! 🔧",
            "Selamat datang kembali! 🔄",
            "Halo juga! Gimana kabarmu hari ini?",
            "Halo halo! Udah siap produktif?",
            "Yo bro/sis! Lagi sibuk apa nih?",
        ]
        return random.choice(rspnd)

    @staticmethod
    def motivasi():
        motivasi_list = [
            "Jangan pernah menyerah! 💪 Kesuksesan butuh proses.",
            "Kegagalan adalah bagian dari belajar 📚. Bangkit lagi ya!",
            "Hari ini mungkin sulit, tapi besok bisa jadi luar biasa 🌅",
            "Terus belajar dan berkarya! 🚀 Dunia menunggumu.",
            "Kamu hebat, kamu mampu, kamu bisa! 🔥",
            "Gagal itu biasa, yang penting jangan nyerah! 💯",
            "Mimpi besar dimulai dari langkah kecil ✨",
            "Setiap detik kamu belajar, kamu makin dekat ke impian 💡",
            "Tetap fokus, tetap semangat! 🔥 Kamu akan sampai ke tujuan!",
            "Kamu pencipta masa depanmu sendiri 🧠",
            "Hidup bukan tentang seberapa cepat kamu sampai, tapi seberapa konsisten kamu melangkah.",
            "Banyak orang pintar gagal karena menyerah terlalu cepat. Kamu jangan begitu ya!",
            "Waktu terbaik menanam pohon adalah 10 tahun lalu. Waktu terbaik kedua adalah sekarang 🌱",
            "Jangan bandingin dirimu dengan orang lain, bandingin dirimu hari ini dengan kemarin 💪",
            "Ayo wujudkan mimpi besarmu, mulai dari langkah kecil hari ini!"
        ]
        return random.choice(motivasi_list)

    @staticmethod
    def semangat():
        semangat_list = [
            "Semangat terus ya! 💪🔥",
            "Jangan kasih kendor! 💯",
            "Kamu bisaaa! 🚀",
            "Tetap kuat dan semangat 💥",
            "Ayo bangkit lagi, gas terus! 🏃‍♂️💨",
            "Kalau capek, istirahat ya. Tapi jangan menyerah 😎",
            "Semangatmu hari ini menentukan masa depanmu!",
            "Kamu udah sejauh ini, jangan balik arah sekarang!",
            "Gaskeun sampai finish line! 🏁",
            "Kerja kerasmu bakal kebayar suatu hari nanti. Yakinin itu!"
        ]
        return random.choice(semangat_list)

    @staticmethod
    def sedih():
        sedih_list = [
            "Gapapa kok kalau kamu lagi sedih 😢. Aku di sini.",
            "Semua akan baik-baik saja 🌈",
            "Kadang kita perlu hujan buat lihat pelangi 🌦️",
            "Kalau kamu butuh teman, aku siap dengerin 🤝",
            "Peluk virtual dulu ya 🤗",
            "Sedih itu wajar, jangan dipendam sendiri ya.",
            "Kamu nggak sendiri, aku di sini nemenin.",
            "Mungkin sekarang terasa berat, tapi kamu pasti bisa lewatin ini 💙",
            "Menangis bukan tanda lemah, itu tandanya kamu manusia 🌧️",
            "Ambil napas, tarik pelan, buang... Semua akan baik-baik aja."
        ]
        return random.choice(sedih_list)
    
    @staticmethod
    def kabar():
        kabar_list = [
            "Aku baik-baik saja, makasih sudah nanya! 😊",
            "Lagi semangat nih! Kamu gimana?",
            "Sedikit ngelag, tapi tetap semangat! 🤖⚡",
            "Aku selalu siap bantu kamu ✨",
            "Alhamdulillah, sehat! Kamu gimana?"
        ]
        return random.choice(kabar_list)

    @staticmethod
    def cuaca():
        cuaca_list = [
            "Kayaknya hari ini cerah ya! ☀️",
            "Bawa payung deh, siapa tahu hujan ☔",
            "Cuaca lagi mendung, cocok buat ngoding 😌",
            "Dingin banget ya hari ini 🥶",
            "Panasnya kayak oven! 🔥"
        ]
        return random.choice(cuaca_list)

    @staticmethod
    def ngapain():
        ngapain_list = [
            "Lagi nunggu kamu ngobrol sama aku 😁",
            "Aku sih standby terus buat bantu kamu 🤖",
            "Baru aja belajar bahasa manusia 😅",
            "Lagi mikirin cara jadi bot pintar kayak kamu 😜"
        ]
        return random.choice(ngapain_list)

    @staticmethod
    def makasih():
        return random.choice([
            "Sama-sama yaa 🤗",
            "Aku senang bisa bantu kamu! 😄",
            "Terima kasih kembali 🫶",
            "Kapan pun kamu butuh, aku di sini 😌"
        ])
