# Chapter files extracted from https://ebible.org/Scriptures/eng-kjv_readaloud.zip

# Above link and the following copyright information are from:
#   https://ebible.org/find/show.php?id=eng-kjv
"""

King James Version + Apocrypha
The King James Version or Authorized Version of the Holy Bible, using the standardized text of 1769, with Apocrypha/Deuterocanon
Public Domain
Language: English
Dialect: archaic British

Letters patent issued by King James with no expiration date means that to print this translation in the United Kingdom or import printed copies into the UK, you need permission. Currently, the Cambridge University Press, the Oxford University Press, and Collins have the exclusive right to print this Bible translation in the UK. This royal decree has no effect outside of the UK, where this work is firmly in the Public Domain. Please see http://www.cambridge.org/about-us/who-we-are/queens-printers-patent and https://en.wikipedia.org/wiki/King_James_Version#Copyright_status for more information. This free text of the King James Version of the Holy Bible is brought to you courtesy of the Crosswire Bible Society and eBible.org.


2018-08-27

"""

import os.path
import glob
import json
import re


def main():
    def value__key(element):
        sort_key = (element[1], element[0])
        return sort_key

    script_dir = os.path.dirname(os.path.realpath(__file__))
    source_files = os.path.join(script_dir, "downloads", "kjv_chapter_files")

    book_abbrevs = {}
    verse_counts_by_count = {}  # dict of full_refs, indexed by verse counts
    verse_counts_by_desc_count = {}  # above dict, sorted by decreasing verse count
    verse_counts_by_chapter = {}  # dict of verse counts, indexed by chapter
    # e.g., dict["Gen 1"]=31

    kjv_chapter_files = sorted(glob.glob(os.path.join(source_files, "*.txt")))
    # sorted() because glob() may return the list in an arbitrary order

    word_frequency = {}
    for chapter_file in kjv_chapter_files:
        read_file = open(chapter_file, "r", encoding="utf-8")
        lines = read_file.readlines()
        full_book_name = lines[0][1:]  # Strip off unwanted initial Unicode character
        verse_count = len(lines) - 2  # Exclude lines[0] and lines [1]
        # No need to exclude the blank line at the end of chapter files,
        # since readlines() already seems to ignore it.

        for line in lines[2:]:
            line = re.sub("[¶’]\S*", "", line).strip()
            # Eliminate paragraph markers, possessives, and leading/trailing blanks
            words = re.sub("[^a-z\- ]+", "", line, flags=re.IGNORECASE)
            for word in words.split():
                word_lower = word.lower()
                if word_lower in word_frequency:
                    word_frequency[word_lower] += 1
                else:
                    word_frequency[word_lower] = 1

        book_number_name_chapter = os.path.basename(chapter_file)[9:-9]
        # basename is, for example, eng-kjv_002_GEN_01_read.txt
        book_number = int(book_number_name_chapter[0:2]) - 1
        # Sets the book number for 'eng-kjv_002_GEN_01_read.txt' to 1
        # Sets the book number for 'eng-kjv_070_MAT_01_read.txt' to 69
        if book_number >= 40:
            book_number -= 29
        # Sets the book number for 'eng-kjv_070_MAT_01_read.txt' to (70 - 1) - 29 = 40
        book_abbr = book_number_name_chapter[3:6].title()  # Gen, Exo, ..., Rev
        if book_abbr not in book_abbrevs:
            book_abbrevs[book_abbr] = full_book_name
        chapter_number = book_number_name_chapter[7:10].lstrip("0").rstrip("_")
        # Filenames normally contain 2-digit chapter numbers, but have 3 for Psalms
        # Remove leading '0's (as from '01' and '001') and trailing '_'s (as from '01_')
        # print(f'Book number: {book_number}, abbr: {book_abbr}, chapter: {chapter_number}')

        # print(
        #     f"{book_number_name_chapter}",
        #     f"{lines[0].strip()[3:-1]}, {lines[1].strip()[0:-1]}: {verse_count} verses",
        # )
        # As in: 002_GEN_01 The First Book of Moses, called Genesis Chapter 1: 31 verses

        full_ref = book_abbr + " " + chapter_number
        if verse_count in verse_counts_by_count:
            verse_counts_by_count[verse_count].append(full_ref)
        else:
            verse_counts_by_count[verse_count] = [full_ref]

        verse_counts_by_chapter[full_ref] = verse_count

    print("\n")
    total_words = 0
    words_with_this_frequency = []
    word_frequency_lists = {}
    previous_occurrences = 0
    occurrences = 0
    for element in sorted(word_frequency.items(), key=value__key):
        # Split into lists of words for each frequency:
        word = element[0]
        occurrences = element[1]  # For "the", occurrences is 64016
        total_words += occurrences
        if previous_occurrences and occurrences != previous_occurrences:
            word_frequency_lists[previous_occurrences] = words_with_this_frequency[:]
            words_with_this_frequency.clear()
        words_with_this_frequency.append(word)
        previous_occurrences = occurrences
    word_frequency_lists[occurrences] = words_with_this_frequency[:]
    word_frequency_lists[total_words] = ["TOTAL WORDS"]

    # TODO: When looping through the dictionary, add up the number of words
    #       and compare to the entry for "TOTAL WORDS"

    word_frequency_lists_reversed = {}
    for key, value in sorted(word_frequency_lists.items(), reverse=True):
        word_frequency_lists_reversed[key] = value

    with open(r"BibleMetaData\book_abbreviations.json", "w") as write_file:
        json.dump(book_abbrevs, write_file, indent=4)

    for verse_count, full_refs in sorted(verse_counts_by_count.items(), reverse=True):
        verse_counts_by_desc_count[verse_count] = full_refs
    with open(r"BibleMetaData\verse_counts_by_desc_count.json", "w") as write_file:
        json.dump(verse_counts_by_desc_count, write_file, indent=4)

    with open(r"BibleMetaData\verse_counts_by_chapter.json", "w") as write_file:
        json.dump(verse_counts_by_chapter, write_file, indent=4)

    with open(r"BibleMetaData\word_frequency_lists.json", "w") as write_file:
        json.dump(word_frequency_lists_reversed, write_file, indent=4)


if __name__ == "__main__":
    main()
