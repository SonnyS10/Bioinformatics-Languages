  print("Hello, welcome to R")

  library(ggplot2)

  data<-read.csv("C:/Users/sonny/OneDrive/Documents/Bioinformatics Language/Coding Projects/R Graph Assignment/YeastGeneData.csv", header=TRUE)
  chromosome=data$Chromosome
  label=data$Label
  GC=data$GC
  searched_in=data$SearchedIn
  searched_in_percent=data$SearchedInPercent

  YeastGene.data<-data.frame(
    chromosome,
    label,
    GC,
    searched_in,
    searched_in_percent
  )
  
  print(YeastGene.data)
  print(summary(YeastGene.data))
  stat_summary=summary(YeastGene.data)
  
  plot1<-ggplot(YeastGene.data, aes(x=chromosome, y=searched_in_percent,)) + geom_point()
  print(plot1)
  
  plot2<-ggplot(YeastGene.data, aes(x=chromosome, y=GC)) +
    stat_boxplot(aes(x=chromosome, y=GC),
    geom='errorbar', linetype=1, width=0.5) +
    geom_boxplot(aes(x=chromosome,y=GC),outlier.shape=1) +
    stat_summary(fun.y=mean, geom="point", size=2) +
    stat_summary(fun.data = mean_se, geom = "errorbar")
  print(plot2)
  
  
  