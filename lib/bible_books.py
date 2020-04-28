import json
import os

bible_books = {
    "Genesis": ("Gen", 50),
    "Exodus": ("Exo", 40),
    "Leviticus": ("Lev", 27),
    "Numbers": ("Num", 36),
    "Deuteronomy": ("Deu", 34),
    "Joshua": ("Jos", 24),
    "Judges": ("Jdg", 21),
    "Ruth": ("Rut", 4),
    "1 Samuel": ("1Sa", 31),
    "2 Samuel": ("2Sa", 24),
    "1 Kings": ("1Ki", 22),
    "2 Kings": ("2Ki", 25),
    "1 Chronicles": ("1Ch", 29),
    "2 Chronicles": ("2Ch", 36),
    "Ezra": ("Ezr", 10),
    "Nehemiah": ("Neh", 13),
    "Esther": ("Est", 10),
    "Job": ("Job", 42),
    "Psalms": ("Psa", 150),
    "Proverbs": ("Pro", 31),
    "Ecclesiastes": ("Ecc", 12),
    "SongOfSolomon": ("Sng", 8),
    "Isaiah": ("Isa", 66),
    "Jeremiah": ("Jer", 52),
    "Lamentations": ("Lam", 5),
    "Ezekiel": ("Ezk", 48),
    "Daniel": ("Dan", 12),
    "Hosea": ("Hos", 14),
    "Joel": ("Jol", 3),
    "Amos": ("Amo", 9),
    "Obadiah": ("Oba", 1),
    "Jonah": ("Jon", 4),
    "Micah": ("Mic", 7),
    "Nahum": ("Nam", 3),
    "Habakkuk": ("Hab", 3),
    "Zephaniah": ("Zep", 3),
    "Haggai": ("Hag", 2),
    "Zechariah": ("Zec", 14),
    "Malachi": ("Mal", 4),
    "Matthew": ("Mat", 28),
    "Mark": ("Mrk", 16),
    "Luke": ("Luk", 24),
    "John": ("Jhn", 21),
    "Acts": ("Act", 28),
    "Romans": ("Rom", 16),
    "1 Corinthians": ("1Co", 16),
    "2 Corinthians": ("2Co", 13),
    "Galatians": ("Gal", 6),
    "Ephesians": ("Eph", 6),
    "Philippians": ("Php", 4),
    "Colossians": ("Col", 4),
    "1 Thessalonians": ("1Th", 5),
    "2 Thessalonians": ("2Th", 3),
    "1 Timothy": ("1Ti", 6),
    "2 Timothy": ("2Ti", 4),
    "Titus": ("Tit", 3),
    "Philemon": ("Phm", 1),
    "Hebrews": ("Heb", 13),
    "James": ("Jas", 5),
    "1 Peter": ("1Pe", 5),
    "2 Peter": ("2Pe", 3),
    "1 John": ("1Jn", 5),
    "2 John": ("2Jn", 1),
    "3 John": ("3Jn", 1),
    "Jude": ("Jud", 1),
    "Revelation": ("Rev", 22),
}


def main():
    bible_metadata_folder = os.path.join(os.getcwd(), "BibleMetaData")
    with open(
        os.path.join(bible_metadata_folder, r"bible_books.json"), "w"
    ) as write_file:
        json.dump(bible_books, write_file, indent=4)


if __name__ == "__main__":
    main()
