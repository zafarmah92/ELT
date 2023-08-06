## Installation Jupyter notebook in Conda env 
    conda install -n <env> ipykernel
## Installation of pyspark in conda 
    1. conda install openjdk
    2. conda install pyspark
    3. conda install -c conda-forge findspark
    4. check pyspark 
## Some Pyspark functions 
    df.select(...) \
        . filter(...) \ 

    ##  UDF's (User defined Functions)
    
    from pyspark.sql import functions as F 
    
    ## for example
    
    df \
        .withcolumns('pickup_date', F.to_date(df.pickup_date)) \
        .withcolumns('dropof_date', F.to_date(df.dropof_date)) \
        .select (....) \
        .show()



