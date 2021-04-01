# Create your views here.
from django.shortcuts import render
from django.views.generic import View

from datetime import datetime, date

from rest_framework.views import APIView
from rest_framework.response import Response

from pandas import read_csv
import numpy as np

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart/index.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    
    def timestring_to_number_of_seconds(self, timestring):
        timestring_parts = timestring.split(":")
        hours_in_seconds = int(timestring_parts[0]) * 3600 # hours * number of seconds in one hour
        minutes_in_seconds = int(timestring_parts[1]) * 60 # minutes * number of seconds in one minute
        seconds = int(timestring_parts[2])
        
        return hours_in_seconds + minutes_in_seconds + seconds
        
    def get(self, request, format = None):

        df = read_csv("../data/log.csv")
        df1 = df.replace(np.nan, '', regex=True)

        labelsX = []
        chartdataX = []
        
        chartdataTwo = []
        chartdataThree = []
        
        for index, row in df1.iterrows():
            
            if index == len(df.index)-1:
                break
            
            start_cell_as_string_list = row['start'].split("-")
            shutdown_cell_as_string_list = row['shutdown'].split("-")
            
            start_date_string = start_cell_as_string_list[0]
            shutdown_date_string = shutdown_cell_as_string_list[0]
            
            start_time_string = ""
            shutdown_time_string = shutdown_cell_as_string_list[1]
            
            if index != 0:
                start_time_string = start_cell_as_string_list[1]
                                        
            shutdown_time_in_seconds_of_the_day = self.timestring_to_number_of_seconds(shutdown_time_string)
            
            one_row_ahead = df1.iloc[index + 1]
            one_row_ahead_start_cell_as_string_list = one_row_ahead['start'].split("-")
            
            one_row_ahead_start_date_string = one_row_ahead_start_cell_as_string_list[0]
            
            one_row_ahead_start_time_string = one_row_ahead_start_cell_as_string_list[1]
            next_start_time_in_seconds_of_the_day = self.timestring_to_number_of_seconds(one_row_ahead_start_time_string)
            the_downtime_timespan = [shutdown_time_in_seconds_of_the_day, next_start_time_in_seconds_of_the_day]
            
            if shutdown_date_string != one_row_ahead_start_date_string:
                the_downtime_timespan = [0, next_start_time_in_seconds_of_the_day]
                # time max per day = seconds in one day = 86400
                the_downtime_timespan_day_before = [shutdown_time_in_seconds_of_the_day, 86400]
                if(len(labelsX) > 0 and shutdown_date_string == labelsX[-1]):
                    if chartdataTwo[-1] != 0:
                        # append to chartdataThree
                        chartdataThree[-1] = the_downtime_timespan_day_before
                    else:
                        # append to chartdataTwo
                        chartdataTwo[-1] = the_downtime_timespan_day_before
                else:
                    chartdataX.append(the_downtime_timespan_day_before)

                
            
            
            if(len(labelsX) > 0 and one_row_ahead_start_date_string == labelsX[-1]):
                if chartdataTwo[-1] != 0:
                    # append to chartdataThree
                    chartdataThree[-1] = the_downtime_timespan
                else:
                    # append to chartdataTwo
                    chartdataTwo[-1] = the_downtime_timespan
            else:
                chartdataX.append(the_downtime_timespan)
                labelsX.append(one_row_ahead_start_date_string)
                chartdataTwo.append(0)
                chartdataThree.append(0)
        
        chartLabel = "my data"

        data = {
                     "labels":labelsX,
                     "chartLabel":chartLabel,
                     "chartdata":chartdataX,
                     "chartdataTwo": chartdataTwo,
                     "chartdataThree": chartdataThree

             }
             
        return Response(data)
