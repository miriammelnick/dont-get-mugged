
###############################################################################
#
# WeatherByCenterPointSubgridSummarized
# Retrieve weather information for a rectangle defined by a center point and distances in the latitudinal and longitudinal directions.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class WeatherByCenterPointSubgridSummarized(Choreography):

    """
    Create a new instance of the WeatherByCenterPointSubgridSummarized Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NOAA/WeatherByCenterPointSubgridSummarized')


    def new_input_set(self):
        return WeatherByCenterPointSubgridSummarizedInputSet()

    def _make_result_set(self, result, path):
        return WeatherByCenterPointSubgridSummarizedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return WeatherByCenterPointSubgridSummarizedChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the WeatherByCenterPointSubgridSummarized
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class WeatherByCenterPointSubgridSummarizedInputSet(InputSet):
        """
        Set the value of the CenterPointLatitude input for this choreography. ((required, decimal) Enter the latitude specifying the rectangle or the grid center that defines the area being queried. North latitude is positive.)
        """
        def set_CenterPointLatitude(self, value):
            InputSet._set_input(self, 'CenterPointLatitude', value)

        """
        Set the value of the CenterPointLongitude input for this choreography. ((required, decimal) Enter the longitute specifying the rectangle or the grid center that defines the area being queried. West longitude is negative.)
        """
        def set_CenterPointLongitude(self, value):
            InputSet._set_input(self, 'CenterPointLongitude', value)

        """
        Set the value of the Format input for this choreography. ((required, string) Specify a timespan for which NDFD data will be summarized. Enter: 24 hourly, for a 24 hour summary, or: 12 hourly, for a 12 hour weather summary.)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the LatitudeDistance input for this choreography. ((required, decimal) Specify the distance from the center point in the latitudinal direction to the rectangle's East/West oriented sides.)
        """
        def set_LatitudeDistance(self, value):
            InputSet._set_input(self, 'LatitudeDistance', value)

        """
        Set the value of the LongitudeDistance input for this choreography. ((required, decimal) Specify the distance from the center point in the longitudinal direction to the rectangle's North/South oriented side.)
        """
        def set_LongitudeDistance(self, value):
            InputSet._set_input(self, 'LongitudeDistance', value)

        """
        Set the value of the NumberOfDays input for this choreography. ((optional, integer) Specify the number of days to retieve data for. If null, data from the earliest date in the dabase is returned.)
        """
        def set_NumberOfDays(self, value):
            InputSet._set_input(self, 'NumberOfDays', value)

        """
        Set the value of the SquareResolution input for this choreography. ((optional, decimal) Enter desired data resolution in kilometers.  Default is 5km.)
        """
        def set_SquareResolution(self, value):
            InputSet._set_input(self, 'SquareResolution', value)

        """
        Set the value of the StartDate input for this choreography. ((optional, date) Enter the start time for retrieval of NDWD data in following format: 2004-04-27 If null, the earliest date in the database is returned.)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the Unit input for this choreography. ((optional, string) Enter the unit format the data will be displayed in. Default is: e, for Standard English (U.S. Standard).  Or: m, for Metric (SI Units).)
        """
        def set_Unit(self, value):
            InputSet._set_input(self, 'Unit', value)


"""
A ResultSet with methods tailored to the values returned by the WeatherByCenterPointSubgridSummarized choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class WeatherByCenterPointSubgridSummarizedResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Response from NDFD servers.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class WeatherByCenterPointSubgridSummarizedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return WeatherByCenterPointSubgridSummarizedResultSet(response, path)
