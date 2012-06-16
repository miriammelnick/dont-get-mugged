
###############################################################################
#
# ToggleFolderEmail
# Enables or disables the upload email address for a folder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ToggleFolderEmail(Choreography):

    """
    Create a new instance of the ToggleFolderEmail Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/ToggleFolderEmail')


    def new_input_set(self):
        return ToggleFolderEmailInputSet()

    def _make_result_set(self, result, path):
        return ToggleFolderEmailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ToggleFolderEmailChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ToggleFolderEmail
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ToggleFolderEmailInputSet(InputSet):
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
        Set the value of the Enable input for this choreography. ((required, boolean) Enter "1" (the default) to enable email uploads to the specified folder, or "0" to disable email uploads.)
        """
        def set_Enable(self, value):
            InputSet._set_input(self, 'Enable', value)

        """
        Set the value of the FolderID input for this choreography. ((required, string) The Box.net ID of the folder in which you want to put the new folder.  Defaults to "0", which is the root folder of the account.)
        """
        def set_FolderID(self, value):
            InputSet._set_input(self, 'FolderID', value)


"""
A ResultSet with methods tailored to the values returned by the ToggleFolderEmail choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ToggleFolderEmailResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Box.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ToggleFolderEmailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ToggleFolderEmailResultSet(response, path)
