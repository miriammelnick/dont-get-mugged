
###############################################################################
#
# ListUserVolumes
# List user volumes.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListUserVolumes(Choreography):

    """
    Create a new instance of the ListUserVolumes Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FilesAnywhere/ListUserVolumes')


    def new_input_set(self):
        return ListUserVolumesInputSet()

    def _make_result_set(self, result, path):
        return ListUserVolumesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListUserVolumesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListUserVolumes
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListUserVolumesInputSet(InputSet):
        """
        Set the value of the Token input for this choreography. ((required, string) The token retrieved from authentication.  Can be passed from the AccountLogin Choreo.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)

        """
        Set the value of the VaultFile input for this choreography. ((optional, vault file) The path to a vault file that you want to upload. Required unless using the FileContents input.)
        """


"""
A ResultSet with methods tailored to the values returned by the ListUserVolumes choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListUserVolumesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from FilesAnywhere.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListUserVolumesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListUserVolumesResultSet(response, path)
