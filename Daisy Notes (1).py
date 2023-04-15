# Databricks notebook source
print("Hello World")

# COMMAND ----------

# MAGIC %run ./Setup

# COMMAND ----------

print(name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
display(files)


# COMMAND ----------

dis
