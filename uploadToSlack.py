import mechanize
import os

defaultD = 'emojis'

def sUploadEmojis(url, email, password, d='.'):
    print 'visiting %s...' % url
    br = mechanize.Browser()
    br.set_handle_robots(False)
    loginResponse = br.open(url)
    br.select_form(nr=0)
    br['email'] = email
    br['password'] = password
    loggedInResponse = br.submit()

    for emojiFilename in os.listdir(d):
        emojiName, extension = emojiFilename.split('.')
        if extension != 'png':
            print '%s extension unsupported' % emojiFilename
            continue

        print 'getting add emoji page... ',
        if not url.endswith('/'): url += '/'
        newEmojiResponse = br.open('%s/customize/emoji' % url)
        br.select_form(nr=0)
        br['name'] = emojiName
        br.form.add_file(open('%s/%s' % (d, emojiFilename)), 'image/*;capture=camera', emojiFilename)
        print 'uploading %s...' % emojiFilename
        br.submit()

if __name__ == '__main__':
    import argparse
    aParser = argparse.ArgumentParser(description="Upload new emojis to Slack from directory %s." % defaultD)
    aParser.add_argument('--url', type=str, help='Slack URL, usually https://organization.slack.com', required=True)
    aParser.add_argument('--email', type=str, help='E-mail address of a Slack admin in the organization', required=True)
    aParser.add_argument('--password', type=str, help='Their password', required=True)
    args = aParser.parse_args()

    sUploadEmojis(args.url, args.email, args.password, defaultD)
