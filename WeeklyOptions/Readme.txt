The data was taken from https://tradecatcher.blogspot.com/p/nifty-wee.html?m=1
I've not made any changes to the data itself. Just cleaned it up in terms of name.

Read one of their disclaimers here.
https://tradecatcher.blogspot.com/p/options-ieod.html?m=1

From what I've understood some ticks where zero transactions happened (esp for non ATM options), have been omitted.

I've attached the rough code snippets I've used to clean it. Essentially my flow went by this.

->Name each CSVfile to a [articular standard, making it easy for calling the data during backtesting
-> Name each folder correspondingly
-> Name the first column of each CSV with the updated CSV name. (Didn't look like it was needed but I thought I won't take the chance)

If you are choosing to use the data, you do so at your discretion. The author and I am not responsible for any damage.
Feel free to contact me if you find mistakes in my code.