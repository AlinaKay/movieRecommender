import scrapy

from imdb.items import ImdbItem

class DmozSpider(scrapy.Spider):
    name='dmoz'
    allowed_domains=['imdb.org']
    #start_urls=["http://www.imdb.com/search/title?genres=action&sort=moviemeter,asc&start=1&title_type=feature"]

    def __init__(self):
        self.count=self.number()
        self.start_urls=self.generateUrls(self.count)

    def generateUrls(self,count):
        url_list=[]
        t=1
        genre='action'

        for i in range(count):
            t=1+i*50
            #print t
            base_url='http://www.imdb.com/search/title?genres=%s&sort=moviemeter,asc&start=%s&title_type=feature'%(genre,t)
            url_list.append(base_url)
        return url_list

    def number(self):
        # count=response.xpath('//div[@class="leftright"]/div/text()')[0]
        # count_text=count.extract()
        # count_text=count_text[count_text.find('of')+2:count_text.find('titles')]
        # count_text=count_text.replace(' ','')
        # count_text=count_text.replace(',','')
        # count_text=int(count_text)
        # print count_text
        # times=count_text/50+1

        '''either get the count of each genre from imdb page or uncomment the above. i suggest the former one'''
        times = 51/50+1
        #times = 29125/50+1

        return times
        

    def parse(self,response):
        #pass
        bad_chars="()"
        for sel in response.xpath('//td[@class="title"]'):
            #print len(title)
            item=ImdbItem()
            title=sel.xpath('a/text()').extract()
            title=''.join(title)
            title_href=sel.xpath('a/@href').extract()
            title_href=''.join(title_href)
            year_type=sel.xpath('span[@class="year_type"]/text()').extract()
            year_type=''.join(year_type)
            year_type=year_type.strip("()")
            user_rating=sel.xpath('div[@class="user_rating"]/div/@title').extract()
            user_rating=''.join(user_rating)
            rating_rating=sel.xpath('div[@class="user_rating"]/div/span[@class="rating-rating"]/span/text()').extract()
            if len(rating_rating)==3:
                rating_rating=rating_rating[0]
            else:
                rating_rating="NA"
            outline=sel.xpath('span[@class="outline"]/text()').extract()
            outline=''.join(outline)
            credit_dir=sel.xpath('span[@class="credit"]/a/text()').extract()
            credit_with=sel.xpath('span[@class="credit"]/a/text()').extract()
            genre=sel.xpath('span[@class="genre"]/a/text()').extract()
            mins=sel.xpath('span[@class="runtime"]/text()').extract()
            mins=''.join(mins)
            if mins=="":
                mins=0
            else:
                mins=mins.split(' ')[0]
            item['title']=title
            item['title_href']=title_href
            item['year_type']=year_type
            item['user_rating']=user_rating
            item['rating_rating']=rating_rating
            item['outline']=outline
            item['credit_dir']=credit_dir
            item['credit_with']=credit_with
            item['genre']=genre
            item['mins']=mins
            yield item
            #print title

        #for i in range(times):x
        # for sel in response.xpath('//ul/li'):
        #     item=DmozItem()
        #     item['title']=sel.xpath('a/text()').extract()
        #     item['link']=sel.xpath('a/@href').extract()
        #     item['desc']=sel.xpath("text()").extract()
        #     yield item