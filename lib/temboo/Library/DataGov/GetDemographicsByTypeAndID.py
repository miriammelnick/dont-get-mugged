
###############################################################################
#
# GetDemographicsByTypeAndID
# Retrieve demographic data for a specified geography type and geography ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetDemographicsByTypeAndID(Choreography):

    """
    Create a new instance of the GetDemographicsByTypeAndID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DataGov/GetDemographicsByTypeAndID')


    def new_input_set(self):
        return GetDemographicsByTypeAndIDInputSet()

    def _make_result_set(self, result, path):
        return GetDemographicsByTypeAndIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDemographicsByTypeAndIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetDemographicsByTypeAndID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetDemographicsByTypeAndIDInputSet(InputSet):
        """
        Set the value of the DataVersion input for this choreography. ((optional, string) Specify the census data version to search, such as "jun2011" (the default).)
        """
        def set_DataVersion(self, value):
            InputSet._set_input(self, 'DataVersion', value)

        """
        Set the value of the GeographyIDs input for this choreography. ((conditional, integer) The geography IDs to search for. Separate multiple IDs by commas; a maximum of 10 IDs are allowed.)
        """
        def set_GeographyIDs(self, value):
            InputSet._set_input(self, 'GeographyIDs', value)

        """
        Set the value of the GeographyType input for this choreography. ((required, string) Specify one of the following geography type values: "state", "county", "tract", "block", "congdistrict", "statehouse", "statesenate", "censusplace", or "msa" (metropolitan statistical area).)
        """
        def set_GeographyType(self, value):
            InputSet._set_input(self, 'GeographyType', value)


"""
A ResultSet with methods tailored to the values returned by the GetDemographicsByTypeAndID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetDemographicsByTypeAndIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response returned from the API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetDemographicsByTypeAndIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetDemographicsByTypeAndIDResultSet(response, path)
