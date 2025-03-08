#Importing the relevant lib
library(readr)
# Placing the External CSV into a dataframe named x variable
x <- read.csv('https://raw.githubusercontent.com/jhnboyy/CUNYSPS_DATA607/main/Week1/538_generic_poll_list.csv')
#Printing the firs4 5 rows of the dataframe
print(head(x))
print(dim(x))
# Checking that it is infact in a df
print(class(x))
# Now working to get a subset for the assignment. The columns we want to keep are:
# startdate, enddate, pollster, grade, samplesize, pollid, url,  dem, rep adjusted_dem adjusted_rep
subset_df <- x[, c("poll_id", "startdate", "enddate", "pollster", "grade", "samplesize", "url", "dem", "rep", "adjusted_dem", "adjusted_rep")]
#Printing the first 5 rows
print(head(subset_df))
print(dim(grt_med))
#Further limiting the df, but filtering by the sample size. Want to grab the median, and then those that are above the median.
sample_size_med <- median(subset_df$samplesize)
print(sample_size_med)
# Need to remove the NA's 
sample_size_med <- median(subset_df$samplesize, na.rm = TRUE)
print(sample_size_med)
#Limiting the df to the rows over that value
grt_med<-subset_df[subset_df$samplesize > sample_size_med, ]
print(head(grt_med))
print(dim(grt_med))
