from crawler import Crawler

if __name__ == '__main__':

    # your virgool username
    virgool_user_name = 'haniehmahdavi26'

    # don't change keys, just update values
    contact_info = {'linkedin' : 'https://www.linkedin.com/in/hanieh-mahdavi/',
                    'virgool': 'https://virgool.io/@haniehmahdavi26', 
                    'telegram': 'https://t.me/honio_notes'}

    crawler = Crawler(virgool_user_name=virgool_user_name, contact_info=contact_info)
    crawler.run()