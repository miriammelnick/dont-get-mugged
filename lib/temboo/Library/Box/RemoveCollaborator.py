
###############################################################################
#
# RemoveCollaborator
# Removes a collaborator from a Box.net file or folder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RemoveCollaborator(Choreography):

    """
    Create a new instance of the RemoveCollaborator Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/RemoveCollaborator')


    def new_input_set(self):
        return RemoveCollaboratorInputSet()

    def _make_result_set(self, result, path):
        return RemoveCollaboratorResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RemoveCollaboratorChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RemoveCollaborator
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RemoveCollaboratorInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Box.net.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the AuthToken input for this choreography. ((required, string) Authorization Token retrieved by following the Oauth process described in Box.net API documentation.)
        """
        def set_AuthToken(self, value):
            InputSet._set_input(self, 'AuthToken', value)

        """
        Set the value of the CollaborationID input for this choreography. ((required, string) The Box.net ID of the collaboration to remove.)
        """
        def set_CollaborationID(self, value):
            InputSet._set_input(self, 'CollaborationID', value)


"""
A ResultSet with methods tailored to the values returned by the RemoveCollaborator choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RemoveCollaboratorResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Box.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RemoveCollaboratorChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RemoveCollaboratorResultSet(response, path)
