import pandas as pd
import numpy as np
from pandas import DataFrame
from sqlalchemy import insert
from sqlalchemy import text

from .session import engine
from .types import FormulaOneTableSchema


class DataLoaders:


    def truncate_table(self, model_class: FormulaOneTableSchema) -> None:
        '''Truncate (empty) a table. Use with caution'''
        table_name = model_class.__tablename__
        with engine.begin() as conn:
            conn.execute(text(
                f'TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE')
                )
        

    def clean_df_for_insert(self, df: DataFrame) -> DataFrame:
        '''Clean DataFrame for PostgreSQL insertion.'''
        df = df.copy()
        
        for col in df.columns:
            # Replace pandas NaT and NaN with None
            df[col] = df[col].replace({pd.NaT: None, np.nan: None})
            
            # Convert any remaining numpy types to Python native types
            if df[col].dtype == 'datetime64[ns]':
                df[col] = df[col].apply(lambda x: x.to_pydatetime() if pd.notna(x) else None)
        
        return df


    def bulk_data_insert_from_df(
            self,
            df: DataFrame,
            model_class: FormulaOneTableSchema,
            chunk_size:int = 10000) -> int:
        
        model_columns = [col.key for col in model_class.__table__.columns]
        rename_map = dict(zip(df.columns, model_columns))
        
        df = df.rename(columns=rename_map)

        df_clean = self.clean_df_for_insert(df)

        records = df_clean.to_dict(orient='records')
        total = 0

        with engine.begin() as conn:
            for i in range(0, len(records), chunk_size):
                chunk = records[i:i + chunk_size]
                stmt = insert(model_class).values(chunk)
                conn.execute(stmt)
                total += len(chunk)

        return total
    
data_loader = DataLoaders()


# if __name__ == '__main__':
#     raise SystemExit()
