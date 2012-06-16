
###############################################################################
#
# CopyFile
# Copies a specified file into a Box.net folder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CopyFile(Choreography):

    """
    Create a new instance of the CopyFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/CopyFile')


    def new_input_set(self):
        return CopyFileInputSet()

    def _make_result_set(self, result, path):
        return CopyFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CopyFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CopyFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CopyFileInputSet(InputSet):
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
        Set the value of the DestinationID input for this choreography. ((required, string) The Box.net folder ID into which you're copying the file. Note that you can't copy a file into the same folder as the original file.)
        """
        def set_DestinationID(self, value):
            InputSet._set_input(self, 'DestinationID', value)

        """
        Set the value of the FileID input for this choreography. ((required, string) The Box.net ID of the file you want to copy.)
        """
        def set_FileID(self, value):
            InputSet._set_input(self, 'FileID', value)


"""
A ResultSet with methods tailored to the values returned by the CopyFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CopyFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Box.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CopyFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CopyFileResultSet(response, path)
