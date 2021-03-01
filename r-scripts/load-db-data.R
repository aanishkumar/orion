library(DBI)
library(RSQLite)

connection <- dbConnect(SQLite(), "~/orion/hmdata.sqlite")
db_data <- dbReadTable(connection, "data")

View(db_data)
