path = "/home/marcos/tcc-latex/analise/apps_data/fixed/"

setwd(path)

files <- list.files(pattern= "\\.csv$")
files = gsub(".csv","",files)

source("~/tcc-latex/analise/script-percentis.R")

for (file in files){

  setwd(path)
  
  base <- read.csv(paste(file, ".csv", sep = ""), header=TRUE, sep=',')
  print(paste("li arquivo ",file,sep=""))
  
  dir.create(file)
  setwd(file)  

  # nome <- paste(path,file,'/',file, ".pdf", sep = "")
  # pdf(file = nome)
  
  for(j in 3:39){
    if(length(base[,1]) < 1000) perc.plot(base, index = j, Np = length(base[,1]))
    else perc.plot(base, index = j)
  }
}

