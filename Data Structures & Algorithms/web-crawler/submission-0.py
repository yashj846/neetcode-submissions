# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from concurrent.futures import ThreadPoolExecutor
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def getBase(url):
            return url.split('/')[2]
        
        visited = set([startUrl])
        base = getBase(startUrl)

        visited = set([startUrl])
            
        with ThreadPoolExecutor(max_workers = 10) as executor:
            q = collections.deque()
            q.append(executor.submit(htmlParser.getUrls, startUrl))
            while q:
                urls = q.popleft().result()
                for url in urls:
                    if url not in visited and getBase(url) == base:
                        visited.add(url)
                        q.append(executor.submit(htmlParser.getUrls, url))

        return list(visited)


        