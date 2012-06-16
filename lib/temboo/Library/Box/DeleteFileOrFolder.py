
###############################################################################
#
# DeleteFileOrFolder
# Deletes a specified Box.net file or folder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteFileOrFolder(Choreography):

    """
    Create a new instance of the DeleteFileOrFolder Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/DeleteFileOrFolder')


    def new_input_set(self):
        return DeleteFileOrFolderInputSet()

    def _make_result_set(self, result, path):
        return DeleteFileOrFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteFileOrFolderChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteFileOrFolder
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteFileOrFolderInputSet(InputSet):
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
        Set the value of the TargetID input for this choreography. ((required, string) The Box.net ID of the file or folder you want to delete.)
        """
        def set_TargetID(self, value):
            InputSet._set_input(self, 'TargetID', value)

        """
        Set the value of the Target input for this choreography. ((required, string) The type of item to delete, either "file" (the default) or "folder".)
        """
        def set_Target(self, value):
            InputSet._set_input(self, 'Target', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteFileOrFolder choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteFileOrFolderResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Box.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteFileOrFolderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteFileOrFolderResultSet(response, path)
