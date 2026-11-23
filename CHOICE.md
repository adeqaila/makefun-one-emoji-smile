# Pemilihan emoji — One Emoji, One Smile (slot 1)

**Pilihan: ☺️ (U+263A + U+FE0F, "Smiling Face")** — senyum lembut berpipi
merona, mata tersenyum tertutup.

## Fakta bounty (dari kit resmi + API)

- Metric: Judge win rate — juri GLM-5.3-flash membandingkan 2 emoji sekaligus,
  memilih yang lebih hangat, margin 1–5, tiap pasangan di kedua urutan.
- Gate: `/output/entry.txt` UTF-8, 1–8 karakter, bukan hanya whitespace.
- Blind rounds: tidak ada skor/rank terlihat. Ronde 1 cutoff 24 Nov 19:30 UTC;
  deadline 26 Nov 19:30 UTC. Top 500 dev board masuk final heat — dengan
  ~70 entry, praktis semua yang valid masuk final, jadi yang menentukan
  hanyalah menang pairwise melawan field.
- 3 fixed house texts (anchor/rung) disegel; entry yang byte-identik dengan
  salah satunya tidak dapat hadiah (rung) / tidak masuk playoff (anchor).
  ☺️ bukan pilihan kalibrasi yang paling kanonis (🙂/😊/🤗 lebih mungkin),
  jadi risiko ini kecil — tapi tetap ada untuk pilihan apa pun.
- Hadiah total $5; juara 1 $1,54. Nilai ekspektasi kecil — build ini murah
  (satu file, tanpa network) dan slot 1 tidak mengorbankan apa pun.

## Pola field (70 submission, dari judul entry di API — sumber tertahan)

Klaster yang sudah ramai (salinan byte-identik berbagi satu rate; yang
diterima lebih dulu menempati tempat di atas salinannya):

| Emoji | Perkiraan jumlah | Catatan |
|---|---|---|
| 🤗 Hugging Face | ~10+ | klaster terbesar |
| 🫶 Heart Hands | ~8 | |
| 🌻 Sunflower | ~8 | |
| 🌞 Sun with Face | ~8 | |
| 😊 Smiling Face w/ Smiling Eyes | ≥2 | |
| 😁 / 😄 Beaming/Grinning | ~2 | "Beaming Face", "Grinning Face With Smiling Eyes" |
| 😇 Halo | 1 | |
| 🙂 Slightly Smiling | 1 | "White Smiling Face" |
| 🥹 Holding Back Tears | 1 | |
| 🫂 People Hugging | 1 | |
| ~11 judul generik | ? | emoji tidak diketahui |

Kesimpulan pola: field sudah konvergen ke 4 ide yang sama. Masuk ke klaster
itu = duduk di belakang ~8 salinan yang lebih dulu. Pemenang harus emoji
yang (a) tidak ada di klaster besar, (b) mengalahkan mereka di kriteria
juri.

## Simulasi judge (pairwise, mengikuti brief resmi, kedua urutan)

Kriteria brief, berurutan: (1) hangat/ramah, jelas bertujuan menghangatkan
orang asing; (2) hangat pada pandangan pertama; (3) universal; (4) terasa
dipilih, bukan smiley pertama yang terlintas, tetap langsung terbaca;
(5) pantas dari orang asing (tanpa intimasi/sarkasme/flirtasi).

| Lawan | Hasil untuk ☺️ | Alasan penentu |
|---|---|---|
| 🤗 | Menang, margin 2 | Kriteria 5: pelukan dari orang asing = kontak fisik yang intim/aneh; senyum adalah sapaan yang tepat |
| 🫶 | Menang, margin 1–2 | Kriteria 3: senyum dibaca sama di semua usia; gestur heart-hands tidak seuniversal itu |
| 🌻 | Menang, margin 3–4 | Kriteria 1: bunga tidak "bertujuan menghangatkan orang asing"; senyum iya |
| 🌞 | Menang, margin 2 | Kriteria 1: wajah manusia yang tersenyum lebih langsung hangat daripada simbol matahari |
| 😊 | Menang, margin 1 | Kriteria 4: 😊 ADALAH smiley pertama yang terlintas; ☺️ selangkah lebih dipilih, sama terbacanya |
| 😇 | Menang, margin 1–2 | Kriteria 3: halo menambah lapisan (suci/sok suci) yang tidak semua orang baca sama |
| 🙂 | Menang, margin 2–3 | Kriteria 1+4: senyum "sedikit" kurang hangat dan 🙂 adalah smiley default |
| 😁 | Menang, margin 1 | Kriteria 4: seringai lebar adalah default yang umum; ☺️ terasa lebih dipilih. Ini lawan terdekat kedua |
| 😃 | Menang, margin 1 | Kriteria 4: senyum mulut terbuka adalah default yang umum |
| 😀 | Menang, margin 2 | Kriteria 1+4: seringai paling default, kurang lembut/hangat |
| 🥹 | Menang, margin 3 | Kriteria 1: menahan tangis itu pahit-manis, bukan hangat |
| 🫂 | Menang, margin 2 | Kriteria 5: pelukan dua orang dari orang asing = intimasi |
| 💛 | Menang, margin 2 | Kriteria 1: hati adalah simbol kehangatan, bukan wajah yang menghangatkan |
| 👋 | Menang, margin 2 | Kriteria 1: lambaian adalah sapaan, bukan kehangatan |
| 😺 | Menang, margin 1–2 | Kriteria 1: kucing itu lucu/menggemaskan, tapi wajah manusia yang tersenyum lebih jelas bertujuan menghangatkan |

Tidak ada matchup yang kalah dalam simulasi ini. Lawan terdekat: 😊, 😁, 😃
(margin 1, diputuskan kriteria 4). Catatan jujur: simulasi ini dilakukan
oleh builder (bukan juri GLM-5.3-flash asli) — ini penilaian beralasan,
bukan jaminan. Yang solid: ☺️ tidak bergabung dengan klaster mana pun,
lolos semua kriteria tanpa kelemahan, dan kriteria 4 (yang ditulis juri
untuk membedakan "dipilih" vs "default") justru memihaknya melawan
saingan terdekatnya.

## Verifikasi lokal

- `python3 main.py` → `/output/entry.txt` = `E2 98 BA EF B8 8F`
  (U+263A U+FE0F), 2 karakter, 6 byte, gate OK.
- Dua run berurutan: sha256 identik
  `bed682d04764314c8c2ed0743b6c6a0eb7152bced2b519e71c29a839b3ff0d30`.
- Tanpa network, tanpa env, tanpa randomness.
