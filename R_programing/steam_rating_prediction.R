## Intro ----
library(tidyverse)
library(caret)
library(scales)
df <- read.csv(url("https://raw.githubusercontent.com/Sirrender-krr/dsb-batch10/refs/heads/main/R_programing/game_data_all.csv"))
## https://www.kaggle.com/datasets/whigmalwhim/steam-releases/data

## inspect data
glimpse(df)
check_na <- function(data){
  sum_na <- data.frame()
  x <- ncol(data)
  for (i in 1:x) {
    output <- c(names(data[i]),sum(is.na(data[i])))
    sum_na <- rbind(sum_na,output)
  }
  colnames(sum_na) <- c("Columns","Count_na")
  print(sum_na)
}
check_na(df)


## drop unneccesary
df$X <- NULL
df$game <- NULL
df$link <- NULL
df$release <- NULL
df$primary_genre <- NULL
df$store_genres <- NULL
df$publisher <- NULL
df$developer <- NULL
df$detected_technologies <- NULL
df$store_asset_mod_time <- NULL
df$players_right_now <- NULL
df$X24_hour_peak <- NULL
df$all_time_peak_date <- NULL
df$review_percentage <- NULL
df$all_time_peak <- NULL
glimpse(df)

## Train Test Split ----
## Split
split_data <- function(data){
  set.seed(934)
  n <- nrow(data)
  id <- sample(1:n, size = n*0.8)
  train_df <- data[id,]
  test_df <- data[-id,]
  return(list(train=train_df,test =test_df))
}
prep_df <- split_data(df)

## train using linear regression----
set.seed(3)
ctrl <- trainControl(method='cv',
                     number=5,
                     verboseIter=TRUE)
lm_fit <- train(rating ~ .,
      data=prep_df$train,
      method='lm',
      metric='RMSE',
      trControl=ctrl)
print(lm_fit)

## train using knn regression (2nd)----
set.seed(3)
ctrl <- trainControl(method='cv',
                     number=5,
                     verboseIter=TRUE)
knn_model <- train(rating ~ .,
                data=prep_df$train,
                method='knn',
                metric='RMSE',
                trControl=ctrl)
print(knn_model)


## train using Decision tree regression----
set.seed(3)
ctrl <- trainControl(method='cv',
                     number=10,
                     verboseIter=TRUE)
tree_model <- train(rating ~ .,
                  data=prep_df$train,
                  method='rpart',
                  metric='RMSE',
                  trControl=ctrl)
print(tree_model)


## train using random forest regression (winner) ----
set.seed(3)
ctrl <- trainControl(method='cv',
                     number=5,
                     verboseIter=TRUE)
rf_model <- train(rating ~ .,
                data=prep_df$train,
                method='rf',
                metric='RMSE',
                trControl=ctrl)
print(rf_model)

## test ----
## KNN test
knn_p <- predict(knn_model,newdata=prep_df$test)
print(knn_model)
postResample(pred=knn_p,obs=prep_df$test$rating)

## Random Forest test
rf_p <- predict(rf_model, newdata=prep_df$test)
print(rf_model)
postResample(pred=rf_p,obs=prep_df$test$rating)

## testing whole data set ----
p_df <- predict(rf_model,newdata=df)
postResample(pred=p_df,obs=df$rating)

## save the model----
saveRDS(rf_model, file= 'steam_rating_model.RDS')

#----


