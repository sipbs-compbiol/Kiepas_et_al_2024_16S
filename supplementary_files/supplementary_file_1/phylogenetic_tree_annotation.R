#This script was used to generate annotated 16S tree for main and supplementary material. 

#Set Up
library("ape")
library(RColorBrewer)
library(dplyr)
library('ggplot2')
library('ggtree')
library(ggnewscale)
library("phytools")
library(tidytree)



#Generate tree
gettreedata <- function(tree, meta){
  #get treedata object
  d<-meta[row.names(meta) %in% tree$tip.label,]
  d$label <- row.names(d)
  y <- full_join(as_tibble(tree), d, by='label')
  y <- as.treedata(y)
  return(y)
}

get_color_mapping <- function(data, col, cmap){
  labels <- (data[[col]])   
  names <- levels(as.factor(labels))
  n <- length(names)
  if (n<10){      
    colors <- suppressWarnings(c(brewer.pal(n, cmap)))[1:n]
  }
  else {
    colors <- colorRampPalette(brewer.pal(8, cmap))(n)
  }
  names(colors) = names
  return (colors)
}

ggplottree <- function(tree, meta, cols=NULL, cmaps=NULL, layout="rectangular",
                       offset=10, tiplabel=FALSE, tipsize=1) {
  
  y <- gettreedata(tree, meta)
  p <- ggtree(y, layout=layout, ladderize = TRUE, size=0.2) + geom_point2(aes(label=label,  subset = !is.na(as.numeric(label)) & as.numeric(label) == 1.1), colour='#008000', size=3)
  if (is.null(cols)){
    return (p)
  }
  
  col <- cols[1]
  cmap <- cmaps[1]
  df<-meta[tree$tip.label,][col]
  colors <- get_color_mapping(df, col, cmap)
  
  #tip formatting    
  p1 <- p + new_scale_fill() +geom_tippoint(mapping=aes(fill=.data[[col]]),size=tipsize,shape=22, stroke=NA) +
    scale_fill_manual(values=colors, na.value=NA, name='Species')
  
  p2 <- p1
  if (length(cols)>1){
    for (i in 2:length(cols)){
      col <- cols[i]
      cmap <- cmaps[i]
      df <- meta[tree$tip.label,][col]
      type <- class(df[col,])            
      p2 <- p2 + new_scale_fill()
      p2 <- gheatmap(p2, df, offset=i*offset, width=.15,
                     colnames_angle=0, colnames_offset_y = .05)  
      #deal with continuous values
      if (type == 'numeric'){               
        p2 <- p2 + scale_color_brewer(type="div", palette=cmap)
      }
      else {
        colors <- get_color_mapping(df, col, cmap)
        p2 <- p2 + scale_fill_manual(values=colors, name='Species') +theme(legend.position = "none")
      }          
    }
  }
  

  
  return(p2)
}



#Load data
tree <- ape::read.tree('collapsed_strep_tbe.new')
tree <- root(tree, outgroup = 'Streptoalloteichus_tenebrarius__COLLAPSED__id002124', resolve.root = TRUE)
df <- read.csv("phylogenetic_tree_data_annotation.csv", header=TRUE)


#Generate Figure 1. 
pdf(file = "../supplementary_file_1/Fig_1.pdf",   # The directory you want to save the file in
    width = 30, # The width of the plot in inches
    height = 30) # The height of the plot in inches
row.names(df) <- df$Name

