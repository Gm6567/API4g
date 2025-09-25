from django.core.management.base import BaseCommand, CommandError
from addressApplication.models import OperatorTable
from addressApplication.functions import lamber93_to_gps
import pandas as pd

'''
This command is launched once at database initialization.
It takes the content of data_operator.csv file and insert the data in the operator_table
whose fields are defined in models.py
'''
class Command(BaseCommand):
    help = "Get Lambert93 data from CSV file"

    def handle(self, *args, **options):
        path = "data_lambert93/data_operator.csv"
        if len(OperatorTable.objects.all()) > 0:
            self.stdout.write(self.style.WARNING("Data in Lambert93 table is not empty"))
            return
        try:
            df = pd.read_csv(path)
        except Exception as e:
            raise CommandError("Unable to read the CSV file")
        if df.empty:
            self.stdout.write(self.style.WARNING("No data in CSV File"))
            return
        df["long"], df["lat"] = zip(*[lamber93_to_gps(x, y) 
                                    for x, y in zip(df["x"], df["y"])])
        df = df.drop(columns=["x","y"])
        df = df.rename(columns={"Operateur": "operator_name",
                                "2G": "is_2g",
                                "3G": "is_3g",
                                "4G": "is_4g"
                                }
                       )
        objs = [OperatorTable(**row.dropna().to_dict()) for _, row in df.iterrows()]
        OperatorTable.objects.bulk_create(objs, batch_size=1000)
        self.stdout.write(self.style.SUCCESS("{} lines have been inserted in the database".format(len(objs))))
        
