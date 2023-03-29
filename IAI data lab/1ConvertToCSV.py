from numpy.core import numeric
import pandas as pd
import numpy as np
import os

dir_rpt = "change path to the RPT files"

dir_csv = "change path to the output folder"

dir_sensorlist = "change to path to the selected_sensors_bigger_list.csv"

directory = os.fsencode(dir_rpt)

i=1    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    df = pd.read_csv('{}/{}'.format(dir_rpt,filename),names=["ignore1", "time", "sensor", "value", "ignore2"],encoding = "ISO-8859-1")
    df = df.filter(items=['time', 'sensor', 'value'])
    sensors = pd.read_csv('{}/selected_sensors_bigger_list.csv'.format(dir_sensorlist))
    sensors_id_list = sensors['Sensor_id'].tolist()
    df = df[df['sensor'].isin(sensors_id_list)]
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.dropna()
    df = df.pivot_table(values="value", index="time", columns="sensor")
    df.to_csv('{}/{}.csv'.format(dir_csv,i))
    i=i+1
