
###############################################################################
#
# SharePublic
# Share a specified Box.net file or folder publicly.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SharePublic(Choreography):

    """
    Create a new instance of the SharePublic Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/SharePublic')


    def new_input_set(self):
        return SharePublicInputSet()

    def _make_result_set(self, result, path):
        return SharePublicResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SharePublicChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SharePublic
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SharePublicInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Box.net.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Addresses input for this choreography. ((optional, string) The email addresses for the users you want to notify of the shared item. Separate multiple addresses with commas (no spaces).)
        """
        def set_Addresses(self, value):
            InputSet._set_input(self, 'Addresses', value)

        """
        Set the value of the AuthToken input for this choreography. ((required, string) The authorization token provided by Box.net.)
        """
        def set_AuthToken(self, value):
            InputSet._set_input(self, 'AuthToken', value)

        """
        Set the value of the Message input for this choreography. ((optional, string) The text of the email message sent to users about the newly shared file or folder.)
        """
        def set_Message(self, value):
            InputSet._set_input(self, 'Message', value)

        """
        Set the value of the Password input for this choreography. ((optional, string) A password to protect the shared file or folder.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the TargetID input for this choreography. ((required, string) The Box.net ID of the file or folder to share.)
        """
        def set_TargetID(self, value):
            InputSet._set_input(self, 'TargetID', value)

        """
        Set the value of the Target input for this choreography. ((required, string) They type of item to share, either "file" (the default) or "folder".)
        """
        def set_Target(self, value):
            InputSet._set_input(self, 'Target', value)


"""
A ResultSet with methods tailored to the values returned by the SharePublic choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SharePublicResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Box.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SharePublicChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SharePublicResultSet(response, path)
