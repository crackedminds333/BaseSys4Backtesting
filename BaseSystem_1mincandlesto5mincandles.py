#import libraries and modules

import sys
import csv
import numpy as np

#Define some necessary functions and useful functions

#Functiong for getting new high and new low
#Zero implies start of a new day/candle
def getnewhigh(high,candle_high):
    if high == 0:
        return candle_high
    elif candle_high > high:
        return candle_high
    else:
        return high

def getnewlow(low,candle_low):
    if low == 0:
        return candle_low
    elif candle_low < low:
        return candle_low
    else:
        return low

#Checks if time is 12:30 am or past. Change the function as per the time you want to be checked
#Format for timestr is assumed to be '09:15:00'
def isafter1000am(timestr):
    h=int(timestr[0:2])
    m=int(timestr[3:5])
    if (h > 12) or (h == 12 and m >=30):
        return 1
    else:
        return 0

#Check if the current 1min candle is in the process of forming a 5 minute candle. You can use the same structure to convert 1 min candle data to any other candle
#Returns 1 (True) if the candle time in mins is 00,01,02,03. Returns 0 (False) if it is 04 as 04 could be the 1 min that ends the 5 min candle formation process
def isforming5mincandle(timestr):
    m=int(timestr[3:5])
    if ((m+1)%5 == 0):
        return 0
    else:
        return 1

#Execution starts

