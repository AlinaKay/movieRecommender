from django.shortcuts import render_to_response
from django.template import RequestContext
from lxml import etree
import urllib2
from django.core.context_processors import csrf

# Create your views here.

def index(request):
	c = {}
	c.update(csrf(request))
	dictlist=[]
	if request.POST:
		print 'h'
		print 'post request'
		text=request.POST['query']
		li=[int(s) for s in text.split() if s.isdigit()]
		count=li[0]
		url='http://www.imdb.com/chart/top'
		page=urllib2.urlopen(url).read()
		x=etree.HTML(page)
		url=x.xpath('//td[@class="titleColumn"]/a/@href')
		rank=x.xpath('//td[@class="titleColumn"]/span[@name="ir"]/text()')
		title=x.xpath('//td[@class="titleColumn"]/a/@title')
		secondaryinfo=x.xpath('//td[@class="titleColumn"]/span[@class="secondaryInfo"]/text()')
		fullrating=x.xpath('//td[@class="ratingColumn imdbRating"]/strong/@title')
		rating=x.xpath('//td[@class="ratingColumn imdbRating"]/strong/text()')
		dictlist = [dict() for x in range(count)]
		for k in range(count):
			dictlist[k]={'url':url[k],'title':title[k]}
		#return render_to_response('movielist.html', {'movies': dictlist,'name':'taranjeet'}, context_instance=RequestContext(request))
	return render_to_response('index.html',{'movies': dictlist,'name':'taranjeet'},context_instance=RequestContext(request))

def suggestmovie(request,query=None):
	if request.POST:
		print 'get request'
		text=request.GET['query']
		li=[int(s) for s in text.split() if s.isdigit()]
		count=li[0]
		url='http://www.imdb.com/chart/top'
		page=urllib2.urlopen(url).read()
		x=etree.HTML(page)
		url=x.xpath('//td[@class="titleColumn"]/a/@href')
		rank=x.xpath('//td[@class="titleColumn"]/span[@name="ir"]/text()')
		title=x.xpath('//td[@class="titleColumn"]/a/@title')
		secondaryinfo=x.xpath('//td[@class="titleColumn"]/span[@class="secondaryInfo"]/text()')
		fullrating=x.xpath('//td[@class="ratingColumn imdbRating"]/strong/@title')
		rating=x.xpath('//td[@class="ratingColumn imdbRating"]/strong/text()')
		dictlist = [dict() for x in range(count)]
		for k in range(count):
			dictlist[k]={'url':url[k],'title':title[k]}
		return render_to_response('movielist.html', {'movies': dictlist,'name':'taranjeet'}, context_instance=RequestContext(request))