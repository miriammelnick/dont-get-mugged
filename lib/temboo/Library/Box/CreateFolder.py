
###############################################################################
#
# CreateFolder
# Creates a new folder in the parent folder you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateFolder(Choreography):

    """
    Create a new instance of the CreateFolder Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/CreateFolder')


    def new_input_set(self):
        return CreateFolderInputSet()

    def _make_result_set(self, result, path):
        return CreateFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateFolderChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateFolder
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateFolderInputSet(InputSet):
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
        Set the value of the Name input for this choreography. ((required, string) The name of the folder to create.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the ParentID input for this choreography. ((required, string) The Box.net ID of the folder in which you want to put the new folder.  Defaults to "0", which is the root folder of the account.)
        """
        def set_ParentID(self, value):
            InputSet._set_input(self, 'ParentID', value)

        """
        Set the value of the Share input for this choreography. ((required, boolean) Enter "1" to allow the new folder to be shared, or "0" (the default) to keep it private.)
        """
        def set_Share(self, value):
            InputSet._set_input(self, 'Share', value)


"""
A ResultSet with methods tailored to the values returned by the CreateFolder choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateFolderResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Box.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateFolderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateFolderResultSet(response, path)
