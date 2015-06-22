library(ggplot2)
library(MASS)

setwd("~/tcc-latex/analise/data/fixed/")

data <- read.csv("all_merged.csv", header=TRUE, sep=',')

for(i in 3:39){

  nome <- paste("~/tcc-latex/analise/results/",colnames(data)[i], ".pdf", sep = "")
  pdf(file = nome)

  # Boxplot to identify outliers
  metric <- data[,i]
  
  boxplot(metric, main=colnames(data)[i])

  # library(Hmisc)
  # t = 1:length(metric)
  # #par(mfrow = c(2, 2)) 
  # hist(metric,main="",xlab=colnames(data)[i])
  # qqnorm(metric);qqline(metric)
  # plot(t,metric,ylab=colnames(data)[i],xlab="Run Sequence",type="l")
  # plot(metric,Lag(metric),xlab=paste(colnames(data)[i],"[i-1]",sep=""),ylab=paste(colnames(data)[i],"[i]",sep=""))
  # mtext(paste(colnames(data)[i]," Data: 4-Plot",sep=""), line = 0.5, outer = TRUE)
}

