
###############################################################################
#
# WeatherForPointsOnLineSummarized
# Retrieve weather information for all points on a line defined by a set of latitude and longitude coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class WeatherForPointsOnLineSummarized(Choreography):

    """
    Create a new instance of the WeatherForPointsOnLineSummarized Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NOAA/WeatherForPointsOnLineSummarized')


    def new_input_set(self):
        return WeatherForPointsOnLineSummarizedInputSet()

    def _make_result_set(self, result, path):
        return WeatherForPointsOnLineSummarizedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return WeatherForPointsOnLineSummarizedChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the WeatherForPointsOnLineSummarized
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class WeatherForPointsOnLineSummarizedInputSet(InputSet):
        """
        Set the value of the Endpoint1Latitude input for this choreography. ((required, integer) Enter the latitude of the first endpoint of the line for which weather data is requested. North latitude is positive.)
        """
        def set_Endpoint1Latitude(self, value):
            InputSet._set_input(self, 'Endpoint1Latitude', value)

        """
        Set the value of the Endpoint1Longitude input for this choreography. ((required, integer) Enter the longitude of the first endpoint of the line for which weather data is requested. West longitude is negative.)
        """
        def set_Endpoint1Longitude(self, value):
            InputSet._set_input(self, 'Endpoint1Longitude', value)

        """
        Set the value of the Endpoint2Latitude input for this choreography. ((required, integer) Enter the latitude of the second endpoint of the line for which weather data is requested. North latitude is positive.)
        """
        def set_Endpoint2Latitude(self, value):
            InputSet._set_input(self, 'Endpoint2Latitude', value)

        """
        Set the value of the Endpoint2Longitude input for this choreography. ((required, integer) Enter the longitude of the second endpoint of the line for which weather data is requested. West longitude is negative.)
        """
        def set_Endpoint2Longitude(self, value):
            InputSet._set_input(self, 'Endpoint2Longitude', value)

        """
        Set the value of the Format input for this choreography. ((required, string) Specify a timespan for which NDFD data will be summarized. Enter: 24 hourly, for a 24 hour summary, or: 12 hourly, for a 12 hour weather summary.)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the NumberOfDays input for this choreography. ((optional, integer) Specify the number of days to retieve data for. If null, data from the earliest date in the dabase is returned.)
        """
        def set_NumberOfDays(self, value):
            InputSet._set_input(self, 'NumberOfDays', value)

        """
        Set the value of the StartDate input for this choreography. ((optional, date) Enter the start time for retrieval of NDWD information in UTC format. If null, the earliest date in the database is returned. Format: 2004-04-27T12:00.)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the Unit input for this choreography. ((optional, string) Enter the unit format the data will be displayed in. Default is: e, for Standard English (U.S. Standard).  Or: m, for Metric (SI Units).)
        """
        def set_Unit(self, value):
            InputSet._set_input(self, 'Unit', value)


"""
A ResultSet with methods tailored to the values returned by the WeatherForPointsOnLineSummarized choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class WeatherForPointsOnLineSummarizedResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Response from NDFD servers.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class WeatherForPointsOnLineSummarizedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return WeatherForPointsOnLineSummarizedResultSet(response, path)