#Import your chart data. The one used for reference is a NIFTY spot data file. You can find the same in the repository
#The result file that was created by this program is also found in the repository
with open('Nifty.csv') as input_file, open('Nifty_5mincandles.csv','w', newline='') as output_file:

    #Opens the result file for writing. Writes in the column names
    writer = csv.writer(output_file)
    writer.writerow(["Year", "Month", "Day", "Time", "Open", "High", "Low", "Close", "Volume"])
    
    #Every row of Niftry is converted to a list and stored in 'row'. Total_dataset is the number of total datasets in Nifty.
    nifty_5min_csv = csv.reader(input_file, delimiter=',')
    rows = list(nifty_5min_csv)
    total_dataset = len(rows)
    
    #Initilize variables to calculate T-2, T-1, current day's high/low
    day_high = 0
    day_low = 0
    Tminus1High = 0
    Tminus1Low = 0
    Tminus1Close = 0
    Tminus2High = 0
    Tminus2Low = 0
    Tminus2Close = 0

    #Initialize variables to calculate 5 min candles OHLC
    candle_open = 0
    candle_close = 0
    candle_high = 0
    candle_low = 0
    candle_time = 0

    #Initialize list to hold current day's ohlc values in case of entry/exits based on it
    o = []
    l = []
    h = []
    c = []
    
    #Initialize variables to check for day change, possible signal for entry
    #Signal is +1 for buy, -1 for sell, 0 for no signal.
    day_change = 1
    signal = 0
    
    #In case a signal goes through the following variables can note some of the data you can record in another file.
    pos_open = 0
    entry_time = 0
    exit_time = 0
    reward = 0
    R = 0
    sl = 0    

    #Initialize line_count to read through the rows one by one. 0th row is the column name so it is skipped
    #Current day is initialized to first data set's 'yyyy-mm-dd'. rows[line_count][0][0:11] extracts the same
    line_count = 1
    current_day = rows[line_count][0][0:11]
    
    #Process the data.
    while line_count < total_dataset:
        
        #Reset parameters for new day
        if day_change == 1:
            day_high = 0
            day_low = 0
            candle_high = 0
            candle_low = 0
            candle_open = 0
            candle_close = 0
            o = []
            l = []
            h = []
            c = []

            #Assuming that the backtest is for intraday
            signal = 0
            pos_open = 0
            entry_time = 0
            exit_time = 0
            reward = 0
            sl = 0
            R = 0
            
            #Once we have reset it, this will be reset to zero until we encounter the next day change
            day_change = 0
        
        
        if (current_day == rows[line_count][0][0:11]):
            
            #Start code for candle formation
            
            #First we compare the current 1min candle's high and lows with established highs and lows of the 5 min candle
            candle_high = getnewhigh(candle_high,float(rows[line_count][2]))
            candle_low = getnewlow(candle_low,float(rows[line_count][3]))

            #Extract the current candletime
            current_candletime = rows[line_count][0][11:19]


            #We check if the current 1 min candle is closing the 5 min candle or not. If no we enter...
            if ( isforming5mincandle(rows[line_count][0][11:20]) ):
                
                #If the candle is the beginning of a new 5 min candle, we add it to the open list
                if (int(current_candletime[3:5])%5==0):
                    candle_open = float(rows[line_count][1])
                    o.append(candle_open)
                    candle_time = current_candletime
                    
            #Since the candle is the closing candle, we close the candle to the close list, and add candle's highs and lows to their respective list
            else:
                candle_close = float(rows[line_count][4])
                l.append(candle_low)
                h.append(candle_high)
                c.append(candle_close)           
                writer.writerow([rows[line_count][0][0:4], rows[line_count][0][5:7], rows[line_count][0][8:10], candle_time, o[-1], h[-1], l[-1], c[-1], 0])
                
                #Reset for next candle
                candle_open = 0
                candle_close = 0
                candle_high = 0
                candle_low = 0
                candle_time = 0

            #End code for candle formation

            #Start code for checking signal. Currently we are assuming only one position can be open on Nifty at a time. Code snippets have been commented out for smooth execution of the program

            #if ( <long_setup_rules> == 1 and signal == 0 ):            Checks if currently there are no positions open (signal = 0)
            #    signal = 1
            #elif ( <short_setup_rules> == 1 and signal == 0 ):         Checks if currently there are no positions open (signal = 0)
            #    signal = -1
            #End code for checking signal

            #Code for trade management
            #if signal != 0:
            #     if pos_open == 0 and signal == 1:               Long is entered here
            #         pos_open = <current_candle_tick>
            #         sl = <your sl method>
            #         R = pos_open - sl
            #         entry_time = rows[line_count][0][11:19]
            #     elif pos_open == 0 and signal == -1:            Short is entered here
            #         pos_open = <current_candle_tick>
            #         sl = <your sl method>
            #         R = sl - pos_open
            #         entry_time = rows[line_count][0][11:19]                        
            #     elif pos_open!= 0 and <exit_condition>:         Long open and exit condition fulfilled
            #         exit_time = rows[line_count][0][11:19]
            #         if signal == 1:
            #             reward = <current_candle_tick> - pos_open
            #             <code for writing into your trade record file>
            #         elif signal == -1:
            #             reward = pos_open - <current_candle_tick>
            #             <code for writing into your trade record file>
            #
            #         #Reset parameters to no trade open condition
            #         pos_open = 0
            #         entry_time = 0
            #         exit_time = 0
            #         signal = 0
            #         reward = 0
            #         R = 0
            #         sl = 0
            #     else:
            #         <code for trailing SL or calculating other params for trade management>                        
            #Update day;s high & day's low AFTER checking signal. Not to be called if first candle is being formed

            #Checks code for day's high and low
            if (len(h)>=1) and (len(l)>=1):
                day_high = getnewhigh(day_high,h[-1])
                day_low = getnewlow(day_low,l[-1])
        
        #when the row read is that of a different day
        else:
            #we indicate that the day has changed
            day_change = 1
            
            #set the new day as current day
            current_day = rows[line_count][0][0:11]

            #Previous highs, lows etc are all changed as needed
            Tminus2High = Tminus1High
            Tminus2Low = Tminus1Low
            Tminus2Close = Tminus1Close
            Tminus1High = day_high
            Tminus1Low = day_low
            Tminus1Close = c[-1]
            
            #reduce linecount by one as the new day's first data is yet to be read
            line_count -=1
        
        #Go to next data point no
        line_count +=1