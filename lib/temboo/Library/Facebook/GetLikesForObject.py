
###############################################################################
#
# GetLikesForObject
# Retrieves likes for a specified Graph API object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetLikesForObject(Choreography):

    """
    Create a new instance of the GetLikesForObject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/GetLikesForObject')


    def new_input_set(self):
        return GetLikesForObjectInputSet()

    def _make_result_set(self, result, path):
        return GetLikesForObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLikesForObjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetLikesForObject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetLikesForObjectInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ObjectID input for this choreography. ((required, integer) The id of a graph api object to get likes for.)
        """
        def set_ObjectID(self, value):
            InputSet._set_input(self, 'ObjectID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetLikesForObject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetLikesForObjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) The response from Facebook. Returns "true" on success.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetLikesForObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLikesForObjectResultSet(response, path)
