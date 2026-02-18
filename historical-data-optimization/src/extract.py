import pandas as pd
from database import connect

def extract_historical_data(start_date, end_date):

    query = f"""
        SELECT
            T.OPERATION_DATE AS DATE,
            T.PRODUCT_ID,
            T.STORE_ID,
            SUM(T.QUANTITY) AS TOTAL_QTY,
            SUM(T.NET_SALES) AS NET_SALES
        FROM SALES_FACT T
        WHERE T.OPERATION_DATE >= DATE '{start_date}'
          AND T.OPERATION_DATE <  DATE '{end_date}'
        GROUP BY 
            T.OPERATION_DATE,
            T.PRODUCT_ID,
            T.STORE_ID
    """

    conn = connect()
    df = pd.read_sql(query, conn)
    conn.close()

    return df
