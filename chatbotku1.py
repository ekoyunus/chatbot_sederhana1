import streamlit as st

# Pengetahuan chatbot tentang kegiatan 17 Agustus di sekolah
knowledge_base = [
    "Upacara bendera dilaksanakan pukul 07.00 di lapangan sekolah.",
    "Peserta upacara wajib mengenakan seragam putih merah.",
    "Lomba balap karung diadakan setelah upacara bendera.",
    "Lomba makan kerupuk diikuti oleh siswa kelas 1-6.",
    "Lomba tarik tambang diikuti oleh guru dan siswa.",
    "Pendaftaran lomba dilakukan di ruang OSIS.",
    "Hadiah lomba berupa piala dan bingkisan menarik.",
    "Panitia lomba terdiri dari guru dan OSIS.",
    "Peserta lomba wajib mendaftar sebelum tanggal 15 Agustus.",
    "Lomba kelereng diadakan untuk siswa kelas 1-3.",
    "Lomba lari estafet diadakan untuk siswa kelas 4-6.",
    "Setiap kelas wajib mengirimkan perwakilan lomba.",
    "Upacara dipimpin oleh kepala sekolah.",
    "Petugas pengibar bendera dipilih dari siswa berprestasi.",
    "Setelah lomba, diadakan makan bersama di aula sekolah.",
    "Orangtua siswa diundang untuk menghadiri upacara dan lomba.",
    "MC acara lomba adalah guru olahraga.",
    "Lomba memasukkan paku ke botol diadakan untuk kelas 4-6.",
    "Lomba membawa kelereng dengan sendok diadakan untuk kelas 1-3.",
    "Setiap pemenang lomba akan diumumkan di akhir acara.",
    "Upacara bendera diiringi lagu Indonesia Raya.",
    "Siswa yang terlambat tidak diperbolehkan mengikuti lomba.",
    "Panitia menyediakan air minum gratis untuk peserta lomba.",
    "Lomba balap karung menggunakan karung yang disediakan panitia.",
    "Lomba makan kerupuk dilakukan tanpa menggunakan tangan.",
    "Peserta lomba wajib menjaga sportivitas dan keamanan.",
    "Setiap kelas membuat yel-yel untuk mendukung timnya.",
    "Guru bertugas sebagai juri lomba.",
    "Acara ditutup dengan pembagian hadiah dan foto bersama.",
    "Siswa yang berprestasi di lomba akan mendapat sertifikat.",
    "Lomba estafet dilakukan secara berkelompok.",
    "Lomba tarik tambang dilakukan di lapangan belakang sekolah.",
    "Peserta lomba wajib memakai sepatu olahraga.",
    "Upacara bendera wajib diikuti oleh seluruh warga sekolah.",
    "Lomba kreatifitas menghias kelas juga diadakan.",
    "Penilaian lomba kreatifitas dilakukan oleh dewan guru.",
    "Acara 17 Agustus bertujuan menumbuhkan semangat kebangsaan.",
    "Dokumentasi acara dilakukan oleh tim multimedia sekolah.",
    "Setiap kelas wajib menjaga kebersihan selama acara berlangsung."
]

def chatbot_response(user_input):
    user_input = user_input.lower()
    for info in knowledge_base:
        if any(word in info.lower() for word in user_input.split()):
            return info
    return "Maaf, informasi yang Anda cari belum tersedia. Silakan tanyakan hal lain seputar kegiatan 17 Agustus di sekolah."

st.title("Chatbot Kegiatan 17 Agustus di Sekolah")
st.write("Tanyakan apa saja seputar lomba, upacara, dan kegiatan 17 Agustus di sekolah!")

user_question = st.text_input("Masukkan pertanyaan Anda:")

if user_question:
    response = chatbot_response(user_question)
    st.success(response)
