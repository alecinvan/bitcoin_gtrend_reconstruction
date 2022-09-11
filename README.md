# bitcoin_gtrend_reconstruction

Currently Google has the limitation for the time resolution to query the trend data, query for only 7-day period provides hourly search trends, weekly data is provided for query 1 year. However we are able to have the monthly data return for any longer period query.

Clearly this problem is to reconstruct the hourly data to make it comparable based on the 3 downloaded dataset provided. Because the hourly data only allows intra-week comparisons, we need to make the valid comparisons globally, the hourly data for each week needs to rescaled by the respective weekly search interest weights for all the weeks between 2017 and present. Since weekly data is retrieved by yearly resolution, it has the same issue as hourly data, so we need to rescale weekly data based on corresponding monthly trend data which is retrieved directly from 2017 to now.

So this is the fundamental principle to solve this problem, please see https://github.com/alecinvan/bitcoin_gtrend_reconstruction/blob/main/reconstructionHourlydata.py for detail.


Alec 
