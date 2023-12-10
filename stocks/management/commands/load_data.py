import pandas as pd
from django.core.management.base import BaseCommand
from stocks.models import Stock

class Command(BaseCommand):
    help = 'Load stock data from CSV file into the database'

    def handle(self, *args, **options):
        file_path = 'D:/stockProject/stockMarket/stock_market_data.csv'  

        try:
            
            df = pd.read_csv(file_path)

            
            numeric_fields = ['high', 'low', 'open', 'close', 'volume']
            for field in numeric_fields:
                df[field] = df[field].str.replace(',', '')

            
            for index, row in df.iterrows():
                Stock.objects.create(
                    date=row['date'],
                    trade_code=row['trade_code'],
                    high=float(row['high']),  
                    low=float(row['low']),    
                    open=float(row['open']),   
                    close=float(row['close']), 
                    volume=int(row['volume'])   
                )

            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))