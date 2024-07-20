#This script was used to generate Figures used in the main text, as well as supplementary figures. 

#Set Up
library('ggplot2')
library(ggplot2)
library(dplyr)
library(tidyr)
library(ggpubr)
library(ggplot2)
library('ggExtra')



#Generate Supplementray File 7. Empirical cumulative plot of cluster sizes generated at all clustering thresholds
df <- read.csv("cluster_taxID_info.csv", header=TRUE)
df$theresholds_id <- factor(df$theresholds_id, levels=c('98%', '98.1%', '98.2%', '98.3%', '98.4%', '98.5%', '98.6%', '98.7%', '98.8%', '98.9%', '99%', '99.1%', '99.2%',  '99.3%', '99.4%', '99.5%', '99.6%', '99.7%',
                                                        '99.8%', '99.9%', '100%'))  

pdf(file='../supplementary_file_7.pdf', width=12, height=8)
p<-ggplot(df, aes(x=number_of_cluster_members, group=theresholds_id, col=theresholds_id)) + stat_ecdf(geom = "step", pad=FALSE) +
  scale_color_manual(values=c("#022857", "#223e92", "#1576bb", "#458ccc", "#6aa6da", "#96c0e6", "#9acfe6", "#9ddceb", "#355E3B", "#152238", "#087E16", "#168E25", "#2CAC3C", "#43C152", "#5CD16A", "#7DE089", "#AFFAB8", "#D9D608", "#E8E62B",'#FFFF8F', "#F7F469"), name='Clustering \nThreshold (%)') +
  scale_x_continuous(breaks = seq(0, 3600, 200), name ="Cluster Size") +
  coord_cartesian(ylim = c(.98, 1)) +
  stat_ecdf(geom = "step", pad = FALSE, size = 1.5) + ylab("Proportion")  +
  theme()+ 
  guides(color = guide_legend(ncol = 1, title.position = "top", title.hjust = 1, title.vjust = 1,
                              label.position = "right", label.hjust = 1, label.vjust = 1)) +
  theme(legend.text = element_text(size = 20), 
        legend.title = element_text(size = 20), 
        legend.position = c(0.95, 0.05), 
        legend.justification = c(1, 0), 
        legend.box.just = "right",
        axis.title.x = element_text(size = 20),  # Adjust x-axis label size
        axis.title.y = element_text(size = 20),  # Adjust y-axis label size
        axis.text.x = element_text(size = 15),   # Adjust x-axis tick label size
        axis.text.y = element_text(size = 15))   # Adjust y-axis tick label size
plot(p)
dev.off()


#Generate supplementary file 8. Empirical plot of unique taxID at all clustering theresholds
pdf(file='../supplementary_file_8.pdf', width=12, height=8)
p<-ggplot(df, aes(x=unique_number_of_cluster_members, group=theresholds_id, col=theresholds_id)) + stat_ecdf(geom = "step", pad=FALSE) +
  scale_color_manual(values=c("#022857", "#223e92", "#1576bb", "#458ccc", "#6aa6da", "#96c0e6", "#9acfe6", "#9ddceb", "#355E3B", "#152238", "#087E16", "#168E25", "#2CAC3C", "#43C152", "#5CD16A", "#7DE089", "#AFFAB8", "#D9D608", "#E8E62B",'#FFFF8F', "#F7F469"), name='Clustering \nThreshold (%)') +
  xlim(0,100) + xlab("Unique taxID") +
  coord_cartesian(ylim = c(.98, 1)) +
  stat_ecdf(geom = "step", pad = FALSE, size = 1.5) + ylab("Proportion")  +
  theme()+ 
  guides(color = guide_legend(ncol = 1, title.position = "top", title.hjust = 1, title.vjust = 1,
                              label.position = "right", label.hjust = 1, label.vjust = 1)) +
  theme(legend.text = element_text(size = 20), 
        legend.title = element_text(size = 20), 
        legend.position = c(0.95, 0.05), 
        legend.justification = c(1, 0), 
        legend.box.just = "right",
        axis.title.x = element_text(size = 20),  # Adjust x-axis label size
        axis.title.y = element_text(size = 20),  # Adjust y-axis label size
        axis.text.x = element_text(size = 20),   # Adjust x-axis tick label size
        axis.text.y = element_text(size = 20))   # Adjust y-axis tick label size
plot(p)
dev.off()



