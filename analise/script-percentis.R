# Função perc.plot: Gera um gráfico dos percentis pelos quantis de uma dada variável.
# Parâmetros: 
#   - base: base contendo as variáveis para gerar o gráfico;
#   - index: índice da coluna da base dada que representa a posição da variável;
#   - Np: número de percentis a serem usados para gerar o gráfico

perc.plot <- function(base = NULL, index = NULL, Np = 1000){
  
  var <- base[,index]
  #var <- base[index,]
  
  perc <- 1:Np/(Np+1)
  n <- length(var)
  
  perc.var <- array(dim = Np)
  
  var.sort <- sort(var)
  
  for(i in 1:Np) perc.var[i] <- var.sort[round(perc[i]*n)]
  
  h.line <- 0:6*((perc.var[Np] - perc.var[1])/6)
  nome <- paste(colnames(base)[index], ".pdf", sep = "")
  pdf(file = nome)
  plot(perc.var ~ perc, type = "n", xlab = "", ylab = "", axes = FALSE)
  abline(h = h.line, v = 0:10/10, col = "lightgray", lty = 3)
  par(new = T)
  plot(perc.var ~ perc, type = "l", xlab = "Percentis", ylab = "Quantis", main = colnames(base)[index])
  dev.off()

  p <- c(.01, .05, .1, .25, .50, .75, .9, .95, .99)  
  
  table <- c(min(base[,index]), quantile(base[,index], probs = p, na.rm = TRUE), max(base[,index]))
  table <- t(table)
  colnames(table) = c("Mínimo", "1%", "5%", "10%", "25%", "50%", "75%", "90%", "95%", "99%", "Máximo")
  write.table(table, paste(colnames(base)[index], ".txt", sep = ""), sep = "\t", row.names = FALSE, dec = ",") 
}

