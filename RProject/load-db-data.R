library(DBI)
library(RSQLite)


connection <- dbConnect(SQLite(), "../data.sqlite")
db_data <- dbReadTable(connection, "data")

View(db_data)
