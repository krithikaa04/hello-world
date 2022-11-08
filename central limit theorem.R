#Step 1 - Importing Data
#_______________________________________________________

#Importing the csv data 
data<-read.csv(file.choose())

#Step 2 - Validate data for correctness
#______________________________________________________

#Count of Rows and columns
dim(data)

#View top 10 rows of the dataset
head(data,10)
#Step 3 - Calculate the population mean and plot the observations
#___________________________________________________________________

#Calculate the population mean
mean(data$Wall.Thickness)

#Plot all the observations in the data
hist(data$Wall.Thickness,col = "pink",main = "Histogram for Wall Thickness",xlab = "wall thickness")
abline(v=12.8,col="red",lty=1)

#We will take sample size=10, samples=9000
#Calculate the arithmetice mean and plot the mean of sample 9000 times

s10<-c()
#replace =TRUE - data can occur more than once

n=9000
for (i in 1:n) {
  s10[i] = mean(sample(data$Wall.Thickness,10, replace = TRUE))}
hist(s10, col ="lightgreen", main="Sample size =10",xlab = "wall thickness")
abline(v = mean(s10), col = "Red")
abline(v = 12.8, col = "blue")