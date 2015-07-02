# library(ggplot2)
# library(MASS)

setwd("~/tcc-latex/analise/data/fixed/")

data <- read.csv("android-5.1.0_r1.csv", header=TRUE, sep=',')

# for(i in 3:39){

  nome <- paste("~/tcc-latex/analise/results/","android510dist", ".pdf", sep = "")
  pdf(file = nome)

  classes <- data[,2]
  percentil75 <- data[,9]


# Kernel Density Plot
  par(mfrow = c(2, 2)) 
  dens_lcom4 <- density(data$lcom4) # returns the density data 
  dens_acc <- density(data$acc) # returns the density data 
  dens_accm <- density(data$accm) # returns the density data 
  dens_rfc <- density(data$rfc) # returns the density data 




  plot(dens_lcom4,main="LCOM4",xlab="",ylab="Densidade")
  plot(dens_acc,main="ACC",xlab="",ylab="Densidade")
  plot(dens_accm,main="ACCM",xlab="",ylab="Densidade")
  plot(dens_rfc,main="RFC",xlab="",ylab="Densidade")


  # Boxplot to identify outliers ,mainACCsidade LCOM4") # plots the results 
  # boxplot(metric, ma,main="Densidade ACCM"),main="Densidade RFC")
  # nom <- data[,26]
  # amloc <- data[,5]
  # loc <- data[,21]
  #### plot(classes,percentil75)#,xlim=c(0,35),ylim=c(0,35))  


# library(Hmisc)
# t = 1:length(metric)
  # #par(mfrow = c(2, 2)) 
  # hist(metric,main="",xlab=colnames(data)[i])
  # qqnorm(metric);qqline(metric)
  # plot(t,metric,ylab=colnames(data)[i],xlab="Run Sequence",type="l")
  # plot(metric,Lag(metric),xlab=paste(colnames(data)[i],"[i-1]",sep=""),ylab=paste(colnames(data)[i],"[i]",sep=""))
  # mtext(paste(colnames(data)[i]," Data: 4-Plot",sep=""), line = 0.5, outer = TRUE)
# }


