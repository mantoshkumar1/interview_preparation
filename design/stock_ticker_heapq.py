"""
https://stackoverflow.com/questions/43550873/stock-ticker-data-structure-for-getting-top-k-stock-prices

Given a stream of stock prices write a data structure that supports that following operations:

 1. StockSticker(int k) : Initialize the size of the ticker.
 2. void addOrUpdate(String stock, double price) : Add or update a stock
 3. List<Stock> top(int k) : Get top k stocks.
 
StockSticker contains stocks with the highest prices up to  initial size of the ticker.
"""
import itertools
import heapq


class Stock:
    _counter = itertools.count()
    
    def __init__(self, name, price):
        self.count = next(Stock._counter)
        self.price = price
        self.name = name
        self.deleted = False

    def __repr__(self):
        return "{}, price={}, deleted={}".format(
            self.name, self.price, "Yes" if self.deleted else "No"
            )
    
    def __eq__(self, other):
        return (self.price, self.count) == (other.price, other.count)

    def __ne__(self, other):
        return (self.price, self.count) != (other.price, other.count)
    
    def __lt__(self, other):
        return (self.price, self.count) < (other.price, other.count)

    def __le__(self, other):
        return (self.price, self.count) <= (other.price, other.count)
    
    def __gt__(self, other):
        return (self.price, self.count) > (other.price, other.count)
    
    def __ge__(self, other):
        return (self.price, self.count) >= (other.price, other.count)


class StockSticker:
    def __init__(self, size):
        self.stocks = []
        self.stock_dict = dict()  # {stock_name: stock_obj} -> This only contains active stock ref.
        self.remaining_stock_capacity = size
    
    def topK(self, k):
        active_stocks = []
        
        while self.stocks:
            s = heapq.heappop(self.stocks)
            if s.deleted:
                continue
            
            active_stocks.append(s)
        
        # preparing ans
        ans = []
        index = len(active_stocks) - 1
        while k > 0 and index >= 0:
            ans.append(active_stocks[index].name)
            index -= 1
            k -= 1
        
        # pushing back active stocks to heapq
        for s in active_stocks:
            heapq.heappush(self.stocks, s)
        
        return ans
        
    def addOrUpdate(self, stock_name, price):
        if stock_name not in self.stock_dict:
            # check curr number of active stocks
            if self.remaining_stock_capacity == 0:
                # find min active stock and delete its reference from stock_dict
                while True:
                    min_stock = heapq.heappop(self.stocks)
                    if not min_stock.deleted:
                        self.remaining_stock_capacity += 1
                        break
                        
                self.stock_dict.pop(min_stock.name)
                
        else:
            # get reference of matching stock from stock_dict and mark its deleted=True
            stock = self.stock_dict[stock_name]
            
            # if price of a stock does not change, then there is no point doing anything
            if stock.price == price:
                return
            
            stock.deleted = True
            self.remaining_stock_capacity += 1
        
        # add new stock in pq
        new_stock = Stock(stock_name, price)
        heapq.heappush(self.stocks, new_stock)
        self.remaining_stock_capacity -= 1
        
        # update stock_dict with reference of this stock
        self.stock_dict[stock_name] = new_stock
        

if __name__ == "__main__":
    sp = StockSticker(3)
    assert [] == sp.topK(k=2)
    
    sp.addOrUpdate('google', 10)
    # ('google', 10, Del=F)
    assert ['google'] == sp.topK(k=1)
    assert 2 == sp.remaining_stock_capacity
    assert 1 == len(sp.stocks)

    assert ['google'] == sp.topK(k=2)
    # ('google', 10, Del=F)
    assert 2 == sp.remaining_stock_capacity
    assert 1 == len(sp.stocks)
    
    sp.addOrUpdate('google', 8)
    # ('google', 8, Del=F), ('google', 10, Del=T)
    assert 2 == sp.remaining_stock_capacity
    assert 2 == len(sp.stocks)

    assert ['google'] == sp.topK(k=2)
    # ('google', 8, Del=F)
    assert 2 == sp.remaining_stock_capacity
    assert 1 == len(sp.stocks)

    sp.addOrUpdate('cisco', 20)
    # ('google', 8, Del=F), ('cisco', 20, Del=F)
    assert 1 == sp.remaining_stock_capacity
    assert 2 == len(sp.stocks)
    
    sp.addOrUpdate('yahoo', 12)
    # ('google', 8, Del=F), ('yahoo', 12, Del=F), ('cisco', 20, Del=F)
    assert 0 == sp.remaining_stock_capacity
    assert 3 == len(sp.stocks)
    
    sp.addOrUpdate('cisco', 12)
    # ('google', 8, Del=F), ('yahoo', 12, Del=F), ('cisco', 12, Del=F), ('cisco', 20, Del=T)
    assert 0 == sp.remaining_stock_capacity
    assert 4 == len(sp.stocks)

    assert ['cisco', 'yahoo'] == sp.topK(2)
    # ('google', 8, Del=F), ('yahoo', 12, Del=F), ('cisco', 12, Del=F)
    assert 0 == sp.remaining_stock_capacity
    assert 3 == len(sp.stocks)

    sp.addOrUpdate('aricent', 30)
    # ('yahoo', 12, Del=F), ('cisco', 12, Del=F), ('aricent', 30, Del=F)
    
    sp.addOrUpdate('aricent', 20)
    # ('yahoo', 12, Del=F), ('cisco', 12, Del=F), ('aricent', 30, Del=T), ('aricent', 20, Del=F)
    assert 0 == sp.remaining_stock_capacity
    assert 4 == len(sp.stocks)

    sp.addOrUpdate('siemens', 45)
    # ('cisco', 12, Del=F), ('aricent', 30, Del=T), ('aricent', 20, Del=F), ('siemens', 45, Del=F)
    assert 0 == sp.remaining_stock_capacity
    assert 4 == len(sp.stocks)

    assert ['siemens', 'aricent', 'cisco'] == sp.topK(k=4)
    # ('cisco', 12, Del=F), ('aricent', 20, Del=F), ('siemens', 45, Del=F)
    assert 0 == sp.remaining_stock_capacity
    assert 3 == len(sp.stocks)
