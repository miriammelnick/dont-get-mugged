
###############################################################################
#
# GetCensusIDByTypeAndName
# Retrieve the U.S. census ID for a specified geography type and name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetCensusIDByTypeAndName(Choreography):

    """
    Create a new instance of the GetCensusIDByTypeAndName Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DataGov/GetCensusIDByTypeAndName')


    def new_input_set(self):
        return GetCensusIDByTypeAndNameInputSet()

    def _make_result_set(self, result, path):
        return GetCensusIDByTypeAndNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCensusIDByTypeAndNameChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetCensusIDByTypeAndName
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetCensusIDByTypeAndNameInputSet(InputSet):
        """
        Set the value of the GeographyName input for this choreography. ((required, string) Specify the geography name for the correspnding type, with at least three leading characters. For example, for the geography type "state" you could enter "ore" for Oregon.)
        """
        def set_GeographyName(self, value):
            InputSet._set_input(self, 'GeographyName', value)

        """
        Set the value of the GeographyType input for this choreography. ((required, string) Specify one of the following geography type values: "state", "county", "tract", "block", "congdistrict", "statehouse", "statesenate", "censusplace", or "msa" (metropolitan statistical area).)
        """
        def set_GeographyType(self, value):
            InputSet._set_input(self, 'GeographyType', value)

        """
        Set the value of the MaxResults input for this choreography. ((required, integer) Specify the maximum number of results to return. Defaults to 50.)
        """
        def set_MaxResults(self, value):
            InputSet._set_input(self, 'MaxResults', value)


"""
A ResultSet with methods tailored to the values returned by the GetCensusIDByTypeAndName choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetCensusIDByTypeAndNameResultSet(ResultSet):
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

class GetCensusIDByTypeAndNameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCensusIDByTypeAndNameResultSet(response, path)
