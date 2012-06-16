
###############################################################################
#
# LikeObject
# Allows a user to "like" a Graph API object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class LikeObject(Choreography):

    """
    Create a new instance of the LikeObject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/LikeObject')


    def new_input_set(self):
        return LikeObjectInputSet()

    def _make_result_set(self, result, path):
        return LikeObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LikeObjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the LikeObject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LikeObjectInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ObjectID input for this choreography. ((required, integer) The id of a graph api object that you like.)
        """
        def set_ObjectID(self, value):
            InputSet._set_input(self, 'ObjectID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the LikeObject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LikeObjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) The response from Facebook. Returns "true" on success.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LikeObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LikeObjectResultSet(response, path)
