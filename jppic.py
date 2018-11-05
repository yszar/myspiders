import re
import os
import urllib
import urllib.request


class Jppic():

    url = "http://tieba.baidu.com/p/2166231880?traceid="
    picurl = '<img pic_type="0" class="BDE_Image" src="([\s\S]*?)" bdwater="杉本有美吧'

    def __gethtmls(self):
        r = urllib.request.urlopen(Jppic.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __geturl(self, htmls):
        picurls = re.findall(Jppic.picurl, htmls)
        return picurls

    def __report_hook(count, block_size, total_size):
        print('%02d%%' % (100.0 * count * block_size / total_size))

    def __downpic(self, picurls):
        for pic in picurls:
            picpath = os.path.basename(pic)
            urllib.request.urlretrieve(pic, './pic/' + picpath)

    def go(self):
        htmls = self.__gethtmls()
        theurls = self.__geturl(htmls)
        self.__downpic(theurls)


Jppic = Jppic()
Jppic.go()