import os
from extract import extract_historical_data

def main():

    start_date = "2024-01-01"
    end_date = "2026-01-01"

    df = extract_historical_data(start_date, end_date)

    print("Linhas retornadas:", len(df))

    os.makedirs("data", exist_ok=True)

    file_name = f"data/historical_sales_{start_date}_{end_date}.parquet"
    df.to_parquet(file_name, index=False)

    print("gerado com sucesso:", file_name)


if __name__ == "__main__":
    main()
