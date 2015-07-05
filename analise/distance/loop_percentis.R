
args <- commandArgs(trailingOnly = TRUE)
# print(args)

path <- args[1]

source("/home/marcos/tcc-latex/analise/script-percentis.R")
  
filename <- basename(path)
dirname <- dirname(path)
filewithoutext <- gsub(".csv","",filename)

# newdir <- paste(dirname,"/",filewithoutext,sep="")

setwd(dirname)

dir.create(filewithoutext)

base <- read.csv(filename, dec = ".", header = TRUE)

#if(i == 39) base = base[base$loc != 0, -c(5,8)]
#else base = base[base$loc != 0,]
#setwd(paste(path, NomeBase, "\\", sep = ""))

setwd(filewithoutext)

for(j in 3:39){
  if(length(base[,1]) < 1000) perc.plot(base, index = j, Np = length(base[,1]))
  else perc.plot(base, index = j)
}


