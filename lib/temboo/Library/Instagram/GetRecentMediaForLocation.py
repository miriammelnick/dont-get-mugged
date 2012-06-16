
###############################################################################
#
# GetRecentMediaForLocation
# Retrieves a list of recent media objects from a given location.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRecentMediaForLocation(Choreography):

    """
    Create a new instance of the GetRecentMediaForLocation Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Instagram/GetRecentMediaForLocation')


    def new_input_set(self):
        return GetRecentMediaForLocationInputSet()

    def _make_result_set(self, result, path):
        return GetRecentMediaForLocationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecentMediaForLocationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRecentMediaForLocation
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRecentMediaForLocationInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((conditional, string) The access token retrieved during the Oauth 2.0 process. Required unless you provide the ClientID.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ClientID input for this choreography. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide the AccessToken.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the LocationID input for this choreography. ((required, integer) The ID for the location that you want to retrieve information for.)
        """
        def set_LocationID(self, value):
            InputSet._set_input(self, 'LocationID', value)

        """
        Set the value of the MaxID input for this choreography. ((optional, integer) Returns media after this max_id.)
        """
        def set_MaxID(self, value):
            InputSet._set_input(self, 'MaxID', value)

        """
        Set the value of the MaxTimestamp input for this choreography. ((optional, date) Returns media before this UNIX timestamp.)
        """
        def set_MaxTimestamp(self, value):
            InputSet._set_input(self, 'MaxTimestamp', value)

        """
        Set the value of the MinID input for this choreography. ((optional, integer) Returns media before this min_id.)
        """
        def set_MinID(self, value):
            InputSet._set_input(self, 'MinID', value)

        """
        Set the value of the MinTimestamp input for this choreography. ((optional, date) Returns media after this UNIX timestamp.)
        """
        def set_MinTimestamp(self, value):
            InputSet._set_input(self, 'MinTimestamp', value)


"""
A ResultSet with methods tailored to the values returned by the GetRecentMediaForLocation choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRecentMediaForLocationResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Instagram.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRecentMediaForLocationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecentMediaForLocationResultSet(response, path)
