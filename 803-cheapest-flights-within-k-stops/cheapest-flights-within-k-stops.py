class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        price_table = [ float('inf') for _ in range(n) ]
        price_table[ src ] = 0
		
        for source, destination, ticket_price in flights:
            if source == src:
                price_table[destination] = ticket_price
        
        
        for trasfer in range(0, K):
            
            current_price = [*price_table]
            
            for source, destination, ticket_price in flights:
                
                current_price[destination] = min(current_price[destination], price_table[source] + ticket_price )
            
            price_table = current_price
        
        
        if price_table[dst] == float('inf'):
            return -1
        else:
            return price_table[dst]
        