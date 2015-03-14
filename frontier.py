__author__ = 'Abhijeet Sharma'
#import heapq

class FrontierQueue:
    '''Seed URLs should always be crawled first.
    Prefer pages with higher in-link counts.
    If multiple pages have maximal in-link counts, choose the option which has been in the
    queue the longest'''

    def  __init__(self, seed_list):
        #self.heap = []

        #self.count = 0
        self.seed = {}
        for item in seed_list:
            self.seed[item] = set()
        self.front = {}
        #print "front initialized ", self.front

    def push(self, item, in_link):
        #entry = (priority, self.count, item)
        #heapq.heappush(self.heap, entry)

        self.front[item] = set([in_link])
        #self.count += 1
        #print "item ", item," succsessfully pushed in front", self.front

    def pop(self):
        #(_, _, item) = heapq.heappop(self.heap)

        if len(self.seed) == 0:
            item = sorted(self.front.items(),key = lambda x:len(x[1]))[0][0]
            in_links = self.front[item]
            del self.front[item]
            #print "item ", item," successfully popped from front ", self.front
            return item, in_links
        else:
            item = sorted(self.seed.items(),key = lambda x:len(x[1]))[0][0]
            in_links = self.seed[item]
            del self.seed[item]
            #print "item ", item," successfully popped from Seed ", self.seed
            return item, in_links


    def isEmpty(self):
        if len(self.front) == 0:
            return len(self.seed) == 0
        else:
            return False

    def update(self, item, in_link):
        self.front[item].add(in_link)
        #print "item ", item," and in_link ", in_link," successfully updated in front ", self.front

    def exists(self, item):
        if self.front.get(item) == None:
            #print "Item ", item," doesn't exist in Front"
            return False
        else:
            #print "Item ", item," exists in Front"
            return True