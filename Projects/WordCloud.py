# =================================================
# Title:  Word Cloud
# Author: HarishBalaji ShanmugaSundaram
# Date:   28 August 2019
# =================================================
import os
import os.path

import matplotlib.pyplot as plt
from wordcloud import WordCloud

dir = r'/Users/harishbalaji/documents/mycode/mycode/mypythoncode/WordCloud'
if not os.path.exists(dir):
    os.mkdir(dir)


# Create a list of word
text = ('Harish Vinoth Aswin Vivek Aishwariya NaveenKanna Sadiqul')
wordcloud = WordCloud(width=1600, height=800).generate(text)
plt.figure(figsize=(20, 10), facecolor='k')
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.tight_layout(pad=0)

# Save the word cloud as an svg file
plt.savefig('/Users/harishbalaji/documents/mycode/mycode/mypythoncode/WordCloud/My_Word_Cloud.svg',
            format='svg', dpi=1200)
