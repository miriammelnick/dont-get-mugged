
###############################################################################
#
# UnlikeObject
# Allows a user to "unlike" a Graph API object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UnlikeObject(Choreography):

    """
    Create a new instance of the UnlikeObject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/UnlikeObject')


    def new_input_set(self):
        return UnlikeObjectInputSet()

    def _make_result_set(self, result, path):
        return UnlikeObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UnlikeObjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UnlikeObject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UnlikeObjectInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ObjectID input for this choreography. ((required, integer) The id of a graph api object to unlike.)
        """
        def set_ObjectID(self, value):
            InputSet._set_input(self, 'ObjectID', value)


"""
A ResultSet with methods tailored to the values returned by the UnlikeObject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UnlikeObjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) The response from Facebook. Returns "true" on success.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UnlikeObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UnlikeObjectResultSet(response, path)
