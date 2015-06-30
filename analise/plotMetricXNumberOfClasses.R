library(ggplot2)
library(corrplot)
library(MASS)
library(reshape)  

GLOBAL_DIR="~/tcc-latex/analise/global_percentis/"
ANDROID_DIR="~/tcc-latex/analise/data/fixed/unified_percentis/"
APPS_DIR="~/tcc-latex/analise/apps_data/fixed/unified_percentis/"

setwd(ANDROID_DIR)

files <- list.files(pattern= "\\.csv$")
files = gsub(".csv","",files)

for (file in files){
  data <- read.csv(paste(file, ".csv", sep = ""), header=TRUE, sep=',')

  nome <- paste("~/tcc-latex/analise/results/",file, ".pdf", sep = "")
  pdf(file = nome)

  classes <- data[,2]
  percentil75 <- data[,9]
#   percentil90 <- data[,9]
#   percentil95 <- data[,10]

  plot(classes,percentil75,type="p",ylab=file)#,xlim=c(0,35),ylim=c(0,35))  
}


