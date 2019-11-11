# Numerical and categorical pattern visualization
# for a multi-class classification problem

# import required libraries
library(ggplot2)
library(dplyr)
library(ggpubr)

# ------- Numerical items --------

# function: one.numerical
# produces a scatter plot of a pattern with one numerical item, 
# indicating class and pattern support
# ----- Parameters
# data (data.frame): a data frame containing the data of the pattern
# pat (string): a vector string of length = 1, containing the pattern
#               to evaluate as a logical assertion
# var (string): a vector string of length = 1, containing the attribute
#               contained in the pattern
# class (string): a vector string of length = 1 indicating the class attribute
one.numerical <- function(data, pat, var, class) {
        data %>% mutate(pattern = ifelse(eval(parse(text = pat)), T,F)) %>%
                ggplot() + 
                geom_point(aes_string(x = var[1], 
                                      y = class,
                                      color = "pattern")) +
                labs(title = "Pattern representation", subtitle = pat) +
                scale_color_brewer(palette = "Set1")
}

# function: two.numerical
# produces a scatter plot of a pattern with two numerical items, 
# indicating class and pattern support
# ----- Parameters
# data (data.frame): a data frame containing the data of the pattern
# pat (string): a vector string of length = 2, containing the pattern
#               to evaluate as a logical assertion
# var (string): a vector string of length = 2, containing the attributes
#               contained in the pattern
# class (string): a vector string of length = 1 indicating the class attribute
two.numerical <- function(data, pat, var, class) {
        data %>% mutate(pattern = ifelse(eval(parse(text = pat[1])) & 
                                                 eval(parse(text = pat[2])), T,F)) %>%
                ggplot() + 
                geom_point(aes_string(x = var[1], 
                                      y = var[2],
                                      shape = class,
                                      color = "pattern")) +
                labs(title = "Pattern visualization", 
                     subtitle = paste(pat, collapse = " AND ")) +
                scale_color_brewer(palette = "Set1")
}

# function: three.numerical
# produces a scatter plot of a pattern with three numerical items, 
# indicating class and pattern support
# ----- Parameters
# data (data.frame): a data frame containing the data of the pattern
# pat (string): a vector string of length = 3, containing the pattern
#               to evaluate as a logical assertion
# var (string): a vector string of length = 3, containing the attributes
#               contained in the pattern
# class (string): a vector string of length = 1 indicating the class attribute
three.numerical <- function(data, pat, var, class) {
        data %>% mutate(pattern = ifelse(eval(parse(text = pat[1])) & 
                                                 eval(parse(text = pat[2])) &
                                                 eval(parse(text = pat[3])), T,F)) %>%
                ggplot() + 
                geom_point(aes_string(x = var[1], 
                                      y = var[2],
                                      size = var[3],
                                      shape = class,
                                      color = "pattern")) +
                labs(title = "Pattern visualization", 
                     subtitle = paste(pat, collapse = " AND ")) +
                scale_color_brewer(palette = "Set1")
}


# function: four.numerical
# produces a scatter plot of a pattern with three numerical items, 
# indicating class and pattern support
# ----- Parameters
# data (data.frame): a data frame containing the data of the pattern
# pat (string): a vector string of length = 4, containing the pattern
#               to evaluate as a logical assertion
# var (string): a vector string of length = 4, containing the attributes
#               contained in the pattern
# class (string): a vector string of length = 1 indicating the class attribute
four.numerical <- function(data, pat, var, class) {
        data %>% mutate(pattern = ifelse(eval(parse(text = pat[1])) & 
                                                 eval(parse(text = pat[2])) &
                                                 eval(parse(text = pat[3])), T,F)) %>%
                ggplot() + 
                geom_point(aes_string(x = var[1], 
                                      y = var[2],
                                      size = var[3],
                                      alpha = var[4],
                                      shape = class,
                                      color = "pattern")) +
                labs(title = "Pattern visualization", 
                     subtitle = paste(pat, collapse = " AND ")) +
                scale_color_brewer(palette = "Set1")
}




# ------- Categorical items -----------------

# function: one.categorical
# produces a scatter plot of a pattern with one categorical item, 
# indicating class and pattern support
# ----- Parameters
# data (data.frame): a data frame containing the data of the pattern
# pat (string): a vector string of length = 1, containing the pattern
#               to evaluate as a logical assertion
# var (string): a vector string of length = 1, containing the attribute
#               contained in the pattern
# class (string): a vector string of length = 1 indicating the class attribute
one.categorical <- function(data, pat, var, class) {
        data %>% mutate(pattern = ifelse(eval(parse(text = paste0("data$", pat))), T, F)) %>%
                select(c(var, "pattern", class)) %>%
                table %>%
                as.data.frame %>%
                ggballoonplot(x = var,
                              y = "pattern",
                              fill = "#0073C2FF",
                              color = "#0073C2FF",
                              size = "Freq", 
                              facet.by = class,
                              ggtheme = theme_bw()) +
                labs(title = "Pattern visualization",
                     subtitle = pat)
}


