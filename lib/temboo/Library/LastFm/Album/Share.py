
###############################################################################
#
# Share
# Allows you to share an album with one or more Last.fm users or other friends.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Share(Choreography):

    """
    Create a new instance of the Share Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LastFm/Album/Share')


    def new_input_set(self):
        return ShareInputSet()

    def _make_result_set(self, result, path):
        return ShareResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShareChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Share
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ShareInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Your Last.fm API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((string) Your Last.fm API Secret.)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the Album input for this choreography. ((string) The album name.)
        """
        def set_Album(self, value):
            InputSet._set_input(self, 'Album', value)

        """
        Set the value of the Artist input for this choreography. ((string) The artist name.)
        """
        def set_Artist(self, value):
            InputSet._set_input(self, 'Artist', value)

        """
        Set the value of the Message input for this choreography. ((optional, string) An optional message to send with the recommendation. If not supplied a default message will be used.)
        """
        def set_Message(self, value):
            InputSet._set_input(self, 'Message', value)

        """
        Set the value of the Public input for this choreography. ((optional, boolean) Optionally show in the sharing users activity feed. Defaults to 0 (false).)
        """
        def set_Public(self, value):
            InputSet._set_input(self, 'Public', value)

        """
        Set the value of the Recipient input for this choreography. ((string) A comma delimited list of email addresses or Last.fm usernames. Maximum is 10.)
        """
        def set_Recipient(self, value):
            InputSet._set_input(self, 'Recipient', value)

        """
        Set the value of the SessionKey input for this choreography. ((string) The session key retrieved in the last step of the authorization process.)
        """
        def set_SessionKey(self, value):
            InputSet._set_input(self, 'SessionKey', value)


"""
A ResultSet with methods tailored to the values returned by the Share choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ShareResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Last.fm.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ShareChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShareResultSet(response, path)