p <- ggplottree(tree, df, cols=c('representative_disperions'),
                cmaps=c('Set1'), tipsize=5, offset=.05 ,layout='c') +
  geom_hilight(node=c(7496, 7280,7241,7478,7400,7338,7344,7392,2113,7390,7384,7380,7378,7369,2123,2125,2124, 6837,7004,1773,1606,7609,1780,7591,2380,1778,1779,1777,7587,2360,7023,7028,7031,7016,7037,2354,7035,7529,7054,7522,2295,2282,2281,1809,2285,2284,2283,2294,7519,7109,1870,2280,2276,7512,7119,7230), fill="red", extendto=0.54, alpha=0.2) +
  geom_hilight(node=c(6826,2434), fill="#1E88E5", extendto=0.5, alpha=0.2) +
  geom_hilight(node=c(7658), fill="#FFC107", extendto=0.54, alpha=0.2) +
  geom_hilight(node=c(7651,2425,2424,6833), fill="#1E88E5", extendto=0.54, alpha=0.2) +
  geom_strip('no_species_info_id001602', 'Streptomyces_variabilis__COLLAPSED__id001045', barsize=0, color='black', label="Clade 2", fontsize=10, angle=40, offset.text =-0.05, hjust=0.5) +
  geom_strip('Streptomyces_stelliscabiei__12__Streptomyces_sp.__11__Streptomyces_scabiei__6__id004463', 'no_species_info_id004839', barsize=0, color='black', label="Clade 3", fontsize=10, offset.text =-0.05, hjust=1) +
  geom_strip('Streptomyces_sp.__1__Streptomyces_bingchengensis__1__Streptomyces_bingchenggensis__1__id001604', 'Streptoalloteichus_tenebrarius__COLLAPSED__id002124', barsize=0, color='black', label="Clade 1",  fontsize=10, angle=-60, offset.text =-0.05, hjust=0.5) +
  geom_strip('no_species_info_id001602', 'Streptomyces_variabilis__COLLAPSED__id001045', barsize=2, color='white', label="", fontsize=10, angle=40, offset.text =-0.05, hjust=0.5) +
  geom_strip('Streptomyces_stelliscabiei__12__Streptomyces_sp.__11__Streptomyces_scabiei__6__id004463', 'no_species_info_id004839', barsize=2, color='white', label="", fontsize=10, offset.text =-0.05, hjust=-0.5) +
  geom_strip('Streptomyces_sp.__1__Streptomyces_bingchengensis__1__Streptomyces_bingchenggensis__1__id001604', 'Streptoalloteichus_tenebrarius__COLLAPSED__id002124', barsize=2, color='white', label="",  fontsize=10, angle=-60, offset.text =-0.05, hjust=0.5)+
  theme(legend.text = element_text(size = 40),  # Adjust legend text size
        legend.title = element_text(size = 42), # Adjust legend title size
        legend.position = c(0.2, 0.5))  # Move legend to the left

plot(p)
dev.off()




#Generate supplementary file 13. Tree with high dispersion of the same species names. 
pdf(file = "../supplementary_file_13.pdf",   # The directory you want to save the file in
    width = 30, # The width of the plot in inches
    height = 30) # The height of the plot in inches

row.names(df) <- df$Name

p <- ggplottree(tree, df, cols=c('disperse'),
                cmaps=c('Set1'), tipsize=5, offset=.05 ,layout='c') 
plot(p)
dev.off()


#Generate supplementary file 14. Tree with no dispersion of the same species names. 
pdf(file = "../supplementary_file_14.pdf",   # The directory you want to save the file in
    width = 30, # The width of the plot in inches
    height = 30) # The height of the plot in inches

row.names(df) <- df$Name

p <- ggplottree(tree, df, cols=c('no_dispersion'),
                cmaps=c('Set1'), tipsize=5, offset=.05 ,layout='c') 
plot(p)
dev.off()


#Generate supplementary file 15. Tree where not enough sequences with the same species names are avaiable. 
pdf(file = "../supplementary_file_15.pdf",   # The directory you want to save the file in
    width = 30, # The width of the plot in inches
    height = 30) # The height of the plot in inches

row.names(df) <- df$Name

p <- ggplottree(tree, df, cols=c('no_data'),
                cmaps=c('Set1'), tipsize=5, offset=.05 ,layout='c') 
plot(p)
dev.off()


#Generate supplementary file 16. Tree with mild dispersion of the same species names. 
pdf(file = "../supplementary_file_16.pdf",   # The directory you want to save the file in
    width = 30, # The width of the plot in inches
    height = 30) # The height of the plot in inches

row.names(df) <- df$Name

p <- ggplottree(tree, df, cols=c('slight_dispersion'),
                cmaps=c('Set1'), tipsize=5, offset=.05 ,layout='c') 
plot(p)
dev.off()