# function: two.categorical
# produces a scatter plot of a pattern with two categorical item, 
# indicating class and pattern support
# ----- Parameters
# data (data.frame): a data frame containing the data of the pattern
# pat (string): a vector string of length = 2, containing the pattern
#               to evaluate as a logical assertion
# var (string): a vector string of length = 2, containing the attributes
#               contained in the pattern
# class (string): a vector string of length = 1 indicating the class attribute
two.categorical <- function(data, pat, var, class) {
        data %>% mutate(pattern = ifelse(eval(parse(text = paste0("data$", pat[1]))) & eval(parse(text = paste0("data$", pat[2]))), T, F)) %>%
                select(c(var, "pattern", class)) %>%
                table %>%
                as.data.frame %>%
                ggballoonplot(x = var[1],
                              y = var[2],
                              color = "pattern",
                              fill = "white",
                              size = "Freq", 
                              facet.by = class,
                              ggtheme = theme_bw()) +
                scale_color_brewer(palette = "Set1") +
                labs(title = "Pattern visualization",
                     subtitle = paste(pat, collapse = " AND "))
}

# function: three.categorical
# produces a scatter plot of a pattern with three categorical item, 
# indicating class and pattern support
# ----- Parameters
# data (data.frame): a data frame containing the data of the pattern
# pat (string): a vector string of length = 3, containing the pattern
#               to evaluate as a logical assertion
# var (string): a vector string of length = 3, containing the attributes
#               contained in the pattern
# class (string): a vector string of length = 1 indicating the class attribute
three.categorical <- function(data, pat, var, class) {
        data %>% mutate(pattern = ifelse(eval(parse(text = paste0("data$", pat[1]))) & 
                                                 eval(parse(text = paste0("data$", pat[2]))) &
                                                 eval(parse(text = paste0("data$", pat[3]))), T, F)) %>%
                select(c(var, "pattern", class)) %>%
                table %>%
                as.data.frame %>%
                ggballoonplot(x = var[1],
                              y = var[2],
                              shape = var[3],
                              size = "Freq", 
                              color = "pattern",
                              facet.by = class,
                              ggtheme = theme_bw()) +
                scale_color_brewer(palette = "Set1") +
                labs(title = "Pattern visualization",
                     subtitle = paste(pat, collapse = " AND "))
}


# function: four.categorical
# produces a scatter plot of a pattern with four categorical item, 
# indicating class and pattern support
# ----- Parameters
# data (data.frame): a data frame containing the data of the pattern
# pat (string): a vector string of length = 4, containing the pattern
#               to evaluate as a logical assertion
# var (string): a vector string of length = 4, containing the attributes
#               contained in the pattern
# class (string): a vector string of length = 1 indicating the class attribute
four.categorical <- function(data, pat, var, class) {
        data %>% mutate(pattern = ifelse(eval(parse(text = paste0("data$", pat[1]))) & 
                                                 eval(parse(text = paste0("data$", pat[2]))) &
                                                 eval(parse(text = paste0("data$", pat[3]))) &
                                                 eval(parse(text = paste0("data$", pat[4]))), T, F)) %>%
                select(c(var, "pattern", class)) %>%
                table %>%
                as.data.frame %>%
                ggballoonplot(x = var[1],
                              y = var[2],
                              shape = var[3],
                              size = "Freq", 
                              color = var[4],
                              facet.by = c(class,"pattern"),
                              ggtheme = theme_bw()) +
                scale_color_brewer(palette = "Set1") + 
                labs(title = "Pattern visualization",
                     subtitle = paste(pat, collapse = " AND "))
}


# -------- Examples -----
data <- read.csv("automobile_price.csv", header = T)
# one numerical item
var <- "curb.weight"
pat <- "curb.weight <= 2006.00"
class <- "price"
one.numerical(data, pat, var, class)

# two numerical items
pat <- c("city.mpg > 29.50 ", "stroke <= 3.26")
var <- c("city.mpg", "stroke")
two.numerical(data, pat, var, class)

#three numerical items
var <- c("engine.size", "compression.ratio", "highway.mpg") 
pat <- c("engine.size > 125.50 ", "compression.ratio > 7.25 ", "highway.mpg <= 27.50")
three.numerical(data, pat, var, class)

# four numerical items
pat <- c("highway.mpg <= 28.50 ", "engine.size > 125.50", "compression.ratio > 7.25", "symboling > -1.50")
var <- c("highway.mpg", "engine.size", "compression.ratio", "symboling")
four.numerical(data, pat, var, class)

# one categorical item
pat <- "num.of.cylinders != 'four'"
var <- "num.of.cylinders"
one.categorical(data, pat, var, class)

# two categorical items
pat <- c("body.style != 'hatchback'", "num.of.cylinders != 'four'")
var <- c("body.style", "num.of.cylinders")
two.categorical(data, pat, var, class)

# three categorical items
pat <- c("num.of.cylinders == 'four'", "drive.wheels != 'rwd' ", "fuel.system == 'mpfi'")        
var <- c("num.of.cylinders", "fuel.system", "drive.wheels")
three.categorical(data, pat, var, class)

# four categorical items
var <- c("num.of.cylinders", "fuel.system", "drive.wheels", "num.of.doors")
pat <- c("num.of.cylinders == 'four'", "fuel.system == '2bbl' ", "drive.wheels == 'fwd' ", "num.of.doors == 'four'")
four.categorical(data, pat, var, class)
