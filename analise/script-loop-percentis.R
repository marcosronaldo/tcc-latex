path = "/home/marcos/tcc-latex/analise/data/fixed/"

bases = c('android-1.6_r1.2','android-1.6_r1.5',
          'android-2.0_r1','android-2.1_r2.1p2',
          'android-2.2.3_r2','android-2.2_r1',
          'android-2.3.7_r1','android-2.3_r1',
          'android-4.0.1_r1','android-4.0.4_r2.1')

source("script-percentis.R")

for(NomeBase in bases){
  
  setwd(path)  
  dir.create(NomeBase)
  
  base <- read.csv(paste(NomeBase, ".csv", sep = ""), dec = ".", header = TRUE)
  
  #if(i == 39) base = base[base$loc != 0, -c(5,8)]
  #else base = base[base$loc != 0,]
  #setwd(paste(path, NomeBase, "\\", sep = ""))

  setwd(NomeBase)
  
  for(j in 3:39){
    if(length(base[,1]) < 1000) perc.plot(base, index = j, Np = length(base[,1]))
    else perc.plot(base, index = j)
  }
}

