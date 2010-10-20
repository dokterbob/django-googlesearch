import logging
from django.shortcuts import render_to_response
from ajaxgoogle import search
from django.template import RequestContext


def googlesearch(request):
    """
    Google search with the AJAX Google Search API.
    """

    if request.method == 'POST':
        q = request.POST.get(u'q','')
    elif  request.method == 'GET':
        q = request.GET.get(u'q','')


    if request.GET.has_key('start'):
        start = request.GET.get(u'start','')
        start = int(start)
    else:
        start = 0
    

    if q:
        r = search('site:www.visualspace.nl '+q, rsz='large',hl='nl',lr='lang_nl', start=start)
        results = r['results']
        if results:
            currentPageIndex = r['cursor']['currentPageIndex']
            estimatedResultCount = r['cursor']['estimatedResultCount']
            pages = len(r['cursor']['pages'])
            
            moreResultsUrl = r['cursor']['moreResultsUrl']
            
            if pages > 1:
                if start:
                    prev = (currentPageIndex-1)*8
            
                if int(currentPageIndex)+1 < pages:            
                    next = (currentPageIndex+1)*8
                
            if int(estimatedResultCount) < start+8 :
                end = estimatedResultCount
            elif int(estimatedResultCount) > start+8:
                end = start+8
            else:
                end = 64
    
    #         logging.debug("%s - %s van circa %s resultaten" % (start+1, end, estimatedResultCount))
    #         logging.debug("hee ik heb results: %s" % r)
    #         logging.debug("currentPageIndex: %s" % r['cursor']['currentPageIndex'])
    #         logging.debug("estimatedResultCount: %s" % r['cursor']['estimatedResultCount'])
    #         logging.debug("pages: %s" % r['cursor']['pages'])
    #         logging.debug("len: %s" % len(r['cursor']['pages']))
                
            
    c = RequestContext(request, locals())

    return render_to_response('googlesearch.html', c)

