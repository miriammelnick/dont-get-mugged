
###############################################################################
#
# RetrieveFolderItems
# Retrieves only the files and/or folders contained within the specified folder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveFolderItems(Choreography):

    """
    Create a new instance of the RetrieveFolderItems Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/RetrieveFolderItems')


    def new_input_set(self):
        return RetrieveFolderItemsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveFolderItemsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveFolderItemsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveFolderItems
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveFolderItemsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The APIKey provided by Box when registering for a developer account.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the AuthToken input for this choreography. ((required, string) Authorization Token retrieved by following the Oauth process described in Box.net API documentation.)
        """
        def set_AuthToken(self, value):
            InputSet._set_input(self, 'AuthToken', value)

        """
        Set the value of the FolderID input for this choreography. ((optional, string) The id of the folder that you want to retrieve items for. This id is returned in various API calls such as GetAccountTree. It is also viewable in your browser's URL bar when viewing the folder at box.)
        """
        def set_FolderID(self, value):
            InputSet._set_input(self, 'FolderID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the VaultFile input for this choreography. ((optional, vault file) The path to a vault file that you want to upload. Required unless using the FileContents input.)
        """


"""
A ResultSet with methods tailored to the values returned by the RetrieveFolderItems choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveFolderItemsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Box.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveFolderItemsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveFolderItemsResultSet(response, path)
