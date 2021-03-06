
###############################################################################
#
# Shout
# Creates a message in a user's shoutbox 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Shout(Choreography):

    """
    Create a new instance of the Shout Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/Shout')


    def new_input_set(self):
        return ShoutInputSet()

    def _make_result_set(self, result, path):
        return ShoutResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShoutChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Shout
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ShoutInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((required, string) Your Last.fm API Secret.)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the Message input for this choreography. ((required, string) The message to post to the shoutbox.)
        """
        def set_Message(self, value):
            InputSet._set_input(self, 'Message', value)

        """
        Set the value of the SessionKey input for this choreography. ((required, string) The session key retrieved in the last step of the authorization process.)
        """
        def set_SessionKey(self, value):
            InputSet._set_input(self, 'SessionKey', value)

        """
        Set the value of the User input for this choreography. ((required, string) The name of the user to shout on.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the Shout choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ShoutResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ShoutChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShoutResultSet(response, path)
