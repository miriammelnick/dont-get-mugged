
###############################################################################
#
# WeatherByCitiesUnsummarized
# Retrieve weather information for a specific list of cities.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class WeatherByCitiesUnsummarized(Choreography):

    """
    Create a new instance of the WeatherByCitiesUnsummarized Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NOAA/WeatherByCitiesUnsummarized')


    def new_input_set(self):
        return WeatherByCitiesUnsummarizedInputSet()

    def _make_result_set(self, result, path):
        return WeatherByCitiesUnsummarizedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return WeatherByCitiesUnsummarizedChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the WeatherByCitiesUnsummarized
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class WeatherByCitiesUnsummarizedInputSet(InputSet):
        """
        Set the value of the CitiesLevel input for this choreography. ((required, integer) Enter a city grouping number. For example: enter 1, to obtain weather information for primary U.S. cities. See documentation for additional numbers.)
        """
        def set_CitiesLevel(self, value):
            InputSet._set_input(self, 'CitiesLevel', value)

        """
        Set the value of the EndDate input for this choreography. ((required, date) Enter the end time for retrieval of NDWD information in UTC format. Time must be today's date, or a future date.  Format: 2004-04-27T12:00.)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the NDFDParameterName input for this choreography. ((optional, string) Enter an additional weather parameter in the following format: phail=phail. Use only if Product is set to: glance.)
        """
        def set_NDFDParameterName(self, value):
            InputSet._set_input(self, 'NDFDParameterName', value)

        """
        Set the value of the Product input for this choreography. ((required, string) Enter one of two parameters: time-series (to return all data between the Begin and End time parameters); glance for a subset of 5 often used parameters)
        """
        def set_Product(self, value):
            InputSet._set_input(self, 'Product', value)

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
A ResultSet with methods tailored to the values returned by the WeatherByCitiesUnsummarized choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class WeatherByCitiesUnsummarizedResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Response from NDFD servers.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class WeatherByCitiesUnsummarizedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return WeatherByCitiesUnsummarizedResultSet(response, path)
