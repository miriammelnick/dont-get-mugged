
###############################################################################
#
# InviteCollaborators
# Invites users to collaborate on a specified Box.net file or folder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class InviteCollaborators(Choreography):

    """
    Create a new instance of the InviteCollaborators Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/InviteCollaborators')


    def new_input_set(self):
        return InviteCollaboratorsInputSet()

    def _make_result_set(self, result, path):
        return InviteCollaboratorsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InviteCollaboratorsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the InviteCollaborators
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class InviteCollaboratorsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Box.net.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Addresses input for this choreography. ((optional, string) The email addresses for the collaborators you want to invite. Separate multiple addresses with commas (no spaces).)
        """
        def set_Addresses(self, value):
            InputSet._set_input(self, 'Addresses', value)

        """
        Set the value of the AuthToken input for this choreography. ((required, string) The authorization token provided by Box.net.)
        """
        def set_AuthToken(self, value):
            InputSet._set_input(self, 'AuthToken', value)

        """
        Set the value of the Notify input for this choreography. ((required, boolean) Enter "1" (the default) to send a notification email to the invited collaborators. Enter "0" to not send a notification.)
        """
        def set_Notify(self, value):
            InputSet._set_input(self, 'Notify', value)

        """
        Set the value of the Resend input for this choreography. ((required, boolean) Enter "1" to resend a notification email to the invited collaborators. Enter "0" (the default) to not resend a notification.)
        """
        def set_Resend(self, value):
            InputSet._set_input(self, 'Resend', value)

        """
        Set the value of the Role input for this choreography. ((required, string) The role to assign to the invited collaborators, either "editor" or "viewer" (the default).)
        """
        def set_Role(self, value):
            InputSet._set_input(self, 'Role', value)

        """
        Set the value of the TargetID input for this choreography. ((required, string) The Box.net ID of the file or folder to invite collaborators for.)
        """
        def set_TargetID(self, value):
            InputSet._set_input(self, 'TargetID', value)

        """
        Set the value of the Target input for this choreography. ((required, string) The type of item to invite collaborators for. Box.net currently only allows collaborators for folders; "file" will eventually be supported, but for now the default value is "folder".)
        """
        def set_Target(self, value):
            InputSet._set_input(self, 'Target', value)


"""
A ResultSet with methods tailored to the values returned by the InviteCollaborators choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class InviteCollaboratorsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Box.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class InviteCollaboratorsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return InviteCollaboratorsResultSet(response, path)