# Generate Figure 2. Number of unique taxID in clusters vs proportion of all clusters
data2 <- df[df$theresholds_id %in% c('100%', '99.5%', '99%', '98.5%', '98%'), ]

data2$theresholds_id <- factor(data2$theresholds_id, levels=c('100%', '99.5%', '99%', '98.5%', '98%'))

pdf(file='Fig_2.pdf', width=12, height=8)
p <- ggplot(data2, aes(x=unique_number_of_cluster_members, group=theresholds_id, col=theresholds_id, linetype=theresholds_id)) + 
  stat_ecdf(geom = "step", pad=FALSE, size = 1.5) +  # Make lines thicker by setting size
  xlim(0, 100) + xlab("Unique taxID") +
  coord_cartesian(ylim = c(.98, 1)) +
  ylab("Proportion") +
  theme() + 
  scale_color_manual(name='Clustering \nThreshold (%)',
                     values=c('#F0E442', '#009E73', '#56B4E9', '#E69F00', '#152238')) +
  scale_linetype_manual(name='Clustering \nThreshold (%)',
                        values=c('solid', 'solid', 'solid', 'solid', 'solid')) +  # Specify line types
  guides(color = guide_legend(ncol = 1, title.position = "top", title.hjust = 1, title.vjust = 1,
                              label.position = "right", label.hjust = 1, label.vjust = 1)) +
  theme(legend.text = element_text(size = 30), 
        legend.title = element_text(size = 32), 
        legend.position = c(0.95, 0.05), 
        legend.justification = c(1, 0), 
        legend.box.just = "right",
        axis.title.x = element_text(size = 20),  # Adjust x-axis label size
        axis.title.y = element_text(size = 20),  # Adjust y-axis label size
        axis.text.x = element_text(size = 20),   # Adjust x-axis tick label size
        axis.text.y = element_text(size = 20))   # Adjust y-axis tick label size

plot(p)
dev.off()




#Generate Supplementary Figure 26. Total number of 16S rRNA copies per genome vs Total number of unique 16S rRNA copies per genome
data <- read.csv("genome_16S_info.csv") #Loading data

data <- data[!data$total_16S_copies %in% c(0,1), ] #Discarding genomes with a single 16S rRNA gene copy
print(data)
pdf(file='../supplementary_file_26.pdf', width=12, height=8)

p <- ggplot(data, aes(x=total_16S_copies, y=unique_16S_copies)) + 
  scale_x_continuous(breaks = seq(0, 12, 1), name ="16S rRNA copies per genome") +
  scale_y_continuous(name="Unique 16S rRNA copies per genome") + 
  geom_count(aes(colour=after_stat(n)), alpha=0.4)  + 
  scale_size_area(max_size=30, trans="identity") + 
  scale_color_viridis_c() +
  theme(legend.position = "none") + 
  coord_cartesian(clip = "off")
p + geom_text(data = ggplot_build(p)$data[[1]], 
              aes(x, y, label = n), color = "black")
dev.off()




#Generate Supplementary Figure 26.  Total number of 16S rRNA copies per genome vs Total number of unique 16S rRNA copies per genome for genomes at assmebly level complete or chromosome
data <- read.csv("genome_16S_info.csv") #Loading data
data <- data[!data$assembly_level %in% c('Contig', 'Scaffold'), ] #Discarding genomes with a single 16S rRNA gene copy
print(data)

pdf(file='../supplementary_file_27.pdf', width=12, height=8)

p <- ggplot(data, aes(x=total_16S_copies, y=unique_16S_copies)) + 
  scale_x_continuous(breaks = seq(0, 12, 1), name ="16S rRNA copies per genome") +
  scale_y_continuous(name="Unique 16S rRNA copies per genome") + 
  geom_count(aes(colour=after_stat(n)), alpha=0.4)  + 
  scale_size_area(max_size=30, trans="identity") + 
  scale_color_viridis_c() +
  theme(legend.position = "none") + 
  coord_cartesian(clip = "off")
p + geom_text(data = ggplot_build(p)$data[[1]], 
              aes(x, y, label = n), color = "black")
dev.off()



#Generate Figure 32. Total number of genomes per cluster vs NCBI names per cluster
data <- read.csv("genome_clusters_info.csv")
data <- data[!data$Total_genomes %in% c(1), ]
print(data)

pdf(file='../supplementary_file_32.pdf', width=15, height=10)

