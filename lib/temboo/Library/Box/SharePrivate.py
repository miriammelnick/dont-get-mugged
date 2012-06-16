
###############################################################################
#
# SharePrivate
# Share a specified Box.net file or folder privately.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SharePrivate(Choreography):

    """
    Create a new instance of the SharePrivate Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/SharePrivate')


    def new_input_set(self):
        return SharePrivateInputSet()

    def _make_result_set(self, result, path):
        return SharePrivateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SharePrivateChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SharePrivate
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SharePrivateInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Box.net.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Addresses input for this choreography. ((required, string) The email addresses for the users you want to notify of the shared item. Separate multiple addresses with commas (no spaces).)
        """
        def set_Addresses(self, value):
            InputSet._set_input(self, 'Addresses', value)

        """
        Set the value of the AuthToken input for this choreography. ((required, string) The authorization token provided by Box.net.)
        """
        def set_AuthToken(self, value):
            InputSet._set_input(self, 'AuthToken', value)

        """
        Set the value of the Message input for this choreography. ((required, string) The text of the email message sent to users about the newly shared file or folder.)
        """
        def set_Message(self, value):
            InputSet._set_input(self, 'Message', value)

        """
        Set the value of the Notify input for this choreography. ((required, boolean) Enter "1" to send a notification email to the users the item is shared with. Enter "0" (the default) to not send a notification.)
        """
        def set_Notify(self, value):
            InputSet._set_input(self, 'Notify', value)

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
A ResultSet with methods tailored to the values returned by the SharePrivate choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SharePrivateResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Box.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SharePrivateChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SharePrivateResultSet(response, path)
