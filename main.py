from pprint import pprint
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('punkt')
reviews = [
    "Bulan adalah satelit alami Bumi satu-satunya dan merupakan satelit terbesar kelima dalam Tata Surya",
    "Bulan juga merupakan satelit alami terbesar di Tata Surya menurut ukuran planet yang diorbitnya dengan diameter 27%  kepadatan 60%  dan massa 1⁄81 (1.23%) dari Bumi",
    "Di antara satelit alami lainnya Bulan adalah satelit terpadat kedua setelah Io satelit Jupiter",
    "Bulan berada pada rotasi sinkron dengan Bumi yang selalu memperlihatkan sisi yang sama pada Bumi dengan sisi dekat ditandai oleh mare vulkanik gelap yang terdapat di antara dataran tinggi kerak yang terang dan kawah tubrukan yang menonjol",
    "Bulan adalah benda langit yang paling terang setelah Matahari",
]


stop_words = set(stopwords.words("indonesian"))


# tokenizing
word_tokens = []
for review in reviews:
    word_tokens.append(word_tokenize(review))
# pprint(word_tokens)

# case folding
casefolded_sentence = []
for word_token in word_tokens:
    casefolded_sentence.append([word.casefold() for word in word_token])
# pprint(casefolded_sentence)

# stop word removal
filtered_sentence = []
for sent in casefolded_sentence:
    filtered_sentence.append([word for word in sent if not word in stop_words])
# pprint(filtered_sentence)

# stemming sastrawi
stemmer = StemmerFactory().create_stemmer()
stemmed_sentence = []
for review in reviews:
    stemmed_sentence.append(stemmer.stem(review).split(" "))
pprint(stemmed_sentence)


# stemming nltk
# ps = PorterStemmer()
# sentence = "Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth. It has only one-eighth the average density of Earth, but is over 95 times more massive. Saturn's interior is most likely composed of a rocky core, surrounded by a deep layer of metallic hydrogen, an intermediate layer of liquid hydrogen and liquid helium, and finally, a gaseous outer layer. Saturn has a pale yellow hue due to ammonia crystals in its upper atmosphere."
# sentence = "Bulan adalah satelit alami Bumi satu-satunya dan merupakan satelit terbesar kelima dalam Tata Surya. Bulan juga merupakan satelit alami terbesar di Tata Surya menurut ukuran planet yang diorbitnya dengan diameter 27%  kepadatan 60%  dan massa 1⁄81 (1.23%) dari Bumi. Di antara satelit alami lainnya Bulan adalah satelit terpadat kedua setelah Io satelit Jupiter. Bulan berada pada rotasi sinkron dengan Bumi yang selalu memperlihatkan sisi yang sama pada Bumi dengan sisi dekat ditandai oleh mare vulkanik gelap yang terdapat di antara dataran tinggi kerak yang terang dan kawah tubrukan yang menonjol. Bulan adalah benda langit yang paling terang setelah Matahari"
# words = word_tokenize(sentence)
# for w in words:
#  print(w, " : ", ps.stem(w))
