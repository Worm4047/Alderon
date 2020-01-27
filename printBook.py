"""

 Alderon: an experiment in linguistics.


"""
import random
import sentence

def genParagraph():
    """generate paragraph"""
    num_sentences = random.randrange(10, 30)
    sentences = [(" ".join(sentence.Sentence())).capitalize() + "." for i in range(num_sentences)]
    return "<p>{0}</p>".format(" ".join(sentences))

def genChapter():
    """generate chapter"""
    num_paragraphs = random.randrange(20, 50)
    paragraphs = [genParagraph() for i in range(num_paragraphs)]
    return "\n".join(paragraphs)

def Book(booklen):
    """Print the book"""
    real_length = 0
    output_file = open("Alderon.html", "w")
    text = ""
    text += "<html><body style='font-size: 12pt; font-style:-apple-system,BlinkMacSystemFont,Roboto,Helvetica,Arial,sans-serif'>"
    while real_length <= booklen:
        chapter = genChapter()
        text += "<p>"+chapter+"</p>\n"
        real_length += len(chapter.split(" "))
    text += "</body></html>"
    output_file.write(text)
    output_file.close()
    print("Printed Book")

if __name__ == '__main__':
    random.seed(1234567890)
    Book(40000)
    