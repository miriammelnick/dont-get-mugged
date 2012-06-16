
###############################################################################
#
# SalesPercentiles
# Retrieves percentiles of real estate sales from New York Times Web Service.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SalesPercentiles(Choreography):

    """
    Create a new instance of the SalesPercentiles Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/RealEstate/SalesPercentiles')


    def new_input_set(self):
        return SalesPercentilesInputSet()

    def _make_result_set(self, result, path):
        return SalesPercentilesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SalesPercentilesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SalesPercentiles
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SalesPercentilesInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) The API Key provided by NY Times)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Bedrooms input for this choreography. ((optional, integer) Limits the results by number of bedrooms to search for. Defaults to 1.)
        """
        def set_Bedrooms(self, value):
            InputSet._set_input(self, 'Bedrooms', value)

        """
        Set the value of the DateRange input for this choreography. ((string) Sets the quarter, month, week or day for the results (i.e. 2008-Q1, 2008-W52, 2007-07, etc))
        """
        def set_DateRange(self, value):
            InputSet._set_input(self, 'DateRange', value)

        """
        Set the value of the GeoExtentLevel input for this choreography. ((string) The geographical unit for the results (i.e. borough, neighborhood, or zip))
        """
        def set_GeoExtentLevel(self, value):
            InputSet._set_input(self, 'GeoExtentLevel', value)

        """
        Set the value of the GeoExtentValue input for this choreography. ((string) Limits the search to a specific area.  For example, if GeoExtendLevel is borough, the value for GeoExtendValue could be Brooklyn.)
        """
        def set_GeoExtentValue(self, value):
            InputSet._set_input(self, 'GeoExtentValue', value)

        """
        Set the value of the GeoSummaryLevel input for this choreography. ((string) The geographic unit for grouping the results (borough, neighborhood, or zip))
        """
        def set_GeoSummaryLevel(self, value):
            InputSet._set_input(self, 'GeoSummaryLevel', value)

        """
        Set the value of the Percentile input for this choreography. ((integer) Specify the percentile for sales prices you want to retrieve (i.e 50))
        """
        def set_Percentile(self, value):
            InputSet._set_input(self, 'Percentile', value)


"""
A ResultSet with methods tailored to the values returned by the SalesPercentiles choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SalesPercentilesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from the NY Times API)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SalesPercentilesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SalesPercentilesResultSet(response, path)
