from flask import Flask, render_template
import requests

import pymysql
import sys
from lxml import html

app = Flask(__name__)
app.config.update(
    DEBUG=True,
)


@app.route('/')
def index():
    # pass the comic_list to index.html
    return render_template('index.html', data=parse())


def parse():
    match_list = []

    source = requests.get("http://www.bettingtips1x2.com/tips/2016-08-02.html").text
    tree = html.fromstring(source)
    table = tree.xpath('//table[@class="results"]')

    # skips first element (th)
    itertable = iter(table[0])
    next(itertable)

    #time, home, away,  = ''

    # do this shit
    for row in itertable:
        print(row[1].text_content())
        print(row[2].text_content() + ' - ' + row[3].text_content())

    # match =
    # print(match)
    #
    # match_list.append({
    #     'match': match
    # })

    return match_list


def db_test():
    conn = pymysql.connect(host='localhost', user='testuser', passwd='test623', db='testdb');

    cur = conn.cursor()
    cur.execute("SELECT Host,User FROM user")

    print(cur.description)
    print()

    for row in cur:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
    db_test()
    parse()
