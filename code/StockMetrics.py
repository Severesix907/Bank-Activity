
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        averages = []
        for row in self.data: #Created a loop to see what we are working on 
            valid_prices = []
            for num in row[1:]: #This line of code is used to evaluate the elements within the list and since we are dealing with number the dates need to be remove
                num = num.strip()# .strip() is used to remove any leading or trailing whitespaces
                if num and num.replace('.', '', 1): #I used .replace to remove the empty string and change then to empty object
                   price = float(num) # This is for converting the string into a float variable 
                   valid_prices.append(price)
                print(price)
            
            
            sum_averages = sum(valid_prices)/ len(valid_prices)#we find the average here by adding the amount of objects in a list and dividing them
            averages.append(round(sum_averages,3))# since we want to round it so we use the round and additonally show 3 decimal places
            print(averages)
        return averages

    def median02(self):
        """pt2
        """ 
        medians = []
        for row in self.data:
            valid_prices = []               # we reuse the same code here for the median 
            for num in row[1:]:
                num = num.strip()
                if num and num.replace('.', '', 1):
                   price = float(num)
                   valid_prices.append(price)
            

            
            
            sum_medians = stats.median(valid_prices)    # we use the stats package to find the median 
            medians.append(sum_medians)
            print(sum_medians)

        return medians
        ...

    def stddev03(self):
        """pt3
        """
        stddev = []
        for row in self.data:
            valid_prices = []           # we use the same line of code here as the previous 
            for num in row[1:]:
                num = num.strip()
                if num and num.replace('.', '', 1):
                   price = float(num)
                   valid_prices.append(price)
            

            
            
            new_stddev = stats.stdev(valid_prices)      #Additionally here we use the stats method and we find the stdev of the data we collect 
            stddev.append(round(new_stddev, 3))         # we round to the nearest 3rd value here so we use the round method
            print(stddev)

        return stddev
       