p <- ggplot(data, aes(x=Total_genomes, y=Unique_names_per_cluster)) + 
  scale_x_continuous(breaks = seq(0, 55, 2), name ="Number of genome per cluster") +
  scale_y_continuous(breaks = seq(0, 8, 2), name="Number of unique NCBI names per cluster") + 
  geom_count(aes(colour=after_stat(n)), alpha=0.4)  + 
  scale_size_area(max_size=30, trans="identity") + 
  scale_color_viridis_c() +
  theme(legend.position = "none") + 
  coord_cartesian(clip = "off")
p + geom_text(data = ggplot_build(p)$data[[1]], 
              aes(x, y, label = n), color = "black")

dev.off()



#Generate Fig 6. Genome coverage pyANI plots
data <- read.csv("pyani_analysis_coverage_identity_representative.csv")

data2 <- data[!data$unique_taxa_names %in% c('6', '5','4', '3'), ]
data3 <- data[!data$unique_taxa_names %in% c('1', '2'), ]
pdf(file='Fig_6.pdf', width=30, height=15)


p1<-ggplot(data2, aes(x=cluster_id, y=coverage, col=comparision_type_species)) +
  geom_jitter(alpha=0.2)  + 
  facet_wrap(unique_taxa_names ~., scales = 'free_x', nrow=7, shrink=FALSE, dir='h') + 
  scale_y_continuous(name="Genome Coverage (%)") +
  scale_x_continuous(breaks = seq(0, 160, 10), name ="") + theme(legend.position="none") + ylim(0.25, 1) +
  geom_hline(yintercept = 0.5, linetype = "dashed", color = "red") 

p2<-ggplot(data3, aes(x=cluster_id, y=coverage, col=comparision_type_species)) +
  geom_jitter(alpha=0.2) + 
  geom_rect(data = subset(data3,unique_taxa_names == '6'), fill = NA, colour = "red", xmin = 1.5,xmax = 2.5,
            ymin = 0.3,ymax = 1,alpha = 0.1) +
  facet_wrap(unique_taxa_names ~., scales = 'free_x', nrow=1, shrink=TRUE, dir='h') + scale_y_continuous(name="") +
  scale_x_continuous(breaks = seq(0, 20, 2), name ="Cluster ID") + theme(legend.position="none")  + ylim(0.25, 1) +
  geom_hline(yintercept = 0.5, linetype = "dashed", color = "red") 

p4<-ggarrange(p1, p2,
              ncol = 1, nrow = 2, heights = c(2, 1, 1)) + 
  geom_rect(aes(xmin = -132, xmax = -69, ymin = 23, ymax = 49), color = "red", fill = NA) 
  
plot(p4)
dev.off()



#Generate Fig 12. Genome identity pyANI plots
pdf(file='Fig_12.pdf', width=30, height=15)

p1<-ggplot(data2, aes(x=cluster_id, y=identity, col=comparision_type_genus)) +geom_jitter(alpha=0.1)  + facet_wrap(unique_taxa_names ~., scales = 'free_x', nrow=7, shrink=TRUE, dir='h') + scale_y_continuous(name="Genome Identity (%)") +
  scale_x_continuous(breaks = seq(0, 160, 10), name ="") + theme(legend.position="none") +
  ylim(0.85, 1) +
  geom_hline(yintercept = 0.95, linetype = "dashed", color = "red") +
  scale_color_manual(values=c( "purple", "orange")) 

p2<-ggplot(data3, aes(x=cluster_id, y=identity, col=comparision_type_genus)) +geom_jitter(alpha=0.1) +
  
  geom_rect(data = subset(data3,unique_taxa_names == '6'), fill = NA, colour = "red", xmin = 1.5,xmax = 2.5,
            ymin = 0.86,ymax = 1,alpha = 0.1) +
  facet_wrap(unique_taxa_names ~., scales = 'free_x', nrow=1, shrink=TRUE, dir='h') + scale_y_continuous(name="") +
  scale_x_continuous(breaks = seq(0, 20, 2), name ="Cluster ID") + theme(legend.position="none")+
  ylim(0.85, 1) +
  geom_hline(yintercept = 0.95, linetype = "dashed", color = "red") +
  scale_color_manual(values=c( "purple", "orange")) 


p4<-ggarrange(p1, p2,
              ncol = 1, nrow = 2, heights = c(2, 1, 1))
plot(p4)
dev.off()




