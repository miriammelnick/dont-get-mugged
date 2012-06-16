
###############################################################################
#
# GetCensusIDByCoordinates
# Retrieve the U.S. census block geography ID for a specified latitude and longitude. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetCensusIDByCoordinates(Choreography):

    """
    Create a new instance of the GetCensusIDByCoordinates Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DataGov/GetCensusIDByCoordinates')


    def new_input_set(self):
        return GetCensusIDByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return GetCensusIDByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCensusIDByCoordinatesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetCensusIDByCoordinates
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetCensusIDByCoordinatesInputSet(InputSet):
        """
        Set the value of the GeographyType input for this choreography. ((required, string) Specify one of the following geography type values: "state", "county", "tract", "block", "congdistrict", "statehouse", "statesenate", "censusplace", or "msa" (metropolitan statistical area).)
        """
        def set_GeographyType(self, value):
            InputSet._set_input(self, 'GeographyType', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) Specify a latitude to search for, such as "41.486857".)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) Specify a longitude to search for, such as "-71.294392".)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)


"""
A ResultSet with methods tailored to the values returned by the GetCensusIDByCoordinates choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetCensusIDByCoordinatesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response returned from the API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "CensusID" output from this choreography execution. ((integer) The ID retrieved from the API call.)
        """
        def get_CensusID(self):
            return self._output.get('CensusID', None)

class GetCensusIDByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCensusIDByCoordinatesResultSet(response, path)
