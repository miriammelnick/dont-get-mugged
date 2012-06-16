
###############################################################################
#
# GetFileInfo
# Retrieves information on a specified file in a user's Box.net account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetFileInfo(Choreography):

    """
    Create a new instance of the GetFileInfo Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/GetFileInfo')


    def new_input_set(self):
        return GetFileInfoInputSet()

    def _make_result_set(self, result, path):
        return GetFileInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetFileInfoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetFileInfo
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetFileInfoInputSet(InputSet):
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
        Set the value of the FileID input for this choreography. ((required, string) The id of the file that you want to retrieve info for. This id is returned in various API calls such as GetAccountTree. It is also viewable in your browser's URL bar when viewing the doc at box.com)
        """
        def set_FileID(self, value):
            InputSet._set_input(self, 'FileID', value)


"""
A ResultSet with methods tailored to the values returned by the GetFileInfo choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetFileInfoResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Box.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetFileInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetFileInfoResultSet(response, path)
