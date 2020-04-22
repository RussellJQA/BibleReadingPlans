import string

# TODO: Add a master index page
# TODO: Add favicon

head = string.Template(
    """
<head>
    <meta charset="UTF-8">
    <meta name='description' content='eBEREAN: electronic Bible Exploration REsources and ANalysis.'> 
    <meta name='date' content='2020-04-20'> 
    <meta name='last-modified' content='2020-04-20'>     
    <meta name='language' content='english' >
    <meta name='author' content='Russell Johnson (RussellJ.heliohost.org)' >
    <meta name='copyright' content="2020 Russell Johnson. All rights reserved." >
    <meta name='generator' content="HTML">
    <meta property="og:site_name" content="RussellJ"> 
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$title</title>
     <!-- The table styling in this style tag is from https://www.w3schools.com/html/html_tables.asp -->
    <style>
        table,
        th,
        td {
            border: 1px solid black;
        }

        th,
        td {
            padding: 15px;
        }

        .integer {
            text-align: right;
        }

        footer {
            text-align: center
        }
    </style>
</head>
"""
)

header = string.Template(
    """
    <header class='page' role='banner'>
        <h1>$h1</h1>
    </header>"""
)

main_start = string.Template(
    """
    <main id='main_content'  class='page' class='page' role='main' tabindex='-1'>
        <h2>$h2</h2>
        
        <p>
            The columns in the sortable table below are:
            <ul>
                <li>Word:		A word which occurs in this chapter of the KJV Bible</li>
                <li>In chapter:	The number of occurrences of that word in this chapter of the KJV</li>
                <li>In KJV:		The number of occurrences of that word in the entire KJV</li>
                <li>Weighted:	The weighted relative frequency of that word in this chapter of the KJV</li>
                <li>Simple:		The simple relative frequency of that word in this chapter of the KJV</li>
            </ul>
            (See TBD for further explanation of both types of relative frequency.)
        </p>

"""
)

table_start = """
        <!-- Table sorting uses the following script, as explained at
        https://stackoverflow.com/questions/10683712/html-table-sort/51648529 -->
        <script src="https://www.kryogenix.org/code/browser/sorttable/sorttable.js"></script>

        <!-- Prototype table generated using http://convertcsv.com/csv-to-html.htm -->

        <!-- I removed the Bootstrap classes and align attributes from the generated table. -->
        <!-- <table class="table table-bordered table-hover table-condensed"> -->
        <table class="sortable">
            <thead>
                <tr>
                    <th title="Field #1">Word</th>
                    <th title="Field #2">In chapter</th>
                    <th title="Field #3">In KJV</th>
                    <th title="Field #4">Weighted Relative Frequency</th>
                    <th title="Field #4">Simple Relative Frequency</th>
                </tr>
            </thead>
            <tbody>"""

table_row = string.Template(
    """
                <tr>
                    <td>$word</td>
                    <td class='integer'>$numInChap</td>
                    <td class='integer'>$numInKjv</td>
                    <td>$weightedRelFreq</td>
                    <td>$simpleRelFreq</td>
                </tr>"""
)

table_end = """
            </tbody>
        </table>
"""

footer = """
    <footer class='page' role='contentinfo'><p>Copyright &copy; 2020 by Russell Johnson</p></footer>
"""


def get_main_tag(words_in_bible, key, relative_word_frequency):

    main_tag = ""

    words_in_chapter = "{:,}".format(relative_word_frequency["TOTAL WORDS"][0])
    words_in_bible_formatted = "{:,}".format(words_in_bible)
    #   Include thousands separators
    values = {
        "h2": f"{words_in_chapter} word occurrences in {key} in the KJV ({words_in_bible_formatted} word occurrences in the entire KJV):",
    }
    main_tag += main_start.substitute(values)

    main_tag += table_start
    for count, chapter_word_freq_key in enumerate(relative_word_frequency):
        if count:  # Table row data
            values = relative_word_frequency[chapter_word_freq_key]
            # Include thousands separators, where needed
            table_row_values = {
                "word": chapter_word_freq_key,
                "numInChap": values[0],
                "numInKjv": ("{:,}".format(values[1])),
                "weightedRelFreq": values[2],
                "simpleRelFreq": ("{:,}".format(values[3])),
            }
            main_tag += table_row.substitute(table_row_values)
    main_tag += table_end

    main_tag += "    </main>"  # Closing <main> tag

    return main_tag


def write_html_file(html_fn, title_h1, main_tag):

    with open(html_fn, "w") as write_file:

        write_file.write("<!doctype html>")
        write_file.write("<html lang='en'>")

        write_file.write(head.substitute({"title": title_h1}))  # Write <head> tag

        write_file.write("<body>")  # Write start of <body> tag
        write_file.write(header.substitute({"h1": title_h1}))
        write_file.write(main_tag)  #   Write <main> tag
        write_file.write(footer)
        write_file.write("</body>\n\n")  # Write end of <body> tag

        write_file.write("</html>")


def main():
    pass


if __name__ == "__main__":
    main()
