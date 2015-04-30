from HTMLParser import HTMLParser
import urllib2
import wget
import os

hURL = 'https://www.hipchat.com/emoticons'
defaultD = 'emojis'

class HEHTMLParser(HTMLParser):
    emojiURLs = []
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attrName, attrValue in attrs:
                if attrName == 'src' and 'emoticons' in attrValue:
                    self.emojiURLs.append(attrValue)

def hSaveEmojis(d='.'):
    response = urllib2.urlopen(hURL)
    html = response.read()
    response.close()
    heParser = HEHTMLParser()
    heParser.feed(html)
    for emojiURL in heParser.emojiURLs:
        outFilename = emojiURL.split('/')[-1]
        outFilename = outFilename.split('-')[0] + '.' + outFilename.split('.')[-1]
        wgotFileName = wget.download(emojiURL, os.path.join(d, outFilename))
        print ' %s saved as %s' % (emojiURL, wgotFileName)

if __name__ == '__main__':
    import argparse
    aParser = argparse.ArgumentParser(description="Save HipChat emojis from %s to directory %s (will create if doesn't exist)." % (hURL, defaultD))
    args = aParser.parse_args()

    if not os.path.exists(defaultD):
        os.makedirs(defaultD)
    hSaveEmojis(defaultD)
