library(ggplot2)
library(corrplot)
library(MASS)

setwd("~/tcc-latex/analise/global_percentis")

data <- read.csv("lcom4.csv", header=TRUE, sep=',')

# for(i in 3:39){

  nome <- paste("~/tcc-latex/analise/global_percentis/","lcom4", ".pdf", sep = "")
  pdf(file = nome)

  classes <- data[,2]
  percentil75 <- data[,9]

  # Boxplot to identify outliers  
  # boxplot(metric, main=colnames(data)[i])

  # nom <- data[,26]
  # amloc <- data[,5]
  # loc <- data[,21]
  plot(classes,percentil75)#,xlim=c(0,35),ylim=c(0,35))  

# library(Hmisc)
# t = 1:length(metric)
  # #par(mfrow = c(2, 2)) 
  # hist(metric,main="",xlab=colnames(data)[i])
  # qqnorm(metric);qqline(metric)
  # plot(t,metric,ylab=colnames(data)[i],xlab="Run Sequence",type="l")
  # plot(metric,Lag(metric),xlab=paste(colnames(data)[i],"[i-1]",sep=""),ylab=paste(colnames(data)[i],"[i]",sep=""))
  # mtext(paste(colnames(data)[i]," Data: 4-Plot",sep=""), line = 0.5, outer = TRUE)
# }


