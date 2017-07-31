#coding:utf-8

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
d = path.dirname(__file__)
text = open(path.join(d, 'word.txt')).read()
alice_coloring = imread(path.join(d, "2.jpg"))
wc = WordCloud(background_color="white",
mask=alice_coloring,
stopwords=STOPWORDS.add("said"),
max_font_size=70,
random_state=100)
wc.generate(text)
image_colors = ImageColorGenerator(alice_coloring)

plt.imshow(wc)
plt.axis("off")
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
wc.to_file(path.join(d, "a.png"))
